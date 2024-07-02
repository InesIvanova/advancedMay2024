from typing import List


class Vehicle:
    a = 5
    def __init__(self, mileage: float, max_speed: int=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: List[str] = []


car = Vehicle(20, "some string")
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

