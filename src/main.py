import pdf.handler_pdf_payment as pdf_handler
import infos.store as store

def stores_results():
    stores_results = {}
    for x in store.get_names():
        stores_results[x] = pdf_handler.result_payment(x)
    return(stores_results)



results = stores_results()
for i in results:
    print(i)
    print(results[i])
    print(end='\n\n')    
