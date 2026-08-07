# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
# (( Aula_012 ))

preco = float(input('Digite o preço do produto: R$ '))
print('''Escolha a forma de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Digite a opção desejada (1, 2, 3 ou 4): '))

if opcao == 1:
    valor_final = preco * 0.9
    print(f'Pagamento à vista em dinheiro/cheque. Valor final: R$ {valor_final:.2f} (10% de desconto).')
elif opcao == 2:
    valor_final = preco * 0.95
    print(f'Pagamento à vista no cartão. Valor final: R$ {valor_final:.2f} (5% de desconto).')
elif opcao == 3:
    valor_final = preco
    print(f'Pagamento em até 2x no cartão. Valor final: R$ {valor_final:.2f} (preço normal).')
elif opcao == 4:
    valor_final = preco * 1.2
    print(f'Pagamento em 3x ou mais no cartão. Valor final: R$ {valor_final:.2f} (20% de juros).')
else:
    print('Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).')