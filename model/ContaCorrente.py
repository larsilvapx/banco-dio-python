from model.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self,cliente, numero,limite = 500, limite_saques = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print(f"Limite de saques atingidos {self.limite_saques}")
            return False

        if valor > (self.saldo + self.limite):
            print(f"Limite insuficiente {self.limite + self.saldo}")
            return False

        self.saques_realizados += 1
        print(f"Saque realizado com sucesso {self.saldo}")
        return super().sacar(valor)
