from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Piami0of4IQwRWdsFqpZm8uJvNY99z8toHCYOIRlkt4'
RANGE_SUBWAY = 'B5:H12'
RANGE_RESTAURANT = 'B15:H16'


def __get_credentials():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def __get_sheet(creds):
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    return sheet
    
def __has_already_populated(sheet, day):
    
    result_subway = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_SUBWAY).execute()
    
    result_restaurant = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_RESTAURANT).execute()
            
    if('values' in result_subway or 'values' in result_restaurant):
        raise Exception("Planilha já populada")

def __simulator(sheet, day):
    
    result_subway = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_SUBWAY).execute()
    
    result_restaurant = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= day+"!"+RANGE_RESTAURANT).execute()
    
    return (result_subway, result_restaurant)

def __populate(sheet, day:str, stores_results):
    subway_results = {
        'values': stores_results[0]
    }
    restaurant_results = {
        'values': stores_results[1]
    }
    result_subway = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range= (day+"!"+RANGE_SUBWAY), valueInputOption="USER_ENTERED",body = subway_results).execute()
    result_restaurant = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
       range= day+"!"+RANGE_RESTAURANT, valueInputOption="USER_ENTERED",body = restaurant_results).execute()
def populate_sheet(day):
    
    try:
        creds = __get_credentials()    
        sheet = __get_sheet(creds)
        __has_already_populated(sheet,day)
        (result, result2) = __simulator(sheet, "1")
        
        __populate(sheet, day, stores_results=[result['values'], result2['values']])
        


    except HttpError as err:
        print(err)


if __name__ == '__main__':
    try:
        populate_sheet("29")
    except Exception as err:
        print(err)