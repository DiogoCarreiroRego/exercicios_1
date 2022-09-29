"""
a

"""

if __name__ == '__main__':
    ilhas = ['TER', 'PIC', 'FAI', 'GRA', 'SJR']
    tipos = ['Gasolina', 'Gasoleo']

    vendas = [
        [0, 0, 0, 0, 0],     # 0   Gasolina
        [0, 0, 0, 0, 0]      # 1   Gasoleo
    ]

    while True:
        try:
            for x in range(len(tipos)):
                for y in range(len(ilhas)):
                    vendas[x][y] = int(input(f'Qual foi o número de vendas na {ilhas[y]} do tipo {tipos[x]}? '))
            print(f'\n{vendas}')

            total = 0
            for x in range(len(tipos)):
                total_tipo = 0
                for y in range(len(ilhas)):
                    total_tipo += vendas[x][y]
                print(f'Total de {tipos[x]} = {total_tipo}')

            for y in range(len(ilhas)):
                total_ilhas = 0
                for x in range(len(tipos)):
                    total += vendas[x][y]
                    total_ilhas += vendas[x][y]
                print(f'Total na {ilhas[y]} = {total_ilhas}')
            print(f'Total = {total}')
            break

        except ValueError:
            print('Insire um valor válido para vendas.')
