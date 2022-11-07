
filename = 'gsheet_infos.txt'

def set_gsheet_id(newId:str):
    arquivo = open(filename, 'a')
    arquivo.seek(0)
    arquivo.truncate()
    arquivo.write(newId)
    
def get_gsheet_id():
    arquivo = open(filename, 'r')
    return arquivo.readline()
    

set_gsheet_id('1Piami0of4IQwRWdsFqpZm8uJvNY99z8toHCYOIRlkt')
print(get_gsheet_id())