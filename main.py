import os as shell
from choices.students import managment_students

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
            return "ESTUDANTES"
        case 2:
            return "PROFESSORES"
        case 3:
            return "DICIPLINAS"
        case 4:
            return "TURMAS"
        case 5:
            return "MATRICULAS"
        case _:
            return ""

def option(choice):
    title = select_title_option(choice)
    print(f"[{title}] - MENU DE OPERACAO\n")
    number = input_mode('operation')
    return managment_students(number)

while True:
    choice = main()
    option(choice) 