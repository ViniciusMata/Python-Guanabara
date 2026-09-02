# Implemente o seguite diagrama de classes:
#
#   name:       Poligono {abstract}
#   atributos:  qtd_lados
#   metodos:    perimetro() {abstract}
#   metodos:    area() {abstract}
#
#   name:       Quadrado
#   atributos:  lado
#   metodos:    perimetro()
#   metodos:    area()
#
#   name:       Circulo
#   atributos:  raio
#   metodos:    perimetro()
#   metodos:    area()

from rich import print, inspect
from Poligono import *


def main():

    q = Quadrado(20)
    print(f"Um quadrado de lado {q.lado}cm tem perímetro de {q.perimetro():.1f}cm")
    print(f"Um quadrado de lado {q.lado}cm tem área de {q.area():.1f}cm²")
    
    c = Circulo(10)
    print(f"Um círculo de raio {c.raio}cm tem perímetro de {c.perimetro():.1f}cm")
    print(f"Um círculo de raio {c.raio}cm tem área de {c.area():.1f}cm²")

if __name__ == "__main__":
    main()