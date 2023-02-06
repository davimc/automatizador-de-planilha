import datetime
import pdf.pdf_payment_handler as handler

__dict_flag = {'slz':'sao luiz','patio norte': 'pátio norte', 'holandeses':"Olho Dagua","gaia aeroporto":'Gaia Cafe','gaia holandeses':'gaia cafe Gastronomia'}


def translate(store_name:str):
    return __dict_flag[store_name] if store_name in __dict_flag.keys() else store_name

    
def validate_pdf(store_name:str, day = datetime.datetime.now().day-1):
    data = datetime.datetime.now()
    month = data.month
    year = data.year
    data = (('0' if int(day)<10 else '') + str(day)+'/'+ ('0' if month<10 else '') + str(month)+'/'+str(year))
    dataFinal = (('0' if int(day)<10 else '') + str(day)+'/'+ ('0' if month<10 else '') + str(month-1)+'/'+str(year))
    pdf = handler.read_pdf(store_name+'.pdf')
    
    store_name = translate(store_name)
    return True
    #(str.upper(store_name) in pdf[1] and ((data in pdf[1]) or (dataFinal in pdf[1])))


# def test():    
#     stores = store.get_names()[0]

    

#     for x in (stores):
        
#         print(validate_pdf(store_name =x, day=20 if x!='slz' else 19))
        
# test()
    