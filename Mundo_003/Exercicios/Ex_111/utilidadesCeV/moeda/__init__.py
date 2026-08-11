# Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
# Transfira todo as funcoes utilizadas nos Ex_107.py, Ex_108.py, Ex_109.py e Ex_110.py para o primeiro pacote e mantenha tudo funcionando
# (( Aula_022 ))

def aumentar(preco = 0, taxa = 0, formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        taxa (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)
    
    
def diminuir(preco = 0, taxa = 0, formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        taxa (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)
    
    
def dobro(preco = 0, formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco = 0, formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco = 0, moeda = 'R$', formato=False):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        moeda (str, optional): _description_. Defaults to 'R$'.
        formato (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaA=10, taxaR=5):
    """_summary_

    Args:
        preco (int, optional): _description_. Defaults to 0.
        taxaA (int, optional): _description_. Defaults to 10.
        taxaR (int, optional): _description_. Defaults to 5.
    """
    print('-' * 35)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
    print(f'{taxaR}% de redução: \t{diminuir(preco, taxaR, True)}')
    print('-' * 35)