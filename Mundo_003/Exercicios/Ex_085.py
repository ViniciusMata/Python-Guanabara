# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lsita única
# Que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente
# (( Aula_018 ))

num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os valores pares são {num[0]}')
print(f'Os valores ímpares são {num[1]}')
