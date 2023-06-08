import busca as bs
import menu
def entra_cliente(produto_cliente:dict, cliente:dict):
    print('            __-¨-= MENU DO CLIENTE =-¨-__')
    print('                        º              ')
    print('1 - Cadastrar.')
    print('2 - Login. ')
    print('=-' * 25)
    op_menu = int(input('Digite a opção desejada: '))

    while(op_menu != 0 and op_menu != 1 and op_menu != 2):
        print('- x x Opção inválida x x -')
        op_menu = int(input('Digite a opção desejada: '))

    if(op_menu == 1):
        print('            __-¨-¨-= CADASTRO =-¨-¨__')
        print('                        º              ')
        cadastro = input('E-mail: ')
        print('=-' * 25)

        while(cadastro.find('@') == -1 or cadastro.find('.com') == -1):
            print('-x E-mail Inválido (deve conter > @ e .com <). x-')
            cadastro = input('Digite o E-mail novamente: ')
            print('=-' * 25)

        cliente["email"] = cadastro

        senha_cadastro = input('Senha: ')
        print('=-' * 25)

        while(len(senha_cadastro) < 7 or len(senha_cadastro) > 10):
            print('-x A senha deve conter 7 a 10 caracteres. x-')
            senha_cadastro = input('Digite a Senha novamente: ')
            print('=-' * 25)

        cliente["senha"] = senha_cadastro

        nome = input('Digite seu nome: ')
        print('=-' * 25)

        while(nome.isspace() == True or nome == ''):
            print('x Não contêm informações. x')
            nome = input('Digite seu Nome novamente: ')
            print('=-' * 25)

        cliente["nome"] = nome

        cliente["produto_cliente"] = produto_cliente

        print('                        º              ')
        print('        __-¨-¨-= DADOS CADASTRADOS =-¨-__')
        print('                        º              ')
        print('            __-¨-= MENU DO CLIENTE =-¨-__')
        print('                        º              ')
        print('1 - Cadastrar.')
        print('2 - Login. ')
        print('=-' * 25)
        op_menu = int(input('Digite a opção desejada: '))

        while(op_menu != 0 and op_menu != 1 and op_menu != 2):
            print('- x x Opção inválida x x -')
            op_menu = int(input('Digite a opção desejada: '))


    if(op_menu == 2):
        print('            __-¨-¨-= LOGIN =-¨-__')
        print('                       º              ')
        login = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        print('=-' * 25)

        achou = False

        if (cliente["email"] == login and cliente["senha"] == senha):
            achou = True
            print(f' -| Login realizado. Bem-vindo *_- {cliente["nome"]} -_* |-')
            print('=-' * 25)

        if(achou == False):
            print('-x Login ou senha incorreta x-')
