# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# (( Aula_017 ))

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'Valores digitados: {valores}')
print(f'Maior valor: {max(valores)} na posição {valores.index(max(valores))}')
print(f'Menor valor: {min(valores)} na posição {valores.index(min(valores))}')