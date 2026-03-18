from model.Historico import Historico

class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0
        self.numero = numero
        self.agencia = cliente
        self.historico = Historico()

    def Sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado com sucesso! Saldo: {self.saldo}")
            return True
        print("Saldo insuficiente")
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"{valor} depositado com sucesso seu saldo atual: {self.saldo}")
            return True
        print("Valor inválido")
        return False