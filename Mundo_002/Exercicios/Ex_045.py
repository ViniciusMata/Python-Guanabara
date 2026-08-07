# Crie um programa que faça o computador jogar Jokenpô com você.
# (( Aula_012 ))

import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
print('Vamos jogar Jokenpô!')
jogador = input('Escolha sua jogada (Pedra, Papel ou Tesoura): ').capitalize()
computador = random.choice(opcoes)

print(f'Você escolheu: {jogador}')
print(f'O computador escolheu: {computador}') 

if jogador == computador:
    print('Empate!')
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você venceu!')
else:
    print('O computador venceu!')