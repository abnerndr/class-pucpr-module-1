import os
from db.load import load_data
from db.save import save_data
from db.destroy import delete_data
from db.update import update_data

# gera o caminho com o JSON na pasta 'db' e savlvar o arquivo pelo nome
def get_file_path(filename):
    return os.path.join("db", filename)

# gerencia as opções de CRUD baseado no menu da main.py
def managment_choice(option, filename):
    filepath = get_file_path(filename)
    
    entity = filename.split('.')[0]  # Extrai 'students', 'teachers' ...
    
    # seleciona a opção e baseado na entidade chama os items dinamicos no passo a baixo
    match option:
        case 1:
            return create(entity, filepath)
        case 2:
            return list_items(filepath)
        case 3:
            code = input(f"informe o código de registro do {entity}: ")
            return update(code, entity, filepath)
        case 4:
            code = input(f"informe o código de registro do {entity}: ")
            return delete(code, filepath)
        case _:
            return "Opção inválida."

# cria novos registros baseado na entidade
def create(entity, filepath):
    items = load_data(filepath)

    last_code = max((item['code'] for item in items), default=0)
    new_code = last_code + 1

    # seleciona a estrutura de dados baseado na entidade
    if entity == 'students':
        name = input("Informe o nome do estudante: ")
        document = input("Informe o CPF do estudante: ")
        new_item = {"code": new_code, "name": name, "document": document}
    
    elif entity == 'teachers':
        name = input("Informe o nome do professor: ")
        document = input("Informe o CPF do professor: ")
        subject = input("Informe a disciplina do professor: ")
        new_item = {"code": new_code, "name": name, "document": document, "subject": subject}
    
    elif entity == 'courses':
        name = input("Informe o nome da disciplina: ")
        tutor = input("Informe o nome do professor responsável pela disciplina: ")
        new_item = {"code": new_code, "name": name, "tutor": tutor}
    
    elif entity == 'classes':
        name = input("Informe o nome da turma: ")
        quantidade_alunos = input("Informe a quantidade de alunos: ")
        tutor = input("Informe o nome do professor responsável pela turma: ")
        new_item = {"code": new_code, "name": name, "quantidade_alunos": quantidade_alunos, "tutor": tutor}
    
    elif entity == 'enrollments':
        turma = input("Informe o nome da turma: ")
        aluno = input("Informe o nome do aluno: ")
        tutor = input("Informe o nome do professor responsável pela matricula: ")
        new_item = {"code": new_code, "turma": turma, "aluno": aluno, "tutor": tutor}
    
    else:
        return "Entidade desconhecida."

    # salva o item selecionado com seus campos
    items.append(new_item)
    save_data(items, filepath)
    return new_item

# lista baseado no arquivo JSON
def list_items(filepath):
    items = load_data(filepath)
    return items

# atualiza registro baseado no código
def update(code, entity, filepath):
    code = int(code)
    items = load_data(filepath)
    
    # procura items no código e devolve uma exibição para visualizar antes de editar
    item_to_update = None
    for item in items:
        if item['code'] == code:
            item_to_update = item
            break

    if not item_to_update:
        return "Nenhum dado encontrado para o código fornecido."
    
    print(f"\nAtualizando o registro com código {code}:\n")
    
    # exibi os campos capturado no item_to_update
    data = {}
    for key, current_value in item_to_update.items():
        if key != 'code':  # faz com que seja impossível alterar o código pois ele funciona como chave primária
            new_value = input(f"Valor atual de '{key}': {current_value}. Informe o novo valor (ou deixe em branco para manter o atual): ")
            if new_value:
                data[key] = new_value
            else:
                data[key] = current_value  # matem o valor atual se não for informado um novo valor
    
    return update_data(code, data, filepath)


# destroi registro baseado no código
def delete(code, filepath):
    return delete_data(code, filepath)
