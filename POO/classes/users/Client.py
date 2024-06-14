from .Person import Person
from ..accounts.CheckingAccount import CheckingAccount

class Client(Person):


    def __init__(self, name, cpf, date, address):
        super().__init__(name, cpf, date)
        self.address = address

            
    def create_account(self, data):
        CheckingAccount(data)

    
    def __str__(self) -> str:
        return f"{self.name} - {self.cpf}"


    def to_dict(self):
        return {
            "name": self.name,
            "cpf": self.cpf,
            "date": self.date,
            "address": self.address
        }

    
    def __str__(self):
        return super().name

