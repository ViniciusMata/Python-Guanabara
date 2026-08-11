# Crie um programa que tenha uma função fatorial() que receba dois parametros: o primiero que indique o numero a calcular e o outro chamado show, que
# será um valor logico(opcional) indicando se será mostrado ou não na tela o processo de calcuo do fatorial
# (( Aula_021 ))

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor fo Fatorial de um número n
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(5, show=False))
help(fatorial)