from transactions import WithDraw, Deposit 
from . import Account 

class CheckingAccount(Account):
    def __init__(self, limit, wd_limit, account):
        super().__init__(account)
        self.limit = limit
        self.wd_limit = wd_limit
    

    def withdraw(self, value):
        wd = WithDraw(value)
        current_account_statement = super().statement

        wd.register(current_account_statement)


    def deposit(self, value):
        deposit = Deposit(value)
        current_account_statement = super().statement

        deposit.register(current_account_statement)


    def new_transaction(self, type_transaction, value):
           if type_transaction == "wd":
               transaction = WithDraw(value)
               transaction.register(self)
           elif type_transaction == "deposit":
               transaction = Deposit(value)
               transaction.register(self)

    
    def limit_wd(self, balance, date):
        count = 0
        for t in balance:
            if t["type"] == "wd":
                if t["date"] == date:
                    count += 1
                if count == self.wd_limit:
                    return False
        return True
    

    def limit_max(self, value):
       return False if value > self.limit else True
    