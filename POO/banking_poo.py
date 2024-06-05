import json

account_list = json.loads("./accounts.json")

def withdrawal(current_ID, current_value):
    for a in account_list:
        if a["ID"] == current_ID:
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


def deposit(current_ID, current_value):
    if current_value > 0:
        for a in account_list:
            if a["ID"] == current_ID:
                a["statement"] += current_value
                print(f"Deposito efetuado {current_value:.2f}")
                a["balance"].append(f"+ R${current_value:.2f}")
                return f"Saldo atual {a['statement']:.2f}"
    else:
        return "Valor invalido"


def get_statement(current_ID):
    for a in account_list:
        if a["ID"] == current_ID:
            return f"Saldo Atual: {a['statement']:.2f}"
    return "Algo deu errado, tente novamente em alguns minutos"


def get_balance(current_ID):
    print("ACCOUNT STATEMENT")
    for a in account_list:
        if a["ID"] == current_ID:
            if a["balance"]:
                for i in a["balance"]:
                    print(i)
            else:
                print("Nenhuma transacao encontrada")
            return
        print("Algo deu errado, tente novamente em alguns minutos")


def create_user():
    print(" ==== Informe seus dados pessoais ====")
    new_username = input("Seu nome de usuario, essa sera a forma que iremos nos referir a você:")
    new_id = input("Seu CPF:")
    new_password = int(input("Informe sua senha de acesso, apenas numeros:"))

    for u in users_list:
        if u["ID"] == new_id:
            print("Esse CPF já esta cadastrado, entre na sua conta ou procure uma agencia.")
            return

    users_list.append(
        {
            "name": new_username,
            "ID": new_id,
            "password": new_password
        })

    print("Usuario Cadastrado. Aceite os termos para finalizar sua conta.")
    create_account(new_id)


def create_account(current_ID):
    new_statement = 0.0
    value = 500
    new_count = 0
    print(f"Identificador {current_ID}")
    print(f"Saldo inicial {new_statement:.2f}")
    print(f"Limite de saques por dia {new_count + 3} no valor de R${value:.2f}")

    confirm = input("Y/N")
    if confirm.upper() == "Y":
        account_list.append(
            {
                "ID": current_ID,
                "statement": new_statement,
                "balance": [],
                "MAX_VALUE": value,
                "count": new_count
            }
        )
        print("Conta finalizada com sucesso")

    else:
        print("Essa opção ainda não será implementada, criamos sua conta de qualquer forma")
    return


def user_exist(current_ID, current_password):
    for user in users_list:
        if user["ID"] == current_ID:
            if user["password"] == current_password:
                user_id = user["ID"]
                return user_id
            else:
                print("As credenciais não conferem")
    print("Usuario nao existe")


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
            actions_menu(token)

        elif action == 2:
            create_user()
        elif action == 3:
            break
        else:
            print("Opcao invalida")


user_login()
