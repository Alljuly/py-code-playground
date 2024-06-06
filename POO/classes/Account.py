class Account:

    def __init__(self, ID, statement, balance, MAX_VALUE, count):
        self.ID = ID
        self.statement = statement
        self.balance = balance
        self.MAX_VALUE = MAX_VALUE
        self.count = count

    def __str__(self) -> str:
        return f"{self.ID} - {self.statement} - {self.balance} - {self.MAX_VALUE} - {self.count}"

    def to_dict(self):
        return {
            "ID": self.ID,
            "statement": self.statement,
            "balance": self.balance,
            "MAX_VALUE": self.MAX_VALUE,
            "count": self.count
        }

