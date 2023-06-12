import menu

def entra_vendedor(produto_vendedor: dict, vendedor: dict):
    print('            __-¨-= MENU DO PRODUTO =-¨-__')
    print('                        º              ')
    print('1 - Cadastrar.')
    print('2 - Login. ')
    print('=-' * 25)
    op = int(input('Digite a opção: '))

    while (op != 0 and op != 1 and op != 2):
        print('- x x Opção inválida x x -')
        op = int(input('Digite a opção desejada: '))

    if (op == 1):
        print('            __-¨-¨-= CADASTRO =-¨-¨__')
        print('                        º              ')
        cadastro = input('E-mail: ')
        print('=-' * 25)

        while (cadastro.find('@') == -1 or cadastro.find('.com') == -1):
            print('-x E-mail Inválido (deve conter > @ e .com <). x-')
            cadastro = input('Digite o E-mail novamente: ')
            print('=-' * 25)

        vendedor['e-mail'] = cadastro

        senha_cadastro = input('Senha: ')
        print('=-' * 25)

        while (len(senha_cadastro) < 7 or len(senha_cadastro) > 10):
            print('-x A senha deve conter 7 a 10 caracteres. x-')
            senha_cadastro = input('Digite a Senha novamente: ')
            print('=-' * 25)

        vendedor['senha'] = senha_cadastro

        nome = input('Digite seu nome: ')
        print('=-' * 25)

        while (nome.isspace() == True or nome == ''):
            print('x Não contêm informações. x')
            nome = input('Digite seu Nome novamente: ')
            print('=-' * 25)

        vendedor['nome'] = nome

        cpf = input('CPF: ')
        print('=-' * 25)

        while (cpf.isspace() == True or cpf == ''):
            print('-x Não contêm informações. x-')
            cpf = input('Digite o CPF novamente: ')
            print('=-' * 25)

        while (len(cpf) != 11):
            print('-x CPF inválido. x-')
            cpf = input('Digite seu CPF novamente: ')
            print('=-' * 25)

        while (cpf.isdigit() == False):
            print('-x Isso não é um CPF. x-')
            cpf = input('Digite o CPF novamente: ')
            print('=-' * 25)

        vendedor['cpf'] = cpf

        num = input('Telefone(Celular): ')
        print('=-' * 25)

        while (num.isspace() == True or num == ''):
            print('-x Não contêm informações. x-')
            num = input('Digite o número novamente: ')
            print('=-' * 25)

        while (len(num) != 11):
            print('-x Número inválido. x-')
            num = input('Digite o Telefone(Celular) novamente: ')
            print('=-' * 25)

        while (num.isdigit() == False):
            print('-x Isso não é um número. x-')
            num = input('Digite o Telefone(Celular) novamente: ')
            print('=-' * 25)

        vendedor['num'] = num

        ende = input('Endereço: ')
        print('=-' * 25)

        while (ende.isspace() == True or ende == ''):
            print('-x Não contêm informações. x-')
            ende = input('Digite o Endereço novamente: ')
            print('=-' * 25)

        vendedor['endereco'] = ende

        nume = input('Número da casa: ')
        print('=-' * 25)

        while (nume.isspace() == True or nume == ''):
            print('-x Não contêm informações. x-')
            nume = input('Digite o Endereço novamente: ')
            print('=-' * 25)

        vendedor['nume'] = nume

        city = input('Cidade: ')
        print('=-' * 25)

        while (city.isspace() == True or city == ''):
            print('-x Não contêm informações. x-')
            city = input('Digite a Cidade novamente: ')
            print('=-' * 25)

        vendedor['cidade'] = city

        sigla = input('Sigla do estado: ')
        print('=-' * 25)

        while (len(sigla) != 2 or sigla != sigla.upper()):
            print('-x Sigla inválido. Deve ser Dois caracteres e Maiúsculos. x-')
            sigla = input('Digite a Sigla do seu estado novamente: ')
            print('=-' * 25)

        vendedor['estado'] = sigla

        vendedor['produto_vendedor'] = [produto_vendedor]

        print('                        º              ')
        print('        __-¨-¨-= DADOS CADASTRADOS =-¨-__')
        print('                        º              ')

    if (op == 2):
        print('            __-¨-¨-= LOGIN =-¨-__')
        print('                       º              ')
        login = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        print('=-' * 25)

        achou = False

        if (vendedor["e-mail"] == login and vendedor["senha"] == senha):
            achou = True
            print(f' -| Login realizado. Bem-vindo *_- {vendedor["nome"]} -_* |-')
            print('=-' * 25)

        while (achou == False):
            print('E-mail ou senha incorreto.')
            print('=-' * 25)
            login = input('Digite seu e-mail: ')
            senha = input('Digite sua senha: ')
            print('=-' * 25)

            if (vendedor["e-mail"] == login and vendedor["senha"] == senha):
                achou = True
                print(f' -| Login realizado. Bem-vindo *_- {vendedor["nome"]} -_* |-')
                print('=-' * 25)