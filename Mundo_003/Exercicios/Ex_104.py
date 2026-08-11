# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a funcao input() do Python, só que fazendo a validacao 
# para aceitar apenas valores numericos
# Ex: n = leiaInt('Digite um n' )
# (( Aula_021 ))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m]')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')