import pdf.pdf_payment_handler as pdf_handler

import spreadsheet.gsheets_payment_handler as gsheets
import file.file_handler as file_handler

def fill_gsheet():
    day = input('Informe o dia a ser populado: ')
    gsheets.populate_sheet(day)
    
def set_file_id():
    try:
        new_id = input('Informe o id para a planilha do novo mês: ')
        file_handler.set_gsheet_id(new_id)
        print('Nova planilha cadastrada')
    except Exception as error:
        print(err)
    
def menu():
    
    choice = input('1.Popular planilha\n' +
                '2.Alterar id da planilha\n')
    match choice:
        case '1':
            fill_gsheet()
        case '2': 
            set_file_id()
            menu()
        case _:
            print('Opção não identificada')
            menu()
            
if __name__ == '__main__':
    menu()
