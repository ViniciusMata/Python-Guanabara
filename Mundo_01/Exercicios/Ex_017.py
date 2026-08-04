# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo e 
# calcule e mostre o comprimento da hipotenusa
# ((Aula 08))

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# Utilizando import
hi1 = hypot(co, ca)

# Utilizando função interna
hi2 = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi1))
print('A hipotenusa vai medir {:.2f}'.format(hi2))