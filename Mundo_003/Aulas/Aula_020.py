def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

soma(b=4, a=5)
soma(7, 2)

print()
print('*' * 40)
print()

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')


contador(8, 0)
contador(2, 1, 7)

print()
print('*' * 40)
print()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


print()
print('*' * 40)
print()

def somar1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

somar1(5, 2)
somar1(2, 9, 4)