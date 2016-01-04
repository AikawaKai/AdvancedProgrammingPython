from math import pi
from math import sqrt


class shape():

    def calculate_area():
        pass

    def calculate_perimeter():
        pass

    def ltarea(self, other):
        return self.calculate_area() < other.calculate_area()

    def ltperim(self, other):
        return self.calculate_perimeter() < other.calculate_perimeter()

    def sortedByArea(shapes):
        return sorted(shapes, key=lambda x: x.calculate_area())

    def sortedByPerim(shapes):
        return sorted(shapes, key=lambda x: x.calculate_perimeter())

    def nametype(self):
        return "shape"

    def __str__(self):
        return "{0}, area: {1}, perim: {2}".format(self.nametype(),
                                                   self.calculate_area(),
                                                   self.calculate_perimeter())


class rectangle(shape):
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2

    def calculate_area(self):
        return self.__side1 * self.__side2

    def calculate_perimeter(self):
        return (self.__side1 * 2) + (self.__side2 * 2)

    def nametype(self):
        return "rectangle"


class square(rectangle):
    def __init__(self, side):
        self._rectangle__side1 = side
        self._rectangle__side2 = side

    def nametype(self):
        return "square"


class equiTria(shape):
    def __init__(self, side, height):
        self.__side = side

    def calculate_area(self):
        self.__height = self.calculate_perimeter() / (2 * sqrt(3))
        return (self.__side * self.__height)/2

    def calculate_perimeter(self):
        return self.__side * 3

    def nametype(self):
        return "equiTria"


class circle(shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def nametype(self):
        return "circle"


class pentagon(shape):
    def __init__(self, side):
        self.__side = side
        self.__apothem = side * 0.688

    def calculate_perimeter(self):
        return self.__side * 5

    def calculate_area(self):
        return (self.calculate_perimeter() * self.__apothem) / 2

    def nametype(self):
        return "pentagon"


class hexagon(shape):
    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        self.__apothem = self.__side * 0.866
        return (self.calculate_perimeter() * self.__apothem) / 2

    def calculate_perimeter(self):
        return self.__side * 6

    def nametype(self):
        return "hexagon"


if __name__ == '__main__':
    rect = rectangle(2, 5)
    squa = square(2)
    tri = equiTria(2, 5)
    circ = circle(2)
    pent = pentagon(5)
    hexa = hexagon(3)
    listOfShapes = [rect, squa, hexa, tri, circ, pent]
    listOfShapessoretedbyArea = sorted(listOfShapes,
                                       key=lambda x: x.calculate_area())
    listOfShapessoretedbyPeri = sorted(listOfShapes,
                                       key=lambda x: x.calculate_perimeter())
    listOfShapessoretedbyArea2 = shape.sortedByArea(listOfShapes)
    listOfShapessoretedbyPeri2 = shape.sortedByPerim(listOfShapes)
    print("NOT SORTED")
    for shape in listOfShapes:
        print(str(shape))
    print("\nSORTED BY AREA")
    for shape in listOfShapessoretedbyArea:
        print(str(shape))
    print("\nSORTED BY PERIMETER")
    for shape in listOfShapessoretedbyPeri:
        print(str(shape))
    print("\nSORTED BY AREA v2")
    for shape in listOfShapessoretedbyArea2:
        print(str(shape))
    print("\nSORTED BY PERIMETER v2")
    for shape in listOfShapessoretedbyPeri2:
        print(str(shape))
