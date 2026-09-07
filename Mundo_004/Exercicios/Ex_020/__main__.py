# Crie um simulador que gerencia a abertura de diferentes tipos de arquivos
#
#   name:       Arquivo {abstract}
#   atributos:  nome            (+)
#   atributos:  _extensao       (#)
#   atributos:  tamanho         (+)
#   atributos:  @nome_completo  (+)
#   metood:     @abrir
#
#   name:       PDF
#
#   name:       DOC

from classes import *

def main():

    a1 = DOC("Teste", 1_200_000)
    abrir_arquivo(a1)

    a2 = PDF("Contrato", 850_000)
    abrir_arquivo(a2)

if __name__ == "__main__":
    main()