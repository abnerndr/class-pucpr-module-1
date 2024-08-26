from db.load import load_data
from db.save import save_data


def update_data(code, data, FILENAME):
    items = load_data(FILENAME)
    
    for item in items:
        if item['code'] == code:
            item = data
            save_data(FILENAME, items)
            return items
    
    return "nenhum registro encontrato"