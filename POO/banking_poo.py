
from classes.accounts.CheckingAccount import CheckingAccount
from utils.user_utils import create_user, user_login
from utils.account_utils import new_transaction, get_balance, get_statement, account_exist


def actions_menu(current_account: CheckingAccount):
    while True:
        print("\n=== Menu ===")
        print("1. Verificar Extrato")
        print("2. Fazer saque")
        print("3. Fazer depósito")
        print("4. Verificar Saldo")
        print("5. Sair")

        action = int(input())

        if action == 1:
            get_balance(current_account)
        elif action == 2:
            type = "wd" 
            new_transaction(current_account, type)
        elif action == 3:
            type = "deposit"
            new_transaction(current_account, type)
        elif action == 4:
            msg = get_statement(current_account)
            print(f'{msg:.2f}')
        elif action == 5:
            break
        else:
            print("Opcao invalida")

def user_menu():
    while True:
        print("\n=== NEWBANK ===")
        print("1. Entrar na sua conta.")
        print("2. Crie sua conta.")
        print("3. Sair")

        action = int(input())

        if action == 1:
            user_id = input("Seu CPF: ")
            password = int(input("Informe sua senha: "))

            token = user_login(user_id, password)
            if token:
                current_account = account_exist(token)
                actions_menu(current_account)

        elif action == 2:
            create_user()
        elif action == 3:
            break
        else:
            print("Opcao invalida")

user_menu()
