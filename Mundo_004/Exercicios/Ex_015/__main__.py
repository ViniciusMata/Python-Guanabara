# Crie uma classe que gerencia a hash SHA256 de uma senha
#   name:       Credencial
#   atributos:  @senha          (+)
#   atributos:  __hash          (-)
#   metodos:    validar(chave)  (+)

from Credencial import Credencial

def main():

    c = Credencial()
    c.senha = input("Digite a sua senha: ")
    print(c.senha)
    c.validar('CeV!@')

if __name__ == "__main__":
    main()