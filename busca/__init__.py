def buscar(produto:dict, busca):
    achou = False
    for r in produto:
        if (str(r).find(busca) >= 0):
            print(
                f'Código: {produto[r][5]}'
                f'Nome do produto: {r}\n'
                f'Marca do produto: {produto[r][0]}\n'
                f'Estado de uso: {produto[r][1]}\n'
                f'Descrição do Produto: {produto[r][2]}\n'
                f'Preço: {produto[r][3]}\n'
                f'Quantidade(s): {produto[r][4]}')
            print('=-' * 25)
            achou = True
            break

    if (achou == False):
        print('-x Produto não encontrado. x-')
        print('=-' * 25)
