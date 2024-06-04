balance = 10

def withdrawal(value, balance):
    balance -= value
    print(f"Sacar {value}")
    return balance

def deposit(value,balance):
    balance += value
    print(f"Depositar {value}")
    return balance

def get_balance(balance):
    print(f"Balance: {balance}")

get_balance(balance)
balance = withdrawal(10, balance)
get_balance(balance)
balance = deposit(15,balance)
get_balance(balance)