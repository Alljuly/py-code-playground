from interfaces.ITransaction import ITransaction

class Deposit(ITransaction):
    
    def __init__(self, value):
        self.value = value


    def register(self, account):
        account.statement += self.value
        return account.statement
    

    def to_dict(self, account):
        return account.statement


class WithDraw(ITransaction):

    def __init__(self, value):
        self.value = value


    def register(self, account):
        account.statement -= self.value

    
    def to_dict(self, account):
        return account.statement
