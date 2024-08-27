import os
from db.load import load_data
from db.save import save_data
from db.destroy import delete_data
from db.update import update_data

# Função para gerar o caminho completo para o arquivo JSON na pasta 'db'
def get_file_path(filename):
    return os.path.join("db", filename)

def managment_choice(option, filename):
    filepath = get_file_path(filename)
    match option:
        case 1:
            name = input(f"informe o nome do {filename[:-5]}: ")
            document = input(f"informe o CPF do {filename[:-5]}: ")
            return create(name, document, filepath)
        case 2:
            return list_items(filepath)
        case 3:
            code = input(f"informe o código de registro do {filename[:-5]}: ")
            name = input(f"informe o nome a ser alterado: ")
            document = input(f"informe o CPF a ser alterado: ")
            return update(code, name, document, filepath)
        case 4:
            code = input(f"informe o código de registro do {filename[:-5]}: ")
            return delete(code, filepath)
        case _:
            return "error"

def create(name, document, filepath):
    items = load_data(filepath)

    last_code = max((item['code'] for item in items), default=0)
    new_code = last_code + 1
    
    new_item = {
        "code": new_code,
        "name": name,
        "document": document
    }
    
    items.append(new_item)
    save_data(items, filepath)
    return new_item

def list_items(filepath):
    items = load_data(filepath)
    return items

def update(code, name, document, filepath):
    code = int(code)
    data = {
        "name": name,
        "document": document
    }
    return update_data(code, data, filepath)

def delete(code, filepath):
    return delete_data(code, filepath)
