# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
# (( Aula_013 ))

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 
         'Chapecoense', 'Atlético-MG', 'Fluminense', 'Bahia', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí', 'Vitória')

print('Os 5 primeiros colocados são:')
for i in range(5):
    print(f'{i+1}º - {times[i]}')

print('\nOs últimos 4 colocados são:')
for i in range(16, 20):
    print(f'{i+1}º - {times[i]}')

print('\nTimes em ordem alfabética:')
for time in sorted(times):
    print(time)

print(f'\nO time da Chapecoense está na {times.index("Chapecoense")+1}ª posição.')