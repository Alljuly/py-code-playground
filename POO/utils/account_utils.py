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


def new_transaction(current_account: CheckingAccount, type):
    value = float(input("Insira uma valor: "))
    balance = current_account.new_transaction(type, value)
    write_json(transactions_path, balance)


def get_balance(current_id):
    for b in transactions_list:
        if b["client"] == current_id["client"]:
            print("ACCOUNT STATEMENT")
            if b["balance"]:
                print(b["balance"])
            else:
                print("Nenhuma transacao encontrada")
            return
    print("Algo deu errado, tente novamente em alguns minutos")


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
    data = {
        "client": current_id,
        "number_account": 26265,
        "agency": 3265,
        "statement": 10,
        "password": 12345,
    }

    limit = 500
    limit_wd = 3

    print(f"Cliente atual: {data['client']}")
    print(f"Saldo inicial: R${data['statement']:.2f}")
    print(f"Limite de saques por dia {limit_wd} no valor de R${limit:.2f}")

    new_account = CheckingAccount(limit, limit_wd, data)
   
    account_list = read_json(account_path)
    account_list.append(new_account.to_dict())
    write_json(account_path, account_list)
    print("Conta finalizada com sucesso.")
    # Fzr um if pro cliente confirmar depois

    return
