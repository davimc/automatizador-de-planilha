
filename = 'gsheet_infos.txt'

def set_gsheet_id(newId:str):
    arquivo = open('file/'+filename, 'a')
    arquivo.seek(0)
    arquivo.truncate()
    arquivo.write(newId)
    
def get_gsheet_id():
    arquivo = open('file/'+filename, 'r')
    return arquivo.readline()