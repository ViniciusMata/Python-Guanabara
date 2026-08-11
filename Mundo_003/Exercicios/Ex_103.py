# Faça um program que tenha uma funcao chamada ficha(), que receba dois parametro opcionais: o nome de um jogagdor e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogoadr, mesmo que algum dado nºao tenha sido informado corretamente.
# (( Aula_021 ))

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)