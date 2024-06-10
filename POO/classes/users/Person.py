from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, cpf, date):
        self._nome = name
        self._cpf = cpf
        self._date = date


    @property
    @abstractmethod
    def name(self):
        pass


    @property
    @abstractmethod
    def cpf(self):
        pass
   

    @property
    @abstractmethod
    def date(self):
        pass