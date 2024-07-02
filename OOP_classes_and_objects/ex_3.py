pi = 3.14
class Circle:
    # pi = 3.14
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        return self.pi * self.radius ** 2

    def get_circumference(self) -> float:
        return 2 * self.radius * self.pi


print(Circle.pi)
circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())





