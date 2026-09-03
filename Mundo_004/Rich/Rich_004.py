from rich import print
from rich import inspect

class ContaBancaria:
    """_summary_
        Cria uma conta bancária que premite fazer saques e depósitos
    """
    
    # Método Construtor
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso, saldo atual de R${self.saldo:,.2f}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'


    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')


    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
            
c = ContaBancaria(id=111, nome='Vinicius', saldo=3000)
inspect(c)