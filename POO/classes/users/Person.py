from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, cpf, date):
        self._name = name
        self._cpf = cpf
        self._date = date

    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def date(self):
        return self._date

    def __str__(self) -> str:
        return f"Name: {self._name}, CPF: {self._cpf}, Date of Birth: {self._date}"