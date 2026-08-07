# Faça um programa que ajude um jodar da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta.
# (( Aula_018 ))

from random import randint
from time import sleep

lista = []
jogos = []

qtd = int(input('Quantos jogos você quer que seja sorteado? '))
total = 0

while total < qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3 + f' SORTEANDO {qtd} JOGOS ' + '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)