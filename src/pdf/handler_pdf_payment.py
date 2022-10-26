import PyPDF2
from payments_type import payment

formas_pagamento = payment()


def result_payment(file_name):
    try:
        text = read_pdf(file_name)
        txt_pagamentos = []
        for i in range(3,len(text)-2):
            txt_pagamentos.append(text[i])

        total_formas = []
        for i in range(len(formas_pagamento)):
            total_formas.append(0.0)
            for j in range(len(formas_pagamento[i])):
                for k in range(len(txt_pagamentos)):
                    if(txt_pagamentos[k].find(formas_pagamento[i][j]) != -1):
                        aux = (txt_pagamentos[k].split(formas_pagamento[i][j])[1])
                        aux = aux.replace(',','.')
                        total_formas[i] += float(aux)
                        break

        return total_formas
    except FileNotFoundError as error:
        print('o arquivo '+ file_name + ' não pode ser localizado. Tente novamente')
        

def read_pdf(file_name):
    pdf_file = open(file_name, 'rb')
        
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page = read_pdf.getPage(0)
    page_content = page.extractText(5)
    text = page_content.split('\n')
    return text