import json

account_path = '/workspaces/py-code-playground/POO/jsons/accounts.json'
users_path = '/workspaces/py-code-playground/POO/jsons/users.json'
transactions_path = '/workspaces/py-code-playground/POO/jsons/transactions.json'


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def write_json(path, json_list):
    with open(path, 'a') as f:
        json.dump(json_list, f, indent=4)


def rewrite_json(path, json_list):
    with open(path, 'w') as f:
        json.dump(json_list, f, indent=4)


users_list = read_json(users_path)
account_list = read_json(account_path)
transactions_list = read_json(transactions_path)
