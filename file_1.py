

class Animal:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Length must be at least 2 characters")
        self.__name = value

    def get_name(self):
        return f"smething from parent {self.name}"




class EntertaimantDevice:
    def __init__(self, name):
        self.name = name



class ElectronicCat(EntertaimantDevice, Animal):

    def some_method(self):
        self.get_name()

    def get_name(self):
        result = Animal.get_name(self)
        return f"Hello, {self.name} - {result}"


ea = ElectronicCat("Test")
print(ea.get_name())

