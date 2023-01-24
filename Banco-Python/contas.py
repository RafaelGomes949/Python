"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (simples) que tem clientes, contas e um banco.
A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
sacar/depositar nessa conta.
Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""


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
