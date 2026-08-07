# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
# (( Aula_017 ))

valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Quantidade de números digitados: {len(valores)}')
valores.sort(reverse=True)
print(f'Lista de valores ordenada de forma decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')