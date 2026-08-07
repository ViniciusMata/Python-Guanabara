# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# (( Aula_017 ))

valores = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')

valores.sort()
print(f'Valores digitados (em ordem crescente): {valores}')