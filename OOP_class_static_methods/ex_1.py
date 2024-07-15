from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError:
            return "Can not divide to 0, please enter another sequence"


print(Calculator.add(4,5,6))
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2, 0))
print(Calculator.subtract(90, 20, -50, 43, 7))

