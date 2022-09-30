"""
* BI
* NOME
* MORADA
* CÓDIGO POSTAL
* CUSTO HORA
* ANO DE NASCIMENTO

- Apresentar a informação individual de cada utilizador
"""


if __name__ == '__main__':
    dictionary = {}
    for a in range(2):
        dictionary = {
            'BI': int(input('BI - ')),
            'Nome': input('Nome - '),
            'Morada': input('Morada - '),
            'Codigo Postal': int(input('Código Postal - ')),
            'Custo Hora': float(input('Custo Hora - ')),
            'Ano de Nascimento': input('Ano de Nascimento - ')
        }

    for x in dictionary:
        print(f'{x} - {dictionary[x]}')

    print(dictionary)
    #print(len(dictionary))
