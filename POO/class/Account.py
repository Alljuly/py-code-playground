account_list = [
    {
        "ID": "0",
        "statement": 10,
        "balance": [],
        "MAX_VALUE": 500,
        "count": 3
    }
]

class Account:

    def __init__(self, ID, statement, balance, MAX_VALUE, count):
        self.ID = ID
        self.statement = statement
        self.balance = balance
        self.MAX_VALUE = MAX_VALUE
        self.count = count

    def __str__(self) -> str:
        return f"{self.ID} - {self.statement} - {self.balance} - {self.MAX_VALUE} - {self.count}"




print(account)