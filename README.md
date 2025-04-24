# Sistema Bancário em Python

Um **Sistema Bancário** desenvolvido durante o **Bootcamp da DIO** utilizando a linguagem **Python**. Este sistema permite a realização de depósitos, saques e visualização de extrato de uma conta bancária, com controle de limites de saque diário e saldo disponível.

## Funcionalidades

- **Depositar**: Permite ao usuário realizar depósitos na conta.
- **Sacar**: Permite ao usuário realizar saques, respeitando limites de valor e quantidade diária de saques.
- **Extrato**: Exibe o extrato bancário, mostrando todas as operações realizadas.
- **Limites de Saque**: Limita o valor máximo de cada saque e a quantidade de saques por dia.

## Tecnologias Utilizadas

- **Python** (versão 3.x)
- **Git** para controle de versão


# Como Funciona

O sistema oferece um menu com as opções:

[d] Depositar

[s] Sacar

[e] Extrato

[x] Sair

- Depósitos são realizados com valores maiores que 0, e o saldo é atualizado automaticamente.
- aques respeitam um limite diário de 3 transações e um valor máximo de R$500 por transação.
- O extrato exibe todas as movimentações feitas no sistema, com valores de depósitos e saques.


## Exemplos de Saída:

### 1. Menu Inicial

```sh
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> Escolha uma das opções:
```
### 2. Depósito Realizado

```sh
Qual valor deseja depositar? R$500
O depósito de R$500.00 foi realizado. Verifique seu extrato caso queira confirmar o valor em conta.
```

### 3. Saque Realizado

- Saque dentro do limite:

```sh
Qual valor deseja sacar? R$200
Seu saque de R$200.00 foi realizado com sucesso!
Você ainda pode realizar 2 saques hoje.
```

- Saque acima do limite:

```sh
Qual valor deseja sacar? R$600
O limite máximo para cada saque é de R$500.00
```

- Saldo insuficiente:

```sh
Qual valor deseja sacar? R$3000
Você não possui saldo suficiente para ser sacado.
```

### 4. Extrato Bancário

```sh
============ EXTRATO BANCÁRIO ============
Depósito realizado: R$500.00
Saque realizado: -R$200.00

Saldo atual: R$2300.00
==========================================
```

### 5. Opção de Sair

```sh
Atendimento finalizado!
```

## Créditos
Desenvolvido por Monique Santos durante o Bootcamp: Vivo - Python AI Backend Developer, da DIO.
