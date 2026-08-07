# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se 
# ele quer ou não continuar a digitar valores.
# (( Aula_014 ))

soma = 0
cont = 0
maior = 0
menor = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

media = soma / cont
print(f'A média dos valores é {media:.2f}')
print(f'O maior valor é {maior} e o menor valor é {menor}')