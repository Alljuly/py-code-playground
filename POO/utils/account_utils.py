from .json_utils import *

from classes.accounts.CheckingAccount import CheckingAccount
from typing import Union

def convert_json_to_account(obj) -> CheckingAccount:
    data = {
        "client": obj["client"],
        "number_account": obj["number_account"],
        "agency": obj["agency"],
        "statement": obj["statement"],
        "password": obj["password"],
    }

    limit = obj["limit"]
    wd_limit = obj["wd_limit"]

    account = CheckingAccount(limit, wd_limit, data)
    return account


def new_transaction(current_account: CheckingAccount, type) -> CheckingAccount:
    transactions_list  = read_json(transactions_path)
    value = float(input("Insira uma valor: "))

    if current_account.limit_wd(transactions_list) and current_account.limit_value(value) and value > 0:    
        balance = current_account.new_transaction(type, value)
        transactions_list.append(balance[0])
        write_json(transactions_path, transactions_list)
        current_account.statement = balance[1]
        return current_account
    else:
        print("Verifique seu saldo e limite diario de transacoes ou tente novamente mais tarde")
        return None


def set_statement(current_account: CheckingAccount):
    account_list = read_json(account_path)
    value = current_account.statement
    client  = current_account.client

    for ac in account_list:
        if ac["client"] == client:
            ac["statement"] = value
            break

    write_json(account_path, account_list)


def get_balance(client):
    transactions_found = False
    print("ACCOUNT STATEMENT")
    print("-" * 50)
    print(f"{'Value':<10} {'Date':<20} {'Type':<10}")
    print("-" * 50)
    for balance in transactions_list:
        if balance["client"] == client:
            transactions_found = True
            print(f"{balance['value']:<10} {balance['date']:<20} {balance['type']:<10}")
    if not transactions_found:
        print("Nenhuma transacao encontrada")
    


def get_statement(current_account: CheckingAccount) -> float:
    statement = current_account.get_statement()
    return float(statement)


def account_exist(current_cpf)-> Union[CheckingAccount, None]:
    for a in account_list:
        if a["client"] == current_cpf:
            ac = convert_json_to_account(a)
            return ac
    return None

###
def create_account(current_id):
    password = int(input("Informe sua senha"))
    data = {
        "client": current_id,
        "number_account": 26265,
        "agency": 3265,
        "statement": 10,
        "password": password,
    }

    limit = 500
    limit_wd = 3

    print(f"Cliente atual: {data['client']}")
    print(f"Saldo inicial: R${data['statement']:.2f}")
    print(f"Limite de saques por dia {limit_wd} no valor de R${limit:.2f}")

    new_account = CheckingAccount(limit, limit_wd, data)
   
    
    account_list.append(new_account.to_dict())
    write_json(account_path, account_list)
    print("Conta finalizada com sucesso.")
    # Fzr um if pro cliente confirmar depois

    return
