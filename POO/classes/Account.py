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
    

    #Novo __init__
    #O cliente é apenas um numero de cpf
    """
    def __init__(self, data):
        self.statement = data.get('statement')
        self.number_acc = data.get('number')
        self.agency = data.get('agency')
        self.client = data.get('client')
    """

    #Novo to_dict
    """
    def to_dict(self):
        return {
            "client" : self.client,
            "number_account" : self.number_acc,
            "agency" : self.agency,
            "statement" : self.statement,
        }

    """

    #Novo __str__
    """
    def __str__(self) -> str:
            return f"{self.number_account} - {self.agency} - {self.statement} - {self.client}"
    """
