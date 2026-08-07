teste = list()

teste.append('Vinicius')
teste.append(32)

galera = list()
galera.append(teste[:])

teste[0] = 'João'
teste[1] = 22

galera.append(teste[:])

print(galera)


galera = [['Vinicius', 32], ['João', 22], ['Maria', 19], ['Ana', 33]]
print(galera[0][0])  # Acessando o nome da primeira pessoa


galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')