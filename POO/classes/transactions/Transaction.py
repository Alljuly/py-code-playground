from interfaces.ITransaction import ITransaction

class Deposit(ITransaction):
    
    def __init__(self, value):
        self.value = value


    def register(self, account):
        account.statement += self.value
        return account.statement


class WithDraw(ITransaction):

    def __init__(self, value):
        self.value = value


    def register(self, account):
        account.statement -= self.value