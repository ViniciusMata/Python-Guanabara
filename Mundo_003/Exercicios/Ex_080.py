# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.
# (( Aula_017 ))

valores = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Valores digitados (em ordem crescente): {valores}')