# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.
# (( Aula_013 ))

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulhermenor20 = 0

for p in range(1, 5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    somaidade += idade

    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulhermenor20 += 1

mediaidade = somaidade / 4

print('----- FIM DO PROGRAMA -----')
print(f'A média de idade do grupo é {mediaidade:.1f} anos.')
if nomevelho:
    print(f'O homem mais velho é {nomevelho} com {maioridadehomem} anos.')
else:
    print('Não houve homem cadastrado.')
print(f'Total de mulheres com menos de 20 anos: {totmulhermenor20}.')
