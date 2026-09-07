# Crie a seguinte estrutura de classes para calcular bônus salarial
#
#   name:       Funcionario {abstract}
#   atributos:  nome            (+)
#   atributos:  _salario        (-)
#   metood:     @calcular_bonus
#
#   name:       Gerente
#
#   name:       Designer
#
#   name:       Desenvolvedor

from classes import *

def main():

    funcionarios = [
        Desenvolvedor("Pedro", 18_000),
        Designer("José", 25_000),
        Gerente("Mariana", 45_000)
    ]

    for f in funcionarios:
        print(f)

if __name__ == "__main__":
    main()