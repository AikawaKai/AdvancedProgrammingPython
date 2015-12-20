from shape import shape
from math import pi 


class circle(shape):

    def __init__(self, raggio):
        self._raggio = raggio

    def calculate_area(self):
        return pi*self._raggio**2

    def calculate_perimeter(self):
        return 2*self._raggio*pi

    def __str__(self):
        return "Sono un cerchio! :((("
