import json
from classes.users.Client import Client
from classes.accounts.CheckingAccount import CheckingAccount
from typing import Union

account_path = '/workspaces/py-code-playground/POO/jsons/accounts.json'
users_path = '/workspaces/py-code-playground/POO/jsons/users.json'
transactions_path = '/workspaces/py-code-playground/POO/jsons/transactions.json'


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


users_list = read_json(users_path)
account_list = read_json(account_path)
transactions_list = read_json(transactions_path)

def write_json(path, list):
    with open(path, 'w') as f:
        json.dump(list, f, indent=4)


def convert_json_to_account(obj) -> CheckingAccount:
 
    data = {
    "client" : obj["client"],
    "number_account" : obj["number_account"],
    "agency" : obj["agency"],
    "statement" : obj["statement"],
    "password" : obj["password"],
    }

    limit = obj["limit"]
    wd_limit = obj["limit_wd"]

    account = CheckingAccount(limit, wd_limit, data)
    return account


def new_transaction(current_account : CheckingAccount):
    value = float(input("Insira uma valor: "))
    balance = current_account.new_transaction(type, value)
    write_json(transactions_path, balance)


def get_balance(current_id):
    
    for b in transactions_list:
         if b["client"] == current_id:
            print("ACCOUNT STATEMENT")
            if b["balance"]:
                 print(b["balance"])
            else:
                print("Nenhuma transacao encontrada")
            return
    print("Algo deu errado, tente novamente em alguns minutos")


def get_statement(current_account : CheckingAccount):
    statement = current_account.get_statement()
    return statement


def user_exist(current_cpf):
    for u in users_list:
        if u["cpf"] == current_cpf:
            return True
    return False


def account_exist(current_cpf)-> Union[CheckingAccount, None]:
    for a in account_list:
        if a["cpf"] == current_cpf:
            ac = convert_json_to_account(a)
            return ac
    return None


def create_user():
    print(" ==== Informe seus dados pessoais ====")
    new_name = input("Teste")
    new_cpf = input("123456789123")
    new_date = input("27-05-1997")
    new_address = input("1313 E Main St, Portage MI 49024-2001")
    
    if user_exist(new_cpf):
        print("Esse CPF já esta cadastrado, entre na sua conta ou procure uma agencia.")
        return
    
    new_user = Client(new_name, new_cpf, new_date, new_address)
    users_list = read_json(users_path)
    users_list.append(new_user)

    create_account(new_cpf)

    with open(users_path, 'w') as u:
        json.dump(users_list, u, indent=4)

    print("Usuario Cadastrado.")

####
def create_account(current_id):
    data = {
        "client" : current_id,
        "number_account" : 26265,
        "agency" : 3265,
        "statement" : 10,
        "password" : 12345,
    }

    limit = 500
    limit_wd = 3

    print(f"Cliente atual: {data['client']}")
    print(f"Saldo inicial: R${data['statement']:.2f}")
    print(f"Limite de saques por dia {limit_wd} no valor de R${limit:.2f}")

    new_account = CheckingAccount(limit, limit_wd, data)
    #Fzr um if pro cliente confirmar depois

    account_list.append(new_account)
    write_json(account_path, account_list)
    print("Conta finalizada com sucesso.")
    
    return


def user_login(current_id, current_password):
    for u in account_list:
        if u["client"] == current_id:
            if u["password"] == int(current_password):
                user_id = u["client"]
                return user_id
            else:
                print("As credenciais não conferem")
                return None
    print("Usuario nao encontrado")


def actions_menu(current_account: CheckingAccount):
    while True:
        """print("\n=== Menu ===")
        print("1. Verificar Extrato")
        print("2. Fazer saque")
        print("3. Fazer depósito")
        print("4. Verificar Saldo")
        print("5. Sair")"""

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
            print(msg)
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
            password = input("Informe sua senha: ")

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
