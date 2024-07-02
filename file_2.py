class Person:
    def __init__(self, age):
        self.age = age

    def happy_birthday(self):
        self.age += 1

p1 = Person(10)
p2 = Person(30)
print(p1.age)
print(p1.happy_birthday())
print(p1.age)
