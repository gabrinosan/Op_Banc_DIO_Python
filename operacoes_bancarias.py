LIMITE = 500
LIMITE_SAQUES = 3
saldo = 0
extrato = ""
numero_de_saques = 0

def deposito (saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Não são aceitos valores negativos!")

    return saldo, extrato

while True:

    opcao = input("D - Depositar\nS - Sacar\nE - Extrato\n0 - Sair\nOpção: ")

    if opcao == "D" or opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = deposito(saldo = saldo, valor = valor, extrato = "extrato", limite = LIMITE, numero_saques = numero_de_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == "S" or opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo: print("Você não possui saldo suficiente.")

        if valor > LIMITE: print("O valor do saque excedeu o limite.")

        if numero_de_saques >= LIMITE_SAQUES: print("Você não possui mais saques disponíveis")            

        if valor > 0 and not(valor > saldo) and not(valor > LIMITE) and not(numero_de_saques >= LIMITE_SAQUES):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        elif valor < 0:
            print("Não são aceitos valores negativos!")

    elif opcao == "E" or opcao == "e":
        print("\nEXTRATO")
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Por favor selecione novamente a operação desejada.")