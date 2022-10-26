import handler_pdf_payment as pdf_handler
import store

def stores_results():
    stores_results = {}
    for x in store.get_names():
        stores_results[x] = pdf_handler.result_payment(x+'.pdf')
    return stores_results

