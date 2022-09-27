"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido assim como as respetivas ilhas
- O maior valor inserido assim como as respetivas ilhas
- A média das vendas
"""


if __name__ == '__main__':
    vendas = []
    ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']

    for ilha in ilhas:
        vendas.append(int(input(f'Insira as vendas para {ilha} ')))

    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)

    print(f'Vendas = {vendas}')
    print(f'Total de vendas = {total_vendas}')
    print(f'Média de vendas = {media_vendas}')

    menor_num = 0
    maior_num = 0
    comp = 0
    for x in range(0, len(vendas)):
        if x <= menor_num:
            menor_num = vendas[x]
        if x > maior_num:
            maior_num = vendas[x]

        #print(f'Menor vendas = {menor_num} da ilha {ilhas[comp]}')
        print(f'Maior venda = {maior_num}')
        comp += 1



