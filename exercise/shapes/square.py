import rectangle from rectangle

class square(rectangle):

    def __init__(self,lato):
        self._lato = lato

    def calculate_area(self):
        return self._lato**2

    def calculate_perimeter(self):
        return self._lato * 4

    def __str__(str):
        return "Sono un quadrato!"
