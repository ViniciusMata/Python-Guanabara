# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
# # (( Aula_023 ))

from lib.interface import *
from lib.arquivo import *
from time import sleep
#import os

# caminho do arquivo de dados (sempre relativo ao próprio script)
#arq = os.path.join(os.path.dirname(__file__), 'cursoemvideo.txt')

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar nova pessoa
        cabecalho('NOVO CADASTRADO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)