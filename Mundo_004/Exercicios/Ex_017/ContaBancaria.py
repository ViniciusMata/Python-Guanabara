from hashlib import sha256

class ContaBancaria:
    """_summary_
        Cria uma conta bancária que premite fazer saques e depósitos
    """
    
    # Método Construtor
    def __init__(self, id:int, nome: str = None, saldo:float = 0, chave:str = None):
        self._id = id                                           # (#) protected
        self._titular = nome                                    # (#) protected
        self.__saldo = saldo                                    # (-) private
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()        # (-) private
        print(f'Conta {self._id} criada com sucesso, saldo atual de R${self.__saldo:,.2f}')


    def pede_senha(self) -> str:
        from pwinput import pwinput
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha


    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo"
        #return f"Estado atual da conta: {self.__dict__}"


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')


    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        
        if self.validar_senha(chave):            
            if valor > self.__saldo:
                print(f'Saque negado de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE')
            else:
                self.__saldo -= valor
                print(f'Saque de R${valor:,.2f} autorizado na conta {self._id}')
        else:
            print(f"Senha não confere. Saque não autorizado!")


    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novoNome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novoNome) >= 5:
                self._titular = novoNome
        else:
            print(f"Senha não confere. Alteração de nome não autorizado!")