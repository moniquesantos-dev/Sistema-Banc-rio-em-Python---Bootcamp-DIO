def menu():
    
    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário   
    [nc] Criar conta
    [lc] Listar contas
    [x] Sair
    => Escolha uma das opções: """
    return input(menu)

def deposito(saldo, valor, extrato, /): # argumento: positional only
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito realizado: +R${valor:.2f}')
        sucesso = True
    else:
        sucesso = False
    return saldo, extrato, sucesso

def saque(*, saldo, extrato, LIMITE_TOTAL_SAQUE, numero_saques, LIMITE_SAQUES, valor_retirado): # argumento: keyword only
    if valor_retirado <= 0:
        print("Valor do saque deve ser maior que zero.")
        return saldo, extrato, numero_saques
     
    if saldo < valor_retirado:
        print('Você não possui saldo suficiente para sacar esse valor.')
        return saldo, extrato, numero_saques
    
    if valor_retirado > LIMITE_TOTAL_SAQUE:
        print(f'O limite máximo para cada saque é de R${LIMITE_TOTAL_SAQUE}.')
        return saldo, extrato, numero_saques
    
    if numero_saques >= LIMITE_SAQUES: 
        print('Você atingiu o limite máximo de saques diários.')
        return saldo, extrato, numero_saques         
    else:    
        # validação do saque    
        saldo -= valor_retirado
        extrato.append(f'Saque realizado: -R${valor_retirado:.2f}')
        numero_saques += 1
        print(f'Saque de R${valor_retirado:.2f} realizado com sucesso!')
        if numero_saques < LIMITE_SAQUES:
            print(f'Você ainda pode realizar {LIMITE_SAQUES - numero_saques} saques hoje.\n')
        return saldo, extrato, numero_saques    

def relatorio_financeiro(saldo, /, *, extrato): # argumento: positiona only e keyword only
    print('\n' + '=' * 12 + ' EXTRATO BANCÁRIO ' + '=' * 12)
    
    if not extrato:
        print('\nNenhuma movimentação foi realizada.')
    else:
        for operacao in extrato:
            print(operacao)
    return saldo, extrato

def criar_usuario(usuarios):
    CPF = input('Informe seu número de CPF: ')
    try: 
        CPF = int(CPF.replace('.', '').replace('-', ''))        
    except ValueError:
        print('Valor inválido.')

    usuario = filtrar_usuario(CPF, usuarios)

    if usuario:
        print('\nJá existe um usuário com esse CPF.')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento: ')
    endereco = input('Informe seu endereço completo (lograduoro, nº - bairro - cidade/sigla estado): ')

    usuarios.append({
        'nome': nome, 
        'data de nascimento': data_nascimento, 
        'CPF': CPF, 
        'endereco': endereco})
    
    print(f'Usuário criado com sucesso! Seu número de registro: {CPF}')

def filtrar_usuario(CPF, usuarios):    
    return next ((usuario for usuario in usuarios if usuario["CPF"] == CPF), None)

def criar_conta(AGENCIA, numero_conta, usuarios):
    CPF = input('Informe o CPF do usuário: ')
    try: 
        CPF = int(CPF.replace('.', '').replace('-', ''))        
    except ValueError:
        print('Número de CPF incorreto.')
        
    usuario = filtrar_usuario(CPF, usuarios)
    
    if usuario:
        print('Conta criada com sucesso!')
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print('Usuário não encontrado. Fluxo de criação de conta encerrado.')

def listar_contas(contas_corrente, usuarios):
    cpf_input = input("Digite o CPF do titular: ")
    try:
        cpf_input = int(cpf_input.replace('.', '').replace('-', ''))
    except ValueError:
        print("CPF inválido. Digite apenas números.")
        return

    usuario = filtrar_usuario(cpf_input, usuarios)
    
    if not usuario:
        print("Usuário não encontrado.")
        return

    contas_do_usuario = [conta for conta in contas_corrente if conta["usuario"]["CPF"] == cpf_input]
    
    if not contas_do_usuario:
        print("Usuário não encontrado.")
        return
    
    print('\n' + '=' * 12 + ' CONTAS CADASTRADAS ' + '=' * 12)
    encontrou = False
    for conta in contas_corrente:
        if conta["usuario"]["CPF"] == cpf_input:
            print(f'''
        Agência: {conta["agencia"]}
        Número da conta: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        ''')
        encontrou = True        
    if not encontrou:
        print("Nenhuma conta foi encontrada para esse CPF.")
    print('\n' + '=' * 43)
    return contas_corrente       

def main():
    LIMITE_TOTAL_SAQUE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 2000
    extrato = []
    usuarios = []
    contas_corrente = []
    numero_saques = 0

    while True:
        selecao = menu()
        #  saldo anterior = saldo  # Armazena o saldo anterior

        if selecao == 'd':
            valor = float(input('Qual valor deseja depositar? R$').replace(',', '.'))
            saldo, extrato, sucesso = deposito(saldo, valor, extrato)

            if sucesso:
                print(f'O depósito de R${valor:.2f} foi realizado com sucesso.')
                print('Verifique seu extrato caso queira confirmar o valor em conta.')
            else:
                print('Erro: o valor do depósito deve ser maior do que zero.')

        elif selecao == 's':
            valor_retirado = input('Qual valor deseja sacar? R$')
            try:
                valor_retirado = float(valor_retirado.replace(',', '.'))
            except ValueError:
                print('Valor inválido. Digite um número.')
                continue
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                LIMITE_TOTAL_SAQUE=LIMITE_TOTAL_SAQUE,
                LIMITE_SAQUES=LIMITE_SAQUES,
                valor_retirado = valor_retirado,
            )

        elif selecao == 'e':
            saldo, extrato = relatorio_financeiro(saldo, extrato=extrato)
            print(f'\nSaldo atual: R${saldo:.2f}')
            print('\n' + '=' * 42)
            continue

        elif selecao == 'nu':
            criar_usuario(usuarios)
        
        elif selecao == "nc":
            numero_conta = len(contas_corrente) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas_corrente.append(conta)
            
        elif selecao == 'lc':
            listar_contas(contas_corrente, usuarios)
            

        elif selecao == 'x':
            print('Atendimento finalizado.')
            break
        else: 
            print('Operação inválida. Por favor, selecione novamente a operação desejada.')

main()
