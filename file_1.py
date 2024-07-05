class AgeNotValid(Exception):
    pass

class Person:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age


p = Person(18)
print(p.age)
p.age = -19
print(p.age)


class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value

red_car = Car(200)
red_car.drive()             # driving max speed 200
red_car.max_speed = 512     # changes the speed to 447
red_car.drive()             # driving max speed 447


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name must be at least 2 chars")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")
        self.__age = value



p = Person("test", -1)
print(p.__age)
p.__age = -2
print(p.age)
