class Person:
   kind = "mammal"

   def __init__(self, name):
      self.name = name

   def greet(self):
      return "Hi"


class Student(Person):
   kind = 'mammal 2'

s = Student("Test")
print(s.kind)
print(Person.kind)