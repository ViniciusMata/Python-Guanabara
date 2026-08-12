# Reescreva a função leiaInt() que fizemos no Ex_104.py, incluindo agora a possibildiade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# (( Aula_023 ))

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
        
num1 = leiaInt('Digite um Inteiro: ')
num2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}.')