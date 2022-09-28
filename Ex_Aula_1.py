"""
1º Exercicio

"""


if __name__ == '__main__':
    num1_list = []
    num2_list = []

    for x in range(1, 4):
        num1_list.append(int(input('Digite os primeiros números: ')))
        if x == 3:
            for y in range(1, 4):
                num2_list.append(int(input('Digite os segundos números: ')))

    a = 0
    for x in num1_list:
        if x == num2_list[a]:
            print(f'{x} é igual a {num2_list[a]}')
        if x < num2_list[a]:
            print(f'{x} é menor que {num2_list[a]}')
        if x > num2_list[a]:
            print(f'{x} é maior que {num2_list[a]}')
        a += 1
