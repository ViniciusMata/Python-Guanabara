# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# (( Aula_012 ))

valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite em quantos anos você vai pagar: '))

prestacao_mensal = valor_casa / (anos * 12)
limite_prestacao = salario * 0.3

if prestacao_mensal <= limite_prestacao:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')