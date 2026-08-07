# Listas são mutáveis
num = [2, 5, 9, 1]
num[2] = 3  # Altera o valor do índice 2 para 3
num.append(7)   # Adiciona o valor 7 no final da lista no final
num.sort(reverse=True) # Ordena DESC
num.insert(2, 0) # Insere o valor 0 no índice 2
if 4 in num:
    num.remove(2) # Remove o valor 2 da lista
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = []
valores.append(5)
valores.append(9)
valores.append(2)
valores.append(3)
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print('Cheguei ao final da lista.')


a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')