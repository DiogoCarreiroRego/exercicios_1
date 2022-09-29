"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha

Exemplo da estrutura de armazenamento das vendas:

    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]

    ou então:

    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]


"""

if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50], # 0
        [15, 25, 35, 45, 55]  # 1
    ]

    print(vendas)
    for x in vendas:
        print(x)
        for y in x:
            print(y)

    x = 0
    y = 4
    print(f'Vendas[0][0] = {vendas[x][y]}')

    """for x in range(2):
        for y in range(5):
            print(f'{[x]}{[y]} {vendas[x][y]}')"""

    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'{[x]}{[y]} {vendas[x][y]}')

    print(f'a = {len(vendas)}')
    print(f'b = {len(vendas[0])}')

    # Total de vendas
    """total = 0
    for x in range(len(vendas)):
        total_linhas = 0
        for y in range(len(vendas[0])):
            print(f'{[x]}{[y]} {vendas[x][y]}')
            total += vendas[x][y]
            total_linhas += vendas[x][y]
        print(f'Total de linhas {total_linhas}')
    print(f'Total de vendas {total}')"""

    # Soma por ilha, Incompleto
    """total_ilha = 0
    for y in range(len(vendas[0])):
        a = 0
        for x in range(len(vendas)):
            total_ilha += vendas[x][a]
            a += 1
        print(f'{total_ilha}')"""

    # Soma por ilh, Completo
    print('')
    total = 0
    for y in range(len(vendas[0])):
        total_ilhas = 0
        for x in range(len(vendas)):
            print(f'{[x]}{[y]} = {vendas[x][y]}')
            total += vendas[x][y]
            total_ilhas += vendas[x][y]
        print(f'Total por ilha = {total_ilhas}')
    print(f'Total = {total}')