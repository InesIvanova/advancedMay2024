from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "bark bark"


class Turtle(Animal):
    def make_sound(self):
        return "Turtle sound"


class Pig(Animal):
    def make_sound(self):
        return "Pig sound"


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog("Sharo"), Cat("Lady"), Turtle("Bob"), Pig("Pepa")]
animal_sound(animals)

