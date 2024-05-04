LIMITE = 500
LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
extrato = ""
numero_de_saques = 0
contas = []
user = []

def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Não são aceitos valores negativos!")

    return saldo, extrato

def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo: print("Você não possui saldo suficiente.")

    if valor > LIMITE: print("O valor do saque excedeu o limite.")

    if numero_saques >= LIMITE_SAQUES: print("Você não possui mais saques disponíveis")            

    if valor > 0 and not(valor > saldo) and not(valor > LIMITE) and not(numero_saques >= LIMITE_SAQUES):
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    elif valor < 0:
        print("Não são aceitos valores negativos!")

    return saldo, extrato

def extrato_t (saldo, /, *, extrato):
    print(f"\n-------------EXTRATO-------------\n{extrato}\tSaldo: R${saldo:.2f}\n")

def novo_usuario (user):
    cpf = input("Informe seu CPF (somente números): ")
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd:mm:aa): ")
    endereco = input("Informe seu endereço: ")

    user.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("------Usuário criado com sucesso------")

def cria_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": user}

while True:

    opcao = input("D - Depositar\nS - Sacar\nE - Extrato\nnu - Novo usuário\nnc - Nova conta\nlc - Listar contas\n0 - Sair\nOpção: ")

    if opcao == "D" or opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "S" or opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, limite = LIMITE, numero_saques = numero_de_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == "E" or opcao == "e":
        extrato_t(saldo, extrato = extrato)

    elif opcao == "0":
        break

    elif opcao == "nu":
        novo_usuario(user)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = cria_conta(AGENCIA, numero_conta, user)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        print({contas})

    else:
        print("Por favor selecione novamente a operação desejada.")