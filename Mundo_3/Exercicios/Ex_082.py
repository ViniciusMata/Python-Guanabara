# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
# (( Aula_017 ))

valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

pares = []
ímpares = []

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)

print(f'Valores digitados: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores ímpares: {ímpares}')