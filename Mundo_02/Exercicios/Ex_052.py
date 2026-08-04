# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# (( Aula_013 ))

n = int(input('Digite um número: '))

tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')