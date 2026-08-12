# Crie um código em Python que teste se o site Pudim acessível pelo computador usado.
# (( Aula_023 ))

import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br', timeout=5)
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')