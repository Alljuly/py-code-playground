statement = 10
balance = []
MAX_VALUE = 500
count = 0


def withdrawal(current_value, current_statement):
    if count < 3:
        if current_value and current_value <= current_statement and current_value <= MAX_VALUE:
            print(f"Sacar {current_value:.2f}")
            current_statement -= current_value
            balance.append(f"- {current_value:.2f}")
        else:
            print("Algo está errado. Verifique o saldo da conta ou tente novamente em alguns minutos.")
    else:
        print("Limite diario de saques ultrapassado")
    return statement


def deposit(current_value, current_statement):
    if current_value > 0:
        print(f"Depositar {current_value:.2f}")
        current_statement += current_value
        balance.append(f"+ {current_value:.2f}")
    return current_statement


def get_statement(current_statement):
    print(f"Statement: {current_statement:.2f}")


def get_balance(current_balance):
    print("ACCOUNT STATEMENT")
    for n in current_balance:
        print(n)



def actions_menu():
    while True:
        print("\n=== Menu do Banco ===")
        print("1. Verificar Extrato")
        print("2. Fazer saque")
        print("3. Fazer depósito")
        print("4. Sair")

        action = int(input())

        if action == 1:
            get_balance(balance)
        elif action == 2:
            value = int(input("Insira uma valor: "))
            withdrawal(value, statement)
        elif action == 3:
            value = int(input("Insira uma valor: "))
            deposit(value, statement)
        elif action == 4:
            return False


actions_menu()
