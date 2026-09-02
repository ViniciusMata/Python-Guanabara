# Simule uma cafeteria orientada a objetos:
#
#   name:       BebidaQuente {abstract}
#   atributos:  preparar()
#   atributos:  ferver_agua()
#   metodos:    misturar() {abstract}
#   metodos:    servir() {abstract}
#
#   name:       Cafe
#   atributos:  
#   metodos:    misturar()
#   metodos:    servir()
#
#   name:       Cha
#   atributos:  
#   metodos:    misturar()
#   metodos:    servir()
#
#   name:       Leite
#   atributos:  
#   metodos:    misturar()
#   metodos:    servir()

from rich import print, inspect
from Cafeteria import *

def main():

    b1 = Cafe()
    b2 = Cha()
    b3 = Leite()
    
    b1.preparar()
    b2.preparar()
    b3.preparar()

if __name__ == "__main__":
    main()