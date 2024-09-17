from db.load import load_data
from db.save import save_data

def delete_data(code, FILENAME):
    try:
        code = int(code)
    except ValueError:
        return "Erro - Código inválido. Certifique-se de inserir um número."

    # carrega os dados do arquivo pelo nome fornecido
    items = load_data(FILENAME)

    # filtra pelo código os items que tem no json
    new_items = [item for item in items if item['code'] != code]

    # verifica se deu certo a remoção de algum item
    if len(new_items) < len(items):
        save_data(new_items, FILENAME)
        return f"Dado com código {code} removido com sucesso."
    
    return f"Erro - Nenhum dado encontrado com o código {code}."
