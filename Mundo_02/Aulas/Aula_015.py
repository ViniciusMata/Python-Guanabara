n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados é {s}.')

nome = 'Vinicius'
idade = 32
salario = 920.00

print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}.')