from model.Cliente import PessoaFisica
from model.ContaCorrente import ContaCorrente
from model.Transacao import Saque, Deposito
from util.Menu import exibir_menu

clientes = []
contas = []


def buscar_cliente(cpf):
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None


def buscar_conta(numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None


while True:
    exibir_menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")

        cliente = PessoaFisica(nome, cpf, nascimento, endereco)
        clientes.append(cliente)

        print(" Cliente criado com sucesso!")

    elif opcao == "2":
        cpf = input("CPF do cliente: ")
        cliente = buscar_cliente(cpf)

        if cliente:
            numero = len(contas) + 1
            conta = ContaCorrente(cliente, numero)

            cliente.adicionar_conta(conta)
            contas.append(conta)

            print(" Conta criada com sucesso!")
        else:
            print(" Cliente não encontrado!")

    elif opcao == "3":
        numero = int(input("Conta: "))
        valor = float(input("Valor: "))

        conta = buscar_conta(numero)
        if conta:
            deposito = Deposito(valor)
            conta.cliente.realizar_transacao(conta, deposito)
        else:
            print(" Conta não encontrada!")

    elif opcao == "4":
        numero = int(input("Conta: "))
        valor = float(input("Valor: "))

        conta = buscar_conta(numero)
        if conta:
            saque = Saque(valor)
            conta.cliente.realizar_transacao(conta, saque)
        else:
            print(" Conta não encontrada!")

    elif opcao == "5":
        numero = int(input("Conta: "))
        conta = buscar_conta(numero)

        if conta:
            print("\n EXTRATO:")
            conta.historico.mostrar()
            print(f" Saldo: R${conta.saldo}")
        else:
            print(" Conta não encontrada!")

    elif opcao == "6":
        print("\n LISTA DE CONTAS:")
        for conta in contas:
            print(f"Conta: {conta.numero} - {conta.cliente.nome}")

    elif opcao == "0":
        print(" Encerrando sistema...")
        break

    else:
        print(" Opção inválida!")