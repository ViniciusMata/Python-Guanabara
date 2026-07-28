# Crie um programa que leia o nome de uma cidade e diga se começa com o nome "SANTO"
# ((Aula 09))

cidade = input('Qual o nome da cidade: ').strip()

print(cidade[:5].upper() == 'SANTO')