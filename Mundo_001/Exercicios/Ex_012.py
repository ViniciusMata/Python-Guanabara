# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
# ((Aula 07))

preco = float(input('Informe o preço do produto: R$'))

print('O valor do produto com desconto de 5% é {:.2f}'.format(preco - (preco * 0.05)))