import os as shell
from choices.choice import managment_choice

def main():
    # shell.system("cls")
    print("----- MENU PRINCIPAL -----")
    return input_mode('choice')

def input_mode(item):
    match item:
        case 'choice':
            return int(input("(1) Gerenciar estudantes.\n(2) Gerenciar professores.\n(3) Gerenciar disciplinas.\n(4) Gerenciar turmas.\n(5) Gerenciar matriculas.\n(9) Sair.\n\nInforme a opcao desejada: "))
        case 'operation':
            return int(input("(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n(9) Voltar ao menu principal.\n Informe a acao desejada: "))
        case _:
            return "nenhum input mode selecionado"

def select_title_option(number):
    match number:
        case 1:
            return "ESTUDANTES", "students.json"
        case 2:
            return "PROFESSORES", "teachers.json"
        case 3:
            return "DISCIPLINAS", "courses.json"
        case 4:
            return "TURMAS", "classes.json"
        case 5:
            return "MATRICULAS", "enrollments.json"
        case _:
            return "", ""

def option(choice):
    title, filename = select_title_option(choice)
    if not title:
        print("Opção inválida!")
        return

    print(f"[{title}] - MENU DE OPERACAO\n")
    number = input_mode('operation')
    result = managment_choice(number, filename)

    if isinstance(result, list):
        for item in result:
            print(f"Código: {item['code']}\nNome: {item['name']}\nCPF: {item['document']}\n")
            print("-" * 30)  # Linha de separação entre os registros
    else:
        print(result)

while True:
    choice = main()
    if choice == 9:
        break
    option(choice)