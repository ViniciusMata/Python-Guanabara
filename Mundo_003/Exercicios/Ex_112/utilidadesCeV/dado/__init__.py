# Dentro do pacote utilidadesCeV que criamos no Ex_111.py, temos um módulo chamado dado. Cire uma função chamda leiaDinheiro() que seja capaz
# de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
# (( Aula_022 ))

def leiaDinheiro(msg):
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
        

def leiaInt(msg):
    """_summary_

    Args:
        msg (_type_): _description_

    Returns:
        _type_: _description_
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m]')
        if ok:
            break
    return valor