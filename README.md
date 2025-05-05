# Sistema Bancário em Python

Este é um projeto de um sistema bancário simples, desenvolvido em Python, que simula operações básicas de um banco. O programa é executado via terminal e oferece funcionalidades como depósito, saque, extrato, criação de usuários e contas, e listagem de contas existentes.

## Funcionalidades

O menu principal apresenta as seguintes opções para o usuário:

- `[d]` Depositar
- `[s]` Sacar
- `[e]` Extrato
- `[nu]` Novo usuário
- `[nc]` Criar conta
- `[lc]` Listar contas
- `[x]` Sair

## ⚙️ Lógica do Projeto

O projeto utiliza estruturas como listas, dicionários, funções com diferentes tipos de parâmetros e tratamento de exceções. O fluxo principal acontece dentro da função `main()`, onde o sistema executa em loop até que o usuário opte por sair.

## 🔧 Funções Criadas

### `menu()`
Exibe o menu de opções e retorna a escolha do usuário.

---

### `deposito(saldo, valor, extrato, /)`
Realiza o depósito de um valor positivo no saldo e adiciona uma descrição ao extrato.

- **Argumentos position-only** (`/`):
  - `saldo`
  - `valor`
  - `extrato`

---

### `saque(*, saldo, extrato, LIMITE_TOTAL_SAQUE, numero_saques, LIMITE_SAQUES, valor_retirado)`
Realiza um saque, respeitando os limites de saldo, valor máximo por saque e quantidade máxima de saques.

- **Argumentos keyword-only** (`*`):
  - `saldo`
  - `extrato`
  - `LIMITE_TOTAL_SAQUE`
  - `numero_saques`
  - `LIMITE_SAQUES`
  - `valor_retirado`

---

### `relatorio_financeiro(saldo, /, *, extrato)`
Exibe o extrato das transações realizadas.

- `saldo` é **position-only** (`/`)
- `extrato` é **keyword-only** (`*`)

---

### `criar_usuario(usuarios)`
Solicita os dados do usuário (CPF, nome, data de nascimento, endereço) e adiciona à lista de usuários, caso o CPF ainda não esteja cadastrado.

---

### `filtrar_usuario(CPF, usuarios)`
Filtra a lista de usuários e retorna aquele com o CPF correspondente (ou `None` se não existir).

---

### `criar_conta(AGENCIA, numero_conta, usuarios)`
Cria uma nova conta bancária para um usuário existente.

---

### `listar_contas(contas_corrente, usuarios)`
Exibe todas as contas de um determinado CPF.

---

### `main()`
Executa o loop principal do programa, gerenciando as interações do usuário com o sistema bancário.

##  Conceitos Utilizados

- Argumentos position-only (`/`) e keyword-only (`*`)
- Listas e dicionários
- Laços de repetição e condicionais
- Manipulação de strings e números
- Boas práticas como modularização do código


## Créditos
Desenvolvido por Monique Santos durante o Bootcamp: Vivo - Python AI Backend Developer, da DIO.

