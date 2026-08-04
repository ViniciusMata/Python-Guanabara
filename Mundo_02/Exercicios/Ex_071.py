# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# (( Aula_015 ))

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor

cedulas = [50, 20, 10, 1]
for cedula in cedulas:
    if total >= cedula:
        qtd_cedulas = total // cedula
        total -= qtd_cedulas * cedula
        print(f'Total de {qtd_cedulas} cédulas de R$ {cedula}')

