class Cook:
    def cut(self):
        pass

    def boil(self):
        pass

    def bake(self):
        pass


class Waiter:
    def take_order(self):
        pass

    def place_order(self):
        pass

    def deliver(self):
        pass


class Customer:
    def order(self):
        pass


    def eat(self):
        pass


class Restaurant:
    def __init__(self, cook, waiter):
        self.cook = cook
        self.waiter = waiter

    def welcome_customer(self, customer):
        customer.order()
        return self.waiter.place_order()

    def prepare_dish(self, ):
        self.cook.cut()
        self.cook.boil()



res = Restaurant(Cook(), Waiter())
c1 = Customer()

res.welcome_customer(c1)
res.prepare_dish()

