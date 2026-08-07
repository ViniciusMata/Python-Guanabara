# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# A Sequência de Fibonacci é a seguinte: 0 → 1 → 1 → 2 → 3 → 5 → 8 → 13 → ...
# (( Aula_014 ))

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2}', end='')
t3 = t1 + t2
while t3 <= n:
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print(' → FIM')