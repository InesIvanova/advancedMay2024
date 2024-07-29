class A:
    def __init__(self, name):
        self.name = name


a = A("Test")
a2 = A("Test2")

print(id(a))
print(id(a2))