class Historico:

    def _init_(self):
        self.transacoes = []

    def adicionar_transscao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar(self):
        for t in self.transacoes:
            print(f"{t.__class__.__name__}: R$: {t.valor}")