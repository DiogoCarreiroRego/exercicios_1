"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""


if __name__ == '__main__':
    vendas_grupo_central = []
    nomes_ilhas_grupo_central = []
    soma = 0

    for x in range(0, 5):
        num = int(input(f'Qual é o número de vendas? '))
        #nome = str(input(f'Qual é o nome da ilha? '))

        soma = soma + num

        vendas_grupo_central.insert(x, num)
        #nomes_ilhas_grupo_central.insert(x, nome)

    for x in vendas_grupo_central:
        print(x, end=' ')
    print('')
    #for x in nomes_ilhas_grupo_central:
        #print(x, end=' ')

    print(soma)
    #venda(num)

