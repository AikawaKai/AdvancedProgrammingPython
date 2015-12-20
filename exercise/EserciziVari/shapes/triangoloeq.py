import shape from shape

class triangoloeq(shape):

    def __init__(self,lato):
        self._lato = lato

    def calculate_area(self):
        return (sqrt(3))/4 * lato**2

    def calculate_perimeter(self):
        return lato*3

    def __str__(self):
        return "Sono un triangolo!"
