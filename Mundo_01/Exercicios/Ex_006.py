# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# ((Aula 07))

num = int(input('Informe o número: '))

print('Número escolhido foi {}, seu dobro é {}, o tríplo é {} e a raiz quadrada é {:.2f}'.format(num, num * 2, num * 3, pow(num, (1/2))))