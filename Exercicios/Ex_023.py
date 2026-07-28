# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Exemplo Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
# ((Aula 09))

numero = input('Digite um número entre 0 a 9999: ')

print('Unidade:', numero[len(numero)-1])

print('Dezena:', numero[len(numero)-2])

print('Centena:', numero[len(numero)-3])

print('Milhar:', numero[len(numero)-4])