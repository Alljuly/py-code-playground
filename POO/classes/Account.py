class Account:

    def __init__(self, cpf, statement, balance, max_value, count):
        self.cpf = cpf
        self.statement = statement
        self.balance = balance
        self.max_value = max_value
        self.count = count

    def __str__(self) -> str:
        return f"{self.cpf} - {self.statement} - {self.balance} - {self.max_value} - {self.count}"

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "statement": self.statement,
            "balance": self.balance,
            "max_value": self.max_value,
            "count": self.count
        }

