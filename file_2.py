class Engine:
    def __init__(self, liters, type):
        self.liters = liters
        self.type = type


class Car:
    def __init__(self, model, type, engine):
        self.model = model
        self.type = type
        self.engine = engine


engine = Engine(1.3, "Benzin")
engine2 = Engine(1.6, "Disel TDI")

car = Car("Citroen", "Hetchbag", engine)
a = 5

