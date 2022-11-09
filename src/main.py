import pdf.pdf_payment_handler as pdf_handler
import infos.store as store

import spreadsheet.gsheets_payment_handler as gsheets
import file.file_handler as file_handler

## TODO: ensure that the day of the pdfs are the same as the worksheet

def fill_gsheet():
    day = input('Informe o dia a ser populado: ')
    gsheets.populate_sheet(day)
    
def set_file_id():
    new_id = input('Informe o id para a planilha do novo mês: ')
    file_handler.set_gsheet_id(new_id)
    print('Nova planilha cadastrada')
    
def menu():
    while True:
        choice = input(f'1.Popular planilha\n' +
                 '2.Alterar id da planilha\n')
        match choice:
            case '1':
                fill_gsheet()
            case '2': 
                set_file_id()
            case _:
                print('Opção não identificada')
            
if __name__ == '__main__':
    menu()
