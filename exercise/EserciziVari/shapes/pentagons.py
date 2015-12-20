import shape from shape

class pentagons(shape):

_nf = 0.688

    def __init__(self, lato):
        self._lato = lato

    def calculate_area (self):
        apotema = self._lato * _nf
        return (self.calculate_perimeter() * apotema)/2

    def calculate_perimeter(self):
        return self._lato * 5

    def __str__(self):
        return "sono un pentagono"
