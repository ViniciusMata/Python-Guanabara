class ContaBancaria:
    """_summary_
        Cria uma conta bancária que premite fazer saques e depósitos
    """
    
    # Método Construtor
    def __init__(self, id, nome, saldo):
        self.id = id                    # (+) publico
        self._titular = nome            # (#) protected
        self.__saldo = saldo            # (-) private
        print(f'Conta {self.id} criada com sucesso, saldo atual de R${self.__saldo:,.2f}')


    def __str__(self):
        #return f'A conta {self.id} de {self.titular} tem R${self.__saldo:,.2f} de saldo'
        return f"Estado atual da conta: {self.__dict__}"


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')


    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')