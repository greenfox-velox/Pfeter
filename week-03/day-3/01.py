# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        circumference = self.radius * 2 * pi
        return(circumference)

    def get_area(self):
        area = self.radius ** 2 * pi
        return(area)

my_circle = Circle(20)
print(my_circle.get_circumference(), my_circle.get_area())
