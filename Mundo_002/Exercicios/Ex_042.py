# Refaça o desafio Ex_035.py dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
# (( Aula_012 ))

lado1 = float(input('Digite o comprimento do primeiro lado do triângulo: '))
lado2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
lado3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))    

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados informados PODEM formar um triângulo.')
    if lado1 == lado2 == lado3:
        print('O triângulo formado é do tipo EQUILÁTERO.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo formado é do tipo ISÓSCELES.')
    else:
        print('O triângulo formado é do tipo ESCALENO.')