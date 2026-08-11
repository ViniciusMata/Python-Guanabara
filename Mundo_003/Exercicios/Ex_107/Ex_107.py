import Moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${Moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${Moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R${Moeda.aumentar(preco, 10)}')
