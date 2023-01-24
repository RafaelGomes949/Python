class Conta:
    def __init__(self, conta, agencia, saldo=0):
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        self.verificarsaldo(f'(Você depositou {deposito} reais)')

    def sacar(self, saque):
        self.saldo = self.saldo - saque
        if self.saldo < 0:
            print(f'Você tentou sacar {saque} reais')
            print("Saldo insuficiente, operação cancelada")
            self.saldo = self.saldo + saque
            self.verificarsaldo()
        else:
            self.verificarsaldo(f'(Você sacou {saque} reais)')

    def verificarsaldo(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('------------------------------------------------------')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},'\
            ' {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    pass


class ContaCorrente(Conta):
    def __init__(self, conta, agencia, saldo=0, limite=0):
        super().__init__(conta, agencia, saldo)
        self.limite = limite

    def sacar(self, saque):
        self.saldo = self.saldo - saque
        if self.saldo < -(self.limite):
            print(f'Você tentou sacar {saque} reais')
            print("Saldo insuficiente, operação cancelada")
            self.saldo = self.saldo + saque
            self.verificarsaldo()
        else:
            self.verificarsaldo(f'(Você sacou {saque} reais)')


# class Pessoa:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade
#
#
# class Cliente(Pessoa):
#    def __init__(self, nome, idade, conta):
#        super().__init__(nome, idade)
#        self.conta = conta


if __name__ == '__main__':
    cp1 = ContaPoupanca(222, 111, 50)
    cp1.verificarsaldo()
    cp1.depositar(100)
    cp1.sacar(30)
    cp1.sacar(200)

    print('#######################################################')
    print(' ')
    cc1 = ContaCorrente(222, 111, 0, 100)
    cc1.verificarsaldo()
    cc1.depositar(20)
    cc1.sacar(100)
    cc1.sacar(150)
    print('#######################################################')
    print(' ')
