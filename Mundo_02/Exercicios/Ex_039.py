# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# (( Aula_012 ))

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {date.today().year}.')

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'O alistamento será em {date.today().year + (18 - idade)}.')
elif idade == 18:
    print('É hora de se alistar!')
else:
    print(f'Já passou {idade - 18} anos do tempo do alistamento.')
    print(f'O alistamento foi em {date.today().year - (idade - 18)}.')