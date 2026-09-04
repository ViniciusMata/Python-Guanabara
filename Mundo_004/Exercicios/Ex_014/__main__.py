# Simule um diário secreto orientado a objeto
#   name:       Diario
#   atributos:  __segredos[]    (-)
#   atributos:  __senha         (-)
#   metodos:    escrever(msg)   (+)
#   metodos:    ler(senha)      (+)

from Diario import Diario
from rich import print, inspect

def main():
    meuDiario = Diario()
    meuDiario.escrever("Essa é a primeira mensagem")
    meuDiario.escrever("Estou aprendendo Python")
    try:
        meuDiario.ler('CeV!@')
    except Exception as e:
        print(f"[red]ERRO: {e}[/]")
    #inspect(meuDiario, private=True)

if __name__ == "__main__":
    main()