from math import pi
from math import sqrt

class shape:

    def calculate_area(self):pass

    def calculate_perimeter(self):pass

    def sortarea(listOfShapes):
        return sorted(listOfShapes, key=lambda x: x.calculate_area())

    def sortperim(listOfShapes):
        return sorted(listOfShapes, key=lambda x: x.calculate_perimeter())

class circle(shape):

    def __init__(self, raggio):
        self._raggio = raggio

    def calculate_area(self):
        return pi*self._raggio**2

    def calculate_perimeter(self):
        return 2*self._raggio*pi

    def __str__(self):
        return "Sono un cerchio! :((("


class rectangle(shape):

    def __init__(self,lato1,lato2):
        self._lato1 = lato1
        self._lato2 = lato2

    def calculate_area(self):
        return self._lato1 * self._lato2

    def calculate_perimeter(self):
        return (self._lato1*2) + (self._lato2*2)

    def __str__(self):
        return "I'm a rectangle"

class square(rectangle):

    def __init__(self,lato):
        self._lato = lato

    def calculate_area(self):
        return self._lato**2

    def calculate_perimeter(self):
        return self._lato * 4

    def __str__(str):
        return "Sono un quadrato!"


class triangoloeq(shape):

    def __init__(self,lato):
        self._lato = lato

    def calculate_area(self):
        return (sqrt(3))/4 * self._lato**2

    def calculate_perimeter(self):
        return self._lato*3

    def __str__(self):
        return "Sono un triangolo!"

class pentagons(shape):

    _nf = 0.688
    def __init__(self, lato):
        self._lato = lato

    def calculate_area (self):
        apotema = self._lato * pentagons._nf
        return (self.calculate_perimeter() * apotema)/2

    def calculate_perimeter(self):
        return self._lato * 5

    def __str__(self):
        return "sono un pentagono"
