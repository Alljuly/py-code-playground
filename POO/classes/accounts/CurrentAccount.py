from transactions import WithDraw, Deposit 
from .. import Account 


class CurrentAccount(Account):
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
    