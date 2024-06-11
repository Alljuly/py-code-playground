class Account: 

    def __init__(self, data):
        self.statement = data.get('statement')
        self.number_acc = data.get('number')
        self.agency = data.get('agency')
        self.client = data.get('client')
  

    def to_dict(self):
        return {
            "client" : self.client,
            "number_account" : self.number_acc,
            "agency" : self.agency,
            "statement" : self.statement,
        }


    def __str__(self) -> str:
            return f"{self.number_account} - {self.agency} - {self.statement} - {self.client}"
  