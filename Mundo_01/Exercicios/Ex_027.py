# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente
# ((Aula 09))

nome = input('Digite seu nome: ')

nomeDividido = nome.split()

print('Primeiro:', nomeDividido[0])

qtd = len(nomeDividido)
print('Último:', nomeDividido[qtd -1])