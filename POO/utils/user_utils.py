from json_utils import *
from account_utils import create_account
from ..classes.users.Client import Client


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


def user_exist(current_cpf):
    for u in users_list:
        if u["cpf"] == current_cpf:
            return True
    return False


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
