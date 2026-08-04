# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Número 6.127, a parte inteira é 6
# ((Aula 08))

import math

num = float(input('Informe o número: '))

# Utilizando import
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))

# Utilizando função interna
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, int(num)))