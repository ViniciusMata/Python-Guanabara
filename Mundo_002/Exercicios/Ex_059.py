# Crie um programa que leia dois valores e mostre um menu nda tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# (( Aula_014 ))

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif opcao == 3:
        print(f'O maior valor entre {n1} e {n2} é {max(n1, n2)}.')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
