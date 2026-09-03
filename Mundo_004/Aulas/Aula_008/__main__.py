from rich import print, inspect
from classes import Pessoa, Aluno, Professor, Funcionario 

def main():
    a1 = Aluno("José", 17, "Informática", "T01")
    a1.fazer_Aniversario()
    a1.fazerMatricula()
    a1.estudar()
    #inspect(a1, methods=True)

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.fazer_Aniversario()
    p1.dar_aula()
    p1.estudar()
    #inspect(p1, methods=True)

    f1 = Funcionario("Cláudia", 27, "Secretaria", "Secretaria")
    f1.fazer_Aniversario()
    f1.bater_ponto()
    f1.estudar()
    #inspect(f1, methods=True)
    
if __name__ == "__main__":
    main()