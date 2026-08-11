# Faça um programa que tenha uma função chamda escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: 
# Entrada = escreva('Olá, Mundo!')
# Saida = **** Olá, Mundo ****
# (( Aula_020 ))

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)

# Programa principal
escreva('Vinícius Lourenço da Mata')
escreva('Cruso em Vídeo - Python')
escreva('Python')
