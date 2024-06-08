class User:

    def __init__(self, name, cpf, password):
        self.name = name
        self.cpf = cpf
        self.password = password

    def __str__(self) -> str:
        return f"{self.name} - {self.cpf} - {self.password}"

    def to_dict(self):
        return {
            "name": self.name,
            "cpf": self.cpf,
            "password": self.password
        }
