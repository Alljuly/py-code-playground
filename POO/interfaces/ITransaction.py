from abc import ABC, abstractmethod

class ITransaction(ABC):

    @abstractmethod
    def __init__(self, value):
        pass


    @abstractmethod
    def register(account):
        pass

    @abstractmethod
    def to_dict():
        pass
