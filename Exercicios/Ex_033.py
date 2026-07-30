# Faça um program que leia três números e mostre qual é o maior e qual é o menor.
# ((Aula 10))

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print ('O maior número digitado foi {}'.format(maior))