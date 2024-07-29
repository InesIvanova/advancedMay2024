class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError()
        self.__name = value

    def say_name(self):
        return "Hi"


class Teacher(Person):
    def say_name(self):
        raise Exception("not able to say name")




