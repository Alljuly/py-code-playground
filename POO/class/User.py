class User:

    def __init__(self, name, ID, password):
        self.name = name
        self.ID = ID
        self.password = password

    def __str__(self) -> str:
        return f"{self.name} - {self.ID} - {self.password}"


#def get_users(*objs):
#    for obj in objs:
#        print(obj)
#

a = User("Alice", "5656", 4542)

