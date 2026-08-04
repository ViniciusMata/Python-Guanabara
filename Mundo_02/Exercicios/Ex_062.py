# Melhore o Ex_061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# (( Aula_014 ))

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while True:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
    if cont > 10:
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        if mais == 0:
            break
        cont = 1
        while cont <= mais:
            print(f'{termo} → ', end='')
            termo += razao
            cont += 1