# Crie a estrutura capaz de calcular salários de funcionários diferentes:
#
#   name:       Funcionario {abstract}
#   atributos:  nome
#   atributos:  sal_bruto
#   atributos:  salario
#   atributos:  sal_min = 1612
#   atributos:  inss = 7.5
#   metodos:    calc_sal() {abstract}
#   metodos:    analisar_sal()
#
#   name:       Horista
#   atributos:  valor_hora
#   atributos:  horas_trab
#   metodos:    calc_sal()
#
#   name:       Mensalista
#   metodos:    calc_sal()

from rich import print, inspect
from Funcionario import *

def main():

    f1 = FuncionarioMensalista("José da Silva", 8500)
    f1.calcular_salario()
    f1.analisar_salario()
    
    f2 = FuncionarioHorista("Maria de Souza", 25, 250)
    f2.calcular_salario()
    f2.analisar_salario()
    
    #inspect(f1)

if __name__ == "__main__":
    main()