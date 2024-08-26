from db.load import load_data
from db.save import save_data
from db.destroy import delete_data
from db.update import update_data

FILENAME = r'db/students.json'

def managment_students(option):
    match option:
        case 1:
            name = input("informe o nome do aluno: ")
            document = input("informe o CPF do aluno: ")
            return create(name, document)
        case 2:
            return list_students()
        case 3:
            code = input("informe o código de registro do aluno: ")
            name = input("informe o nome a ser alterado: ")
            document = input("informe o CPF a ser alterado: ")
            return update(code, name, document)
        case 4:
            code = input("informe o código de registro do aluno: ")
            return delete(code)
        case _:
            return "error"

def create(name, document):
    students = load_data(FILENAME)

    last_code = max((student['code'] for student in students), default=0)
    new_code = last_code + 1
    
    new_student = {
        "code": new_code,
        "name": name,
        "document": document
    }
    
    students.append(new_student)
    save_data(students, FILENAME)
    return new_student

def list_students():
    students = load_data()
    return students

def update(code, name, document):
    code = int(code)
    data = {
        "name": name,
        "document": document
    }
    return update_data(code, data, FILENAME)
    

def delete(code):
    return delete_data(code, FILENAME)

# Exemplos de uso
if __name__ == "__main__":
    # Criar um novo aluno
    print(managment_students(1, "Alice", "123456789"))

    # Listar todos os alunos
    print(managment_students(2))

    # Atualizar um aluno existente
    print(managment_students(3, 1, "Alice Smith", "987654321"))

    # Deletar um aluno
    print(managment_students(4, 1))