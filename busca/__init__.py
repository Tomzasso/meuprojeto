def buscar(produto:dict, busca):
    achou = False
    for cod, info in produto.items():
        if (str(info).find(busca) >= 0):
            print(
                f'Código: {cod}'
                f'Nome do produto: {info[0]}\n'
                f'Marca do produto: {info[1]}\n'
                f'Estado de uso: {info[2]}\n'
                f'Descrição do Produto: {info[3]}\n'
                f'Preço: {info[4]}\n'
                f'Quantidade(s): {info[5]}')
            print('=-' * 25)
            achou = True
            break

    while(achou == False):
        print('-x Produto não encontrado. x-')
        print('=-' * 25)
        busca = input('Digite novamente: ')
        for cod, info in produto.items():
            if (str(info).find(busca) >= 0):
                print(
                    f'Código: {cod}'
                    f'Nome do produto: {info[0]}\n'
                    f'Marca do produto: {info[1]}\n'
                    f'Estado de uso: {info[2]}\n'
                    f'Descrição do Produto: {info[3]}\n'
                    f'Preço: {info[4]}\n'
                    f'Quantidade(s): {info[5]}')
                print('=-' * 25)
                achou = True
                break
