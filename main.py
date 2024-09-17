from choice import managment_choice

def main():
    print("----- MENU PRINCIPAL -----")
    return input_mode('choice')

# cria a exibição para selecionar o primeiro item
def input_mode(item):
    match item:
        case 'choice':
            return int(input("(1) Gerenciar estudantes.\n(2) Gerenciar professores.\n(3) Gerenciar disciplinas.\n(4) Gerenciar turmas.\n(5) Gerenciar matriculas.\n(9) Sair.\n\nInforme a opcao desejada: "))
        case 'operation':
            return int(input("(1) Incluir.\n(2) Listar.\n(3) Atualizar.\n(4) Excluir.\n(9) Voltar ao menu principal.\nInforme a acao desejada: "))
        case _:
            return "nenhum input mode selecionado"

# seleciona o titulo e o arquivo baseado na opção para exibir depois e já aproveito para nomear o json que vai ser criado no 'db'
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

# exibe o menu de operação baseado na escolha do usuário
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
            print_item(item)
    else:
        print(result)

def print_item(item):
    print("-" * 30)  # Linha de separação entre os registros
    for key, value in item.items():
        print(f"{key.capitalize()}: {value}")
    print("-" * 30)

# laço de repetição para manter a aplicação ativa
while True:
    choice = main()
    if choice == 9:
        break
    option(choice)
