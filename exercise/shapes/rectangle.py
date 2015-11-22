import shape from shape

class rectangle(shape):

    def __init__(self,lato1,lato2):
        self._lato1 = lato1
        self._lato2 = lato2

    def calculate_area(self):
        return self._lato1 * self._lato2

    def calculate_perimeter(self):
        return (self.lato1*2) + (self.lato2*2)

    def __str__(self):
        return "I'm a rectangle"
