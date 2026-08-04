# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# ((Aula 10))

from random import randint

numero_pc = randint(0, 5)

numero_user = int(input('Digite um número entre 0 e 5: '))

if(numero_user == numero_pc):
    print('Parabéns! Você acertou o número que o computador pensou, que era {}'.format(numero_pc))
else:
    print('Você errou! O número que o computador pensou era {}'.format(numero_pc))