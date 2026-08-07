# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considera US$ 1,00 = R$ 3,27
# ((Aula 07))

real = float(input('Informe a quantia disponível na carteira? R$'))

cotacao = 3.27

dolar = real / cotacao

print('Com R${:.2f}, pode comprar US${:.2f} sendo a cotação à {}'.format(real, dolar, cotacao))