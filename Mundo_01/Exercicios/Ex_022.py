# Crie um programa que leia o nome completo de uma pessoe e mostre:
# O nome com todas as letras maiusculas
# O nome com todos as letras minusculas
# Quantas letaras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome:
# ((Aula 09))

nome = str(input('Qual o seu nome: '))

print(nome.upper())

print(nome.lower())

print(len(nome.strip()))

dividido = nome.split()
print(dividido[0])