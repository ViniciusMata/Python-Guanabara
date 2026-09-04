from ContaBancaria import ContaBancaria

def main():
    c1 = ContaBancaria(id=111, nome='Maria', saldo=5000)
    c1.depositar(1000)
    c1.sacar(-100)
    c1.saldo = 0
    print(c1)

if __name__ == "__main__":
    main()