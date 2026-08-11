# Modifique as funções criada no Ex_107.py e Ex_108.py para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser 
# ou nao formatado pela funcao moeda, desenvolvido no Ex_108.py
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