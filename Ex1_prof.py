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


vendas = []
ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']


def declarar_lista(casas):
  for x in range(casas):
    vendas.append(0)
  return vendas


if __name__ == '__main__':
  declarar_lista(5)

  for ilha in ilhas:
    vendas.append(float(input(f'Insira as vendas para {ilha} ')))

  x = 0
  while x < len(ilhas):
    vendas.append(float(input(f'Insira as vendas para {ilhas[x]} ')))
    x += 1

  print(f'Vendas = {vendas}')
