# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
# (( Aula_012 ))

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria JÚNIOR.')
elif idade == 20:
    print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')