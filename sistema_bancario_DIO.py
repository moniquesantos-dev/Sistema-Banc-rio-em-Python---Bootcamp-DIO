'''Projeto - Sistema Bancário em Python - DIO Academy
Desafio: Implementar apenas 3 operações: depósito, saque e extrato.
Operação depósito: Devem ser armazenados em uma variável e exibidos na operação de extrato.
Operação saque: Permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque
    Caso o usuário não tenha saldo em conta o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
    Todos os saques devem ser armazenados em uma viarável e exibidos na operação de extrato.
Operação extrato: Deve listar todos os depósitos e saques realizados em conta. No fim da listagem deve ser exibido o saldo atual em conta. 
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx. 
'''
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> Escolha uma das opções: """

saldo = 400
LIMITE_TOTAL_SAQUE = 500  # Limite total por saque é de R$ 500,00
extrato = []  # Agora é uma lista
numero_saques = 0
LIMITE_SAQUES = 3  # Limite diário de saques

while True:
    selecao = input(menu).lower()

    if selecao == 'd':
        valor = float(input('Qual valor deseja depositar? R$').replace(',', '.'))
        if valor > 0:
            saldo += valor
            print(f'O depósito de R${valor:.2f} foi realizado. Verifique seu extrato caso queira confirmar o valor em conta.')
            extrato.append(f'Depósito realizado: +R${valor:.2f}')
        else:
            print('O valor do depósito deve ser maior do que zero.')

    elif selecao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite máximo de saques diários.")
            continue

        saque = input('Qual valor deseja sacar? R$')
        try:
            saque = float(saque.replace(',', '.'))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue

        if saque > LIMITE_TOTAL_SAQUE:
            print(f'O limite máximo para cada saque é de R${LIMITE_TOTAL_SAQUE:.2f}')
            continue

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
            continue

        if saldo < saque:
            print('Você não possui saldo suficiente para ser sacado.')
            continue

        saldo -= saque
        extrato.append(f'Saque realizado: -R${saque:.2f}')
        numero_saques += 1

        print(f'Seu saque de R${saque:.2f} foi realizado com sucesso!')
        if numero_saques < LIMITE_SAQUES:
            print(f"Você ainda pode realizar {LIMITE_SAQUES - numero_saques} saques hoje.\n")

    elif selecao == 'e':
        print("\n============ EXTRATO BANCÁRIO ============")
        if not extrato:
            print("Nenhuma movimentação foi realizada.")
        else:
            for operacao in extrato:
                print(operacao)
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("==========================================")

    elif selecao == 'x':
        print('Atendimento finalizado!')
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')
