# Tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # Criando uma tupla com elementos
print(lanche[1])  # Acessando o elemento na posição 1   

print(lanche[3])  # Acessando o elemento na posição 3

print(lanche[-2])  # Acessando o elemento na posição -2

print(lanche[1:3])  # Acessando o elemento na posição 1 até 2

print(lanche[2:])  # Acessando o elemento na posição 2 até final

print(lanche[:2])  # Acessando o elemento do início até a posição 2


# Tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação.
# lanche[1] = 'Refrigerante'  # Isso vai gerar um erro, pois não é possível alterar elementos de uma tupla.

print(len(lanche))  # Mostrando o tamanho da tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')  # Iterando sobre os elementos da tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  # Iterando sobre os elementos da tupla

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')  # Iterando sobre os elementos da tupla

print(sorted(lanche))  # Mostrando os elementos da tupla em ordem alfabética


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Concatenando tuplas
print(c)  # Mostrando a tupla concatenada
print(c.count(5))  # Contando quantas vezes o elemento 5 aparece na tupla
print(c.index(8))  # Mostrando a posição do elemento 8 na tupla


pessoa = ('Vinicius', 32, 'M', 120)  # Criando uma tupla com diferentes tipos de elementos
del(pessoa)  # Deletando a tupla
print(pessoa)