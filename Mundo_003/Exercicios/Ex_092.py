# Crie um programa que leia nome, ano de nascimneot, e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO
# O dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# (( Aula_019 ))

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))

dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salaraio'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

for k,v in dados.items():
    print(f' - {k} tem o valor {v}')