from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class FuturisticFactory(AbstractFactory):

    def create_chair(self):
        return Chair("Futuristic chair")

    def create_table(self):
        return Table("Futuristic table")

    def create_sofa(self):
        return Sofa("Futuristic sofa")


class VictorianFactory(AbstractFactory):

    def create_chair(self):
        return Chair("Victorian chair")

    def create_table(self):
        return Table("Victorian table")

    def create_sofa(self):
        return Sofa("Victorian sofa")