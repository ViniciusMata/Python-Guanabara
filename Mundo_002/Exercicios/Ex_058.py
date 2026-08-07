# Melhore o jogo do Ex_028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# (( Aula_014 ))

from random import randint

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite um número entre 0 e 10: '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')

print(f'Acertou! O número era {computador}.')
print(f'Você precisou de {palpites} palpites para vencer.')