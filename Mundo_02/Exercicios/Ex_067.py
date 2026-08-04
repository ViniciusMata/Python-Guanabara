# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
# (( Aula_015 ))

while True:
    n = int(input('Digite um número para ver sua tabuada [Número negativo para parar]: '))
    if n < 0:
        break
    print(f'----- Tabuada do {n} -----')
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('--------------------------')