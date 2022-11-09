
filename = 'gsheet_infos.txt'

def set_gsheet_id(newId:str):
    arquivo = open(filename, 'a')
    arquivo.seek(0)
    arquivo.truncate()
    arquivo.write(newId)
    
def get_gsheet_id():
    arquivo = open(filename, 'r')
    return arquivo.readline()