from ..transactions.Transaction import WithDraw, Deposit 
from .Account import Account 
from datetime import date as dt
from typing import Dict

class CheckingAccount(Account):
    def __init__(self, limit, wd_limit, account: Dict[str, any]):
        super().__init__(account)
        self.limit = limit
        self.wd_limit = wd_limit
    

    def limit_value(self, value) -> bool:
        return value < self.statement and value < self.limit


    def new_transaction(self, type_transaction, value:float):

        if type_transaction == "wd":
            if self.statement >= value:
                transaction = WithDraw(value)
                transaction.register(self)
        elif type_transaction == "deposit":
            transaction = Deposit(value)
            transaction.register(self)
           
        transaction_dict = transaction.to_dict(self)
        current_balance = self.set_balance(type_transaction, value)
        return [current_balance, transaction_dict]

     

    def limit_wd(self, balance) -> bool:
        count = 0
        date = dt.today().strftime('%Y-%m-%d')
        for t in balance:
            if t["client"] == self.client and t["type"] == "wd":
                if t["date"] == date:
                    count += 1
                if count == self.wd_limit:
                    return False
        return True
    

    def set_balance(self, type, value):
        date = dt.today().strftime('%Y-%m-%d')
        balance = {"value": value, "date": date, "type": type, "client": self.client}
        return balance
    

    def get_statement(self) -> str:
        statement = super().get_statement()
        return statement
    

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