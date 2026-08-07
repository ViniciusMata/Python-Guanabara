# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# (( Aula_013 ))

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(0, 10):
    print('{} -> '.format(termo), end='')
    termo += razao

print('FIM')