import json
import os
from classes.User import User
from classes.Account import Account

current_dir = os.path.dirname(os.path.abspath(__file__))

account_path = os.path.join(current_dir, 'accounts.json')
users_path = os.path.join(current_dir, 'users.json')

with open(account_path, 'r') as f:
    account_list = json.load(f)

with open(users_path, 'r') as f:
    users_list = json.load(f)


def withdrawal(current_id, current_value):
    for a in account_list:
        if a["ID"] == current_id:
            if a["count"] < 3:
                if current_value and current_value <= a["statement"] and current_value <= a["MAX_VALUE"]:
                    print(f"Sacar {current_value:.2f}")
                    a["statement"] -= current_value
                    a["balance"].append(f"- R${current_value:.2f}")
                    a["count"] += 1

                else:
                    print("Algo está errado. Verifique o saldo da conta ou tente novamente em alguns minutos.")
            else:
                print("Limite diario de saques ultrapassado")
        return f"Saldo atual: R${a['statement']:.2f}"


def deposit(current_id, current_value):
    if current_value > 0:
        for a in account_list:
            if a["ID"] == current_id:
                a["statement"] += current_value
                print(f"Deposito efetuado {current_value:.2f}")
                a["balance"].append(f"+ R${current_value:.2f}")
                return f"Saldo atual {a['statement']:.2f}"
    else:
        return "Valor invalido"


def get_statement(current_id):
    for a in account_list:
        if a["ID"] == current_id:
            return f"Saldo Atual: {a['statement']:.2f}"
    return "Algo deu errado, tente novamente em alguns minutos"


def get_balance(current_id):
    print("ACCOUNT STATEMENT")
    for a in account_list:
        if a["ID"] == current_id:
            if a["balance"]:
                for i in a["balance"]:
                    print(i)
            else:
                print("Nenhuma transacao encontrada")
            return
        print("Algo deu errado, tente novamente em alguns minutos")


def create_user():
    print(" ==== Informe seus dados pessoais ====")
    new_username = input("Seu nome de usuario, essa sera a forma que iremos nos referir a você: ")
    new_id = input("Seu CPF: ")
    new_password = int(input("Informe sua senha de acesso, apenas numeros: "))

    for u in users_list:
        if u["ID"] == new_id:
            print("Esse CPF já esta cadastrado, entre na sua conta ou procure uma agencia.")
            return

    new_user = User(new_username, new_id, new_password)
    users_list.append(new_user.to_dict())

    create_account(new_id)

    with open(users_path, 'w') as u:
        json.dump(users_list, u, indent=4)

    print("Usuario Cadastrado.")



def create_account(current_id):
    new_statement = 0.0
    value = 500
    new_count = 0
    new_balance = []
    print(f"Identificador {current_id}")
    print(f"Saldo inicial {new_statement:.2f}")
    print(f"Limite de saques por dia {new_count + 3} no valor de R${value:.2f}")

    confirm = input("Y/N ")
    if confirm.upper() == "Y":
        new_account = Account(current_id, new_statement, value, new_balance, new_count)
        account_list.append(new_account.to_dict())

        with open(account_path, 'w') as ac:
            json.dump(account_list, ac, indent=4)

        print("Conta finalizada com sucesso")

    """else:
        print("Essa opção ainda não será implementada, criamos sua conta de qualquer forma")
        new_account = Account(current_id, new_statement, value, new_balance, new_count)
        account_list.append(new_account.to_dict())

        with open(account_path, 'w') as ac:
            json.dump(account_list, ac, indent=4)
        print("Conta finalizada com sucesso")
    """
    return


def user_exist(current_id, current_password):
    for user in users_list:
        if user["ID"] is current_id:
            if user["password"] == current_password:
                user_id = user["ID"]
                return user_id
            else:
                return "As credenciais não conferem"
    return None


def actions_menu(current_user_id):
    while True:
        print("\n=== Menu ===")
        print("1. Verificar Extrato")
        print("2. Fazer saque")
        print("3. Fazer depósito")
        print("4. Verificar Saldo")
        print("5. Sair")

        action = int(input())

        if action == 1:
            get_balance(current_user_id)
        elif action == 2:
            value = float(input("Insira uma valor: "))
            msg = withdrawal(current_user_id, value)
            print(msg)
        elif action == 3:
            value = float(input("Insira uma valor: "))
            msg = deposit(current_user_id, value)
            print(msg)
        elif action == 4:
            msg = get_statement(current_user_id)
            print(msg)
        elif action == 5:
            break
        else:
            print("Opcao invalida")


def user_login():
    while True:
        print("\n=== NEWBANK ===")
        print("1. Entrar na sua conta.")
        print("2. Crie sua conta.")
        print("3. Sair")

        action = int(input())

        if action == 1:
            user_id = input("Seu CPF: ")
            password = input("Informe sua senha: ")

            token = user_exist(user_id, password)
            if token:
                actions_menu(token)

        elif action == 2:
            create_user()
        elif action == 3:
            break
        else:
            print("Opcao invalida")


user_login()
