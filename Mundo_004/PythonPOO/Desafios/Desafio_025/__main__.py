# Crie classes capazes de calcular fretes de veiculos diferentes:
#
#   name:       Transporte {abstract}
#   atributos:  distancia
#   atributos:  frete
#   metodos:    calc_frete() {abstract}
#
#   name:       Moto
#   atributos:  fator = 0.50
#   metodos:    calc_frete()
#
#   name:       Caminhao
#   atributos:  fator = 1.20
#   metodos:    calc_frete()
#
#   name:       Drone
#   atributos:  fator = 9.50
#   metodos:    calc_frete()

from rich import print, inspect
from rich.table import Table
from Transportes import *

def main():

    distancia = 80

    """
    entrega = Drone(distancia)
    print(f"Frete de {type(entrega).__name__} em {distancia}km = {entrega.calc_frete()}")
    """
    
    viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]
    
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    
    for item in viagem:
        tabela.add_row(f"{distancia}Km", f"{type(item).__name__}", f"{item.calc_frete()}")
    
    print(tabela)
    
if __name__ == "__main__":
    main()