class Person:
    def __init__(self):
        self.__first_name = 'Peter'
        self.last_name = 'Parker'

    def __setattr__(self, key, value):
        self.__dict__[key] = value.upper()

    def _example(self):
        return "Hello"

    def __full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return self.__full_name()


person = Person()
print(person._Person__first_name)
print(getattr(person, "_Person__first_name"))


