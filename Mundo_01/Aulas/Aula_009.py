frase = ' Curso em Vídeo de Python '

print(frase)

# Fateamento ( pega posição especifica )
print(frase[3])

# Fateamento ( pega da posição especifica indicada "inicio" e "fim" )
print(frase[3:13])

# Fateamento ( pega posição especifica do inicio ate posicao indicada "fim" )
print(frase[0:13])

# Fateamento ( pega posição especifica do inicio ate posicao indicada "fim" saltando entre 2 )
print(frase[0:15:2])

# Conta qtd de caracteres passado no parametro
print(frase.count('o'))

# Conta qtd de caracteres passado no parametro
print(frase.upper().count('O'))

# Conta qte total de caracteres
print(len(frase))

# Remover "espaços" em branco do inicio ou final
print(len(frase.strip()))

# Substituir algo
print(frase.replace('Python', 'Java'))

# Verifica se parametro existe, retornando True ou False
print('Curso' in frase)

# Retorna a posição do elemento ( caso negativo, retorna -1 )
print(frase.find('o'))

# Retorna a posição do elemento pesquisando do final para o inicio ( caso negativo, retorna -1 )
print(frase.rfind('a'))

# Transforma em maiuscula
print(frase.upper())

# Transforma em minuscula
print(frase.lower())

# Divide a string em listas
print(frase.split())

# Exibe o conteundo da lista pela ordem indicada
dividido = frase.split()
print(dividido[0])

# Com opção de fateamento
print(dividido[0][0:3])