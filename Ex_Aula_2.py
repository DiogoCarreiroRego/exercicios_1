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
    while x in range(num1, num2):
        return x


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

        except ValueError:
            print('Digite um valor inteiro!')

