from .Person import Person
from ..accounts.CheckingAccount import CheckingAccount

class Client(Person):


    def __init__(self, name, cpf, date, address):
        super().__init__(name, cpf, date)
        self.address = address

            
    def create_account(self, data):
        CheckingAccount(data)


    def __str__(self) -> str:
        return f"{super().name} - {super().cpf}"


    def to_dict(self):
        return {
            "name": super().name,
            "cpf": super().cpf,
        }
