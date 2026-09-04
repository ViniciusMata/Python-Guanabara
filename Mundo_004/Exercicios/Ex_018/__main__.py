# Implemente a seguinte estrutura de diagrama de classes.
#
#   name:       Pessoa {abstract}
#   atributos:  _nome            (#)
#   atributos:  _nascimento      (#)
#   atributos:  @nascimento      (+)
#   atributos:  @idade           (+)
#
#
#   name:       Aluno
#   atributos:  cursos_oficiais  (+)
#   atributos:  _curso           (#)
#   atributos:  @curso           (+)
#   métodos:    add_curso(cruso) (+)

from Pessoa import *

def main():
    a = Aluno("Marcia", 2010, "ADS")
    b = Aluno("Pedro", 2015, "ENG")

    a.add_curso("MODA")

    print(a.cursos_oficiais)
    print(a.__dict__)

if __name__ == "__main__":
    main()