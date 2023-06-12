import menu
import decoracao as de
import busca as bs
import cliente_login as cl
import vendedor_login as vl
import chatgpt as cg

cliente = {}
vendedor = {}
dados = []
produto_vendedor = {}
produto_cliente = {}
login = []
senha = []
op = -1

while(op != 0):
    menu.menu_inicial()
    op = int(input('Digite a opção desejada: '))
    print('=-' * 25)

    while(op != 0 and op != 1 and op != 2):
        print('- x x Opção inválida x x -')
        op = int(input('Digite a opção desejada: '))

    if(op == 1):
        op_login_cliente = -1
        cl.entra_cliente(produto_cliente, cliente)
        while(op_login_cliente != 0):
            menu.menu_principal_cliente()

            op_login_cliente = int(input('Digite sua opção: '))
            print('=-' * 25)

            if(op_login_cliente < 0 or op_login_cliente > 3):
                print('-x Opção inválida. x-')
                op_login_cliente = int(input('Digite sua opção: '))
                print('=-' * 25)

            elif(op_login_cliente == 1):
                sen = input('Digite a Senha antiga: ')
                print('=-' * 25)

                while(cliente['senha'] != sen):
                    print('-x Senha incorreta. x-')
                    sen = input('Digite novamente: ')
                    print('=-' * 25)

                senha_nova = input('Digite sua nova senha: ')
                print('=-' * 25)

                while (len(senha_nova) < 7 or len(senha_nova) > 10):
                    print('-x senha precisa ter entre 7 a 10 caracteres. x-')
                    senha_nova = input('Digite a senha novamente: ')
                    print('=-' * 25)

                cliente["senha"] = senha_nova
                print('- senha atualizada. -')
            elif(op_login_cliente == 2):
                produto_busca = input('Pesquisar: ')
                bs.buscar(produto_vendedor, produto_busca)
                menu.menu_produto()
                opp = int(input('Digite a opção desejada: '))
                if(opp == 1):
                    comprou = input('Digite o código do produto: ')
                    for remove in produto_vendedor.keys():
                        if(remove == comprou):
                            produto_cliente[remove] = produto_vendedor[comprou]
                            produto_vendedor.pop(comprou)
                            print('Produto comprado.')
                            break
                        else:
                            print('código inválido. ')
                            break
                elif(opp == 2):
                    descricao = input('Digite o código do produto. ')
                    print(cg.consultarchatgpt(produto_vendedor[descricao][0]))

            elif(op_login_cliente == 3):
                for z, x in produto_cliente.items():
                    print(
                        f'Codigo: {z}\nNome do produto: {x[0]}\nMarca do produto: {x[1]}\nEstado: {x[2]}\nDescrição: {x[3]}\nPreço: {x[4]}\nQuantidade: {x[5]}')
                    print('=-' * 25)
                if(produto_cliente == {} or produto_cliente == { }):
                    print('Produtos indisponíveis.')
                    print('=-' * 25)

    if(op == 2):
        op_login_vendedor = -1
        vl.entra_vendedor(produto_vendedor, vendedor)
        while(op_login_vendedor != 0):

            menu.menu_principal_vendedor()

            op_login_vendedor = int(input('Digite sua opção: '))
            print('=-' * 25)

            while(op_login_vendedor < 0 or op_login_vendedor > 6):
                print('-x Opção inválida. x-')
                op_login_cliente = int(input('Digite sua opção: '))
                print('=-' * 25)


            if(op_login_vendedor == 1):
                sen = input('Digite a Senha antiga: ')
                print('=-' * 25)

                while(vendedor['senha'] != sen):
                    print('-x Senha incorreta. x-')
                    sen = input('Digite novamente: ')
                    print('=-' * 25)

                senha_nova = input('Digite sua nova senha: ')
                print('=-' * 25)

                while (len(senha_nova) < 7 or len(senha_nova) > 10):
                    print('-x senha precisa ter entre 7 a 10 caracteres. x-')
                    senha_nova = input('Digite a senha novamente: ')
                    print('=-' * 25)

                vendedor['senha'] = senha_nova
                print('- senha atualizada. -')
            elif(op_login_vendedor == 2):
                nome_produto = input('Nome do produto: ')
                print('=-' * 25)

                while (nome_produto.isspace() == True or nome_produto == ''):
                    print('-x Não contêm informações. x-')
                    nome_produto = input('Digite novamente: ')
                    print('=-' * 25)

                marca = input('Marca do produto: ')
                print('=-' * 25)

                while (marca.isspace() == True or marca == ''):
                    print('-x Não contêm informações. x-')
                    marca = input('Digite novamente: ')
                    print('=-' * 25)

                nv = input('Estado de uso (novo ou usado): ')
                print('=-' * 25)

                while(nv != 'novo' and nv != 'usado'):
                    nv = input('-x Por favor, digite só se é NOVO ou USADO: ')
                    print('=-' * 25)

                descr = input('Descrição do Produto: ')
                print('=-' * 25)

                while (descr.isspace() == True or descr == ''):
                    print('-x Não contêm informações. x-')
                    descr = input('Digite novamente: ')
                    print('=-' * 25)

                preco = input('Preço do Produto: ')
                print('=-' * 25)

                while (preco.isspace() == True or preco == ''):
                    print('-x Não contêm informações. x-')
                    preco = input('Digite novamente: ')
                    print('=-' * 25)

                qntd = input('Quantidade do produto: ')
                print('=-' * 25)

                while(qntd.isspace() == True or qntd == ''):
                    print('-x Não contêm informações. x-')
                    qntd = input('Digite novamente: ')
                    print('=-' * 25)

                print('O código deve ser três números. ')
                cod = input('Crie um código para o produto: ')

                while(len(cod) != 3):
                    print('Esse código não tem três números. ')
                    cod = input('Crie um código para o produto: ')

                produto_vendedor[cod] = [nome_produto, marca, nv, descr, preco, qntd]

                print(f'Nome do produto: {nome_produto}\nMarca do produto: {marca}\nEstado de uso: {nv}\nDescrição do Produto: {descr}\nPreço: {preco}\nQuantidade(s): {qntd}')
                print('=-' * 25)

            elif(op_login_vendedor == 3):
                remover_produto = input('Qual produto deseja remover: ')
                print('=-' * 25)
                bs.buscar(produto_vendedor, remover_produto)
                produto_vendedor.pop(remover_produto)

                print('_-| Produto removido |-_')
                print('=-' * 25)

            elif(op_login_vendedor == 4):
                ache = input('Buscar produtos: ')
                print('=-' * 25)

                bs.buscar(produto_vendedor, ache)

            elif(op_login_vendedor == 5):
                atualizar = input('Digite o Produto que quer Atualizar: ')
                print('=-' * 25)

                bs.buscar(produto_vendedor, atualizar)
                novo_marca = input('Atualizar Marca do Produto: ')
                print('=-' * 25)

                while (novo_marca.isspace() == True or novo_marca == ''):
                    print('-x Não contêm informações. x-')
                    novo_marca = input('Digite novamente: ')
                    print('=-' * 25)

                novo_nv = input('Atualizar Estado de uso (NOVO ou USADO): ')
                print('=-' * 25)

                while (novo_nv != 'novo' and novo_nv != 'usado'):
                    novo_nv = input('-x Por favor, digite só se é NOVO ou USADO: ')
                    print('=-' * 25)

                novo_descr = input('Atualizar Descrição do Produto: ')
                print('=-' * 25)

                while (novo_descr.isspace() == True or novo_descr == ''):
                    print('-x Não contêm informações. x-')
                    novo_descr = input('Digite novamente: ')
                    print('=-' * 25)

                novo_preco = input('Atualizar Preço do Produto: ')
                print('=-' * 25)

                while (novo_preco.isspace() == True or novo_preco == ''):
                    print('-x Não contêm informações. x-')
                    novo_preco = input('Digite novamente: ')
                    print('=-' * 25)

                novo_qntd = input('Atualizar Quantidade do produto: ')
                print('=-' * 25)

                while (novo_qntd.isspace() == True or novo_qntd == ''):
                    print('-x Não contêm informações. x-')
                    novo_qntd = input('Digite novamente: ')
                    print('=-' * 25)

                novo = {}
                novo[atualizar] = [novo_marca, novo_nv, novo_descr, novo_preco, novo_qntd]
                produto_vendedor.update(novo)
                print('Produto atualizado.')
                print('=-' * 25)
                break

            elif(op_login_vendedor == 6):
                for z, x in produto_vendedor.items():
                    print(f'Codigo: {z}\nNome do produto: {x[0]}\nMarca do produto: {x[1]}\nEstado: {x[2]}\nDescrição: {x[3]}\nPreço: {x[4]}\nQuantidade: {x[5]}')
                    print('=-' * 25)
                if(produto_vendedor == {} or produto_vendedor == { }):
                    print('Produtos indisponíveis.')
                    print('=-' * 25)