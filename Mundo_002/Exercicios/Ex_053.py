# Cria um programa que leia uma frase qualquer e diga se eça é um palíndromo, desconsiderando os espaços.
# (( Aula_013 ))

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')  
