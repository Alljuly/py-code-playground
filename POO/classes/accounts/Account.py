class Account: 

    def __init__(self, data):
        self.statement = data.get('statement')
        self.number_acc = data.get('number')
        self.agency = data.get('agency')
        self.client = data.get('client')
        self.password = data.get('password')
  

    def to_dict(self):
        return {
            "client" : self.client,
            "number_account" : self.number_acc,
            "agency" : self.agency,
            "statement" : self.statement,
            "password" : self.password,
        }


    def get_statement(self) -> float:
            return self.statement
  

    def __str__(self) -> str:
            return f"{self.number_account} - {self.agency} - {self.statement} - {self.client}"
  
    def __get_password__(self) -> str:
            return f'{self.password}'