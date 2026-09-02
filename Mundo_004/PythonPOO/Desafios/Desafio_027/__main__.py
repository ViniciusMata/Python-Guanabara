# Simule o sistema de batalha entre personagens de um RPG:
#
#   name:       Personagem {abstract}
#   atributos:  nome
#   atributos:  vida
#   atributos:  golpes
#   metodos:    atacar(alvo, forca)
#   metodos:    receber_dano(dano)
#   metodos:    curar() {abstract}
#
#   name:       Guerreiro
#   metodos:    curar()
#
#   name:       Mago
#   metodos:    curar()

from rich import print, inspect
from Personagem import *

def main():

    p1 = Guerreiro("Pikachu", 1000)
    p2 = Mago("Charmander", 1000)
    
    p1.atacar(p2, 200)
    p2.atacar(p1, 200)
    
    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()