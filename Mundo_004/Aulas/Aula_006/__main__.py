from rich import print, inspect
from classes import Aluno, Professor, Funcionario 

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_Aniversario()
a1.fazerMatricula()
inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_Aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Cláudia", 27, "Secretaria", "Secretaria")
f1.fazer_Aniversario()
f1.bater_ponto()
inspect(f1, methods=True)