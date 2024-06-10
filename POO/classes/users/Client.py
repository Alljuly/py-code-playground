import Person

class Client(Person):

    def __init__(self, name, cpf, date):
        super().__init__(name, cpf, date)


    """def new_transaction(self, type_transaction, value):
        transaction = Transaction(type_transaction)
        transaction.register(value)"""


    """def create_account(self, data):
        new_account = Account(data)
    """