class User:

    def __init__(self, name, ID, password):
        self.name = name
        self.ID = ID
        self.password = password

    def __str__(self) -> str:
        return f"{self.name} - {self.ID} - {self.password}"

    def to_dict(self):
        return {
            "name": self.name,
            "ID": self.ID,
            "password": self.password
        }

