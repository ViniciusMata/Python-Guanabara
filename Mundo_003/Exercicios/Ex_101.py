# Crie um programa que tenha uma função chamda voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor 
# literal indicado se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
# (( Aula_021 ))

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))