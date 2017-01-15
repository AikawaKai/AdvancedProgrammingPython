from math import pi

class Shape(object):

    def area(self):
        pass

    def perimeter(self):
        pass

    def __lt__(self, other):
        return self.my_lt(other)

    def my_lt(self, other):
        return self.area() < self.other

class Rectangle(Shape):

    def __init__(self, lato1, lato2):
        self.lat1 = lato1
        self.lat2 = lato2

    def area(self):
        return self.lat1 * self.lat2

    def perimeter(self):
        return (self.lat1*2) + (self.lat2*2)


class Square(Rectangle):

    def __init__(self, lato1):
        super(Square, self).__init__(lato1, lato1)

class Circle(Shape):

    def __init__(self, ray):
        self.ray = ray

    def area(self):
        return self.ray**2*pi

    def perimeter(self):
        return self.ray * pi * 2
