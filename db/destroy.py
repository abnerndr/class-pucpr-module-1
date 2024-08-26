from db.load import load_data
from db.save import save_data

def delete_data(code, FILENAME):
    items = load_data(FILENAME)

    new_item = [item for item in items if item['code'] != code]
    
    if len(new_item) < len(items):
        save_data(FILENAME, new_item)
        return "dado removido"
    return "erro - nenhum dado encontrado"