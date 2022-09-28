"""
2º Exercicio

"""


def comfor(num1, num2):
    total = 0
    for x in range(num1, num2 + 1):
        total += x

    return total


def comwhile(num1, num2):
    total = 0
    while num1 < num2:
        total += num1
        num1 += 1
        if num1 == num2:
            break

    return total


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))

            if num2 < num1:
                print('O segundo tem de ser maior que o primeiro número.')

            opcao = int(input('Qual opcão deseja [For - 1 ou While- 2]? '))

            if opcao == 1:
                print(f'Total = {comfor(num1, num2)}')
            if opcao == 2:
                num2 += 1
                print(f'Total = {comwhile(num1, num2)}')

            continuar = input('Deseja continuar (n or s? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor inteiro!')
