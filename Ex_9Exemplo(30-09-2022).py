#pessoa = {1, 'Maria', {'morada': 'Rua de Cima, 1', 'cp': 9533}, 12.56, [123, 434, 3434, 334.3]}

meses = {'Janeiro', 'Fevereiro', 'Março'}


if __name__ == '__main__':
    # Não funcionando
    """print(pessoa[2].keys())
    print(pessoa[2].values())
    print()
    for x in pessoa[2].keys():
        print(x)
    for v in pessoa[2].values():
        print(v)
    print()
    for k in pessoa[2].keys():
        print(f'{k} = {pessoa[2][k]}')"""

    meses.add('Abril')
    print(meses)
    meses.pop()
    print(meses)
