# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# (( Aula_013 ))

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Os números gerados foram: {numeros}')
print(f'O maior valor é: {max(numeros)}')
print(f'O menor valor é: {min(numeros)}')
