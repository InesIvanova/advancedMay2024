import math
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Person name must be at least two chars")
        self.__name = value

    @abstractmethod
    def go_to_work(self):
        pass

    def greeting(self):
        return "Hello"


class Teacher(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if len(value) < 2 and value.startswith("a"):
            raise ValueError("Name is invalid")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary can not be negative")
        self.__salary = value

    def go_to_work(self):
        return "Going school"

    def eat(self):
        return "Eat at school"

    def greeting(self):
        return "Hello, kids!"



t = Teacher("aasd", 1000)
print(t.greeting())
print(math.pi)


