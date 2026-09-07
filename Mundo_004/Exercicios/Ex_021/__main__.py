# Crie um simulador que gerencia o pagamento em diferentes tipos
#
#   name:       Pagamento {abstract}
#   atributos:  valor           (#)
#   atributos:  @fvalorao       (+)
#   metood:     pagar()
#
#   name:       Boleto
#
#   name:       PIX
#
#   name:       Crédito

from classes import *

def main():

    p1 = Pix()
    finalizar_Compra(Pix(), 1500)
    finalizar_Compra(CartaoCredito(), 9540.84)
    finalizar_Compra(Boleto(), 439.23)

if __name__ == "__main__":
    main()