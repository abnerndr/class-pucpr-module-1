from db.load import load_data
from db.save import save_data

def update_data(code, data, FILENAME):
    items = load_data(FILENAME)
    
    for item in items:
        if item['code'] == code:
            # atualiza os campos do item baseado no código fornecido
            for key, value in data.items():
                if key in item:
                    item[key] = value 
                 # salva o item com os campos atualizados que foram inseridos 
            save_data(items, FILENAME)
            return items
    
    return "nenhum registro encontrado"
