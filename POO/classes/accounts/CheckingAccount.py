from ..transactions.Transaction import WithDraw, Deposit 
from .Account import Account 
from datetime import date as dt
from typing import Dict

class CheckingAccount(Account):
    def __init__(self, limit, wd_limit, account: Dict[str, any]):
        super().__init__(account)
        self.limit = limit
        self.wd_limit = wd_limit
    

    def withdraw(self, value) -> float:
        wd = WithDraw(value)
        current_account_statement = super().statement

        statement = wd.register(current_account_statement)
        return statement


    def deposit(self, value) -> float:
        deposit = Deposit(value)
        current_account_statement = super().statement

        statement = deposit.register(current_account_statement)
        return statement


    def new_transaction(self, type_transaction, value):
        if type_transaction == "wd":
               transaction = WithDraw(value)
               transaction.register(self)
        elif type_transaction == "deposit":
               transaction = Deposit(value)
               transaction.register(self)

        current_balance = self.set_balance(type_transaction, value)
        return current_balance
    
    
    def limit_wd(self, balance) -> bool:
        count = 0
        date = dt.today()
        for t in balance:
            if t["type"] == "wd":
                if t["date"] == date:
                    count += 1
                if count == self.wd_limit:
                    return False
        return True
    

    def set_balance(self, type, value):
        date = dt.today().strftime('%Y-%m-%dT%H:%M:%S')
        balance = {"value": value, "date": date, "type": type}
        return balance
    

    def get_statement(self) -> str:
        statement = super().get_statement()
        return statement


    def limit_max(self, value) -> bool:
       return False if value > self.limit else True
    

    def to_dict(self):
        return {
            "client": self.client,
            "number_account": self.number_acc,
            "agency": self.agency,
            "statement": self.statement,
            "password": self.password,
            "limit": self.limit,
            "wd_limit": self.wd_limit
        }