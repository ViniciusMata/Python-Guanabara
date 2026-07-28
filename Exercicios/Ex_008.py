# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# ((Aula 07))

metros = float(input('Informe a distância em metros: '))

print('Valor: Metros {}m, corresponde a {:.0f}cm, e {:.0f}mm'.format(metros, metros * 100, metros * 1000))