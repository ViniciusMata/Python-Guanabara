# Aprimore o exercicio da ContaBancaria, aplicando conceitos de encapsulamento
#   name:       ContaBancaria
#   atributos:  _id                     (#)
#   atributos:  _titular                (#)
#   atributos:  __saldo                 (-)
#   atributos:  __hash                  (-)
#   atributos:  @nome                   (+)
#   atributos:  @validar_senha(chave)   (+)
#   atributos:  @pede_senha()           (+)
#   atributos:  @sacar(valor, chave)    (+)
#   atributos:  @depositar(valor)       (+)
from ContaBancaria import ContaBancaria

def main():
    cc = ContaBancaria(111, "Josenildo", 10000)

    print("Vou tentar sacar...")
    cc.sacar(500)

    print("Vou tentar mudar nome...")
    cc.nome = "Maricota"

    print(cc)

if __name__ == "__main__":
    main()