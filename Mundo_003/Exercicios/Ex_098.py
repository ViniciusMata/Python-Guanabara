# Faça um programa que tenha uma função chamda contador(), que receba três parâmetro: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar 3 contagens atraves da função criada.
# A) de 1 até 10, de 1 em 1
# B) de 10 ate 0, de 2 em 2
# C) uma contagem personalizada
# (( Aula_020 ))

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print('FIM')

# Programa principal
contador(1, 10, 1)
contador(10, 1, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)