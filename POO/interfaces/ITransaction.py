"""
from abc import ABC, abstractmethod

class ITransaction(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def register(account):
        pass

"""