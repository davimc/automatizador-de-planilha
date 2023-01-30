from fileinput import filename
from operator import contains
import PyPDF2

import os.path
from utils.payment_methods_enum import get_methods
import utils.store as store
from utils.validate import validate_pdf

basedir = os.path.abspath(os.path.dirname(__file__))

payment_methods = get_methods()




def stores_results(day):
    subs_results = {}
    rest_results = {}
    stores = store.get_names()
    for x in stores[0]:
        if(validate_pdf(x, day)):
            subs_results[x] = __result_payment(x)
        else:
            raise Exception("documento " + x + " está com o dia ou nome incorreto")
    for x in stores[1]:
        if(validate_pdf(x, day)):
            rest_results[x] = __result_payment(x)    
        else:
            raise Exception("documento " + x + " está com o dia ou nome incorreto")
    return(subs_results, rest_results)


def __result_payment(file_name):
    try:
        text = read_pdf(file_name)
        
        txt_payments = __extract_payments(text)
        total = __extract_total_payments(text)
          
        total_formas = {}
        for i in payment_methods:
            total_formas[i] = 0.0
            for j in range(len(payment_methods[i])):
                for k in range(len(txt_payments)):
                    if(txt_payments[k].find(payment_methods[i][j]) != -1):
                        total_formas[i] += __formater_to_float(txt_payments[k].split(payment_methods[i][j])[1])
                        break

        aux = 0.0
        for i in total_formas:
            aux += total_formas[i]
        
        return (total_formas,total) if __test_total(total_formas, total) else False
    except FileNotFoundError as error:
        print('o arquivo ' + file_name + ' não pode ser localizado. Tente novamente')
    except ValueError as error:
        print(error)
        

def read_pdf(file_name):
    file_name = file_name if(file_name.__contains__('.pdf')) else file_name +'.pdf'
    pdf_file = open(basedir+'/../../reports/'+file_name, 'rb')
        
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(0)
    page_content = page.extractText(5)
    text = page_content.split('\n')
    pdf_file.close()
    
    return text

def __formater_to_float(x:str):
    x = x.replace('R$ ', '')
    x = x.replace('.','')
    x = x.replace(',','.')

    return float(x)
    
def __extract_payments(text):
    txt_payments = []
    for i in range(3,len(text)-2):
            txt_payments.append(text[i])
    return txt_payments        
    
def __extract_total_payments(txt):
    total = __formater_to_float(txt[-2])
    
    return total

def __test_total(total_formas:dict,total:float):
    aux = 0.0
    for i in total_formas:
        aux += total_formas[i]
    return round(aux,2) == round(total,2)