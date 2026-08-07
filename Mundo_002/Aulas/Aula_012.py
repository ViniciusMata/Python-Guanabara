nome = str(input('Digite seu nome: '))

if nome == 'Vinicius':
    print('Que nome bonito você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular.')
elif nome in 'Ana, Julia, Bianca':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))