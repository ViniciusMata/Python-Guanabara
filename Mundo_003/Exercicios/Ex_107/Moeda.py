# Crie um módulo chamado moeda.py que tenha funções incorporadoas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções
# (( Aula_022 ))

def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res
    
def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res
    
def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco / 2
    return res