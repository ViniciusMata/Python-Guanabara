# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
# ((Aula 10))

distancia = float(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da passagem é de R${:.2f}'.format(preco))   