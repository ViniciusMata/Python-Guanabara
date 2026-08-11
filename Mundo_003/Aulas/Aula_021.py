def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Vinicius Mata
    """

    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(3, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

print()
print('*' * 50)
print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É PAR')
else:
    print('É ÍMPAR')