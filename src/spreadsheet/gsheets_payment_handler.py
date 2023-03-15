from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import file.file_handler as file_handler
from pdf.pdf_payment_handler import stores_results



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = file_handler.get_gsheet_id()

def __get_credentials():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def __get_sheet(creds):
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    return sheet
    
def __has_already_populated(sheet, day, RANGE_SUBWAY, RANGE_RESTAURANT):
    
    result_subway = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_SUBWAY).execute()
    
    result_restaurant = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_RESTAURANT).execute()
    # the only way the result's contain 'values' is if the spreadsheet has already been filled in or 
    # has its structure changed            
    if('values' in result_subway or 'values' in result_restaurant):
        raise ValueError("Planilha já populada")

def __populate(sheet, day:str, stores_results, RANGE_SUBWAY, RANGE_RESTAURANT):

    for x in range(len(stores_results)):
        results = {
            'values': list()
        }
        for y in (stores_results[x]):
            #what happened here
            #list transform in a list
            # stores_results[x] acess the list sub_result or rest_result
            #stores_results[x][y] access the dict inside 
            # stores_results[x][y][0] access the item of dict
            # stores_results[x][y][0].values() take just the values inside the dict 
            results['values'].append(list(stores_results[x][y][0].values()))
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range= day+"!"+ (RANGE_SUBWAY if x==0 else RANGE_RESTAURANT), valueInputOption="USER_ENTERED",body = results).execute()
    print('Planilha preenchida com sucesso')
        
def populate_sheet(day:str):
    try:
        (subs_results, rest_results) = stores_results(day)
        __initial_sub = 5
        __final_sub = __initial_sub + (len(subs_results)-1)
        __initial_rest = __final_sub + 3
        __final_rest = __initial_rest + (len(rest_results)-1)
        
        RANGE_SUBWAY = 'B'+str(__initial_sub)+':G' + str(__final_sub)
        RANGE_RESTAURANT = 'B'+str(__initial_rest)+':G'+ str(__final_rest)
        creds = __get_credentials()    
        sheet = __get_sheet(creds)
        __has_already_populated(sheet,day, RANGE_SUBWAY=RANGE_SUBWAY, RANGE_RESTAURANT=RANGE_RESTAURANT)
        
        __populate(sheet, day, stores_results=[subs_results, rest_results], RANGE_SUBWAY=RANGE_SUBWAY, RANGE_RESTAURANT=RANGE_RESTAURANT)
        

    except Exception as err:
        print(err)
    except HttpError as err:
        print(err)
    except ValueError as err:
        print(err)
