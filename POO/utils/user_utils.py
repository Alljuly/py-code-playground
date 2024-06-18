from classes.users.Client import Client
from .account_utils import create_account
from .json_utils import *



def create_user():
    print(" ==== Informe seus dados pessoais ====")
    new_name = input("Seu nome:")
    new_cpf = input("Seu CPF:")
    new_date = input("Informe sua data de nascimento no formato: 01-02-2003")
    new_address = input("Informe seu endereço")

    if user_exist(new_cpf):
        print("Esse CPF já esta cadastrado, entre na sua conta ou procure uma agencia.")
        return

    new_user = Client(new_name, new_cpf, new_date, new_address)
    users_list = read_json(users_path)
    users_list.append(new_user.to_dict()) 

    create_account(new_cpf)

    write_json(users_path, users_list)

    print("Usuario Cadastrado.")


def user_exist(current_cpf):
    for u in users_list:
        if u["cpf"] == current_cpf:
            return True
    return False


def user_login(current_id: str, current_password: int):
    if user_exist(current_id):
        for u in account_list:
            if u["client"] == current_id:
                if u["password"] == current_password:
                    user_id = u["client"]
                    return user_id
                else:
                    print("As credenciais não conferem")
                    return None
    print("Usuario nao encontrado")    
