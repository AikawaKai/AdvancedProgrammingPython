import shape

if __name__ == '__main__':

    cerchio = shape.circle(10)
    pentagono = shape.pentagons(5)
    rettangolo = shape.rectangle(5,2)
    quadrato = shape.square(2)
    triangolo = shape.triangoloeq(3)
    listOfShapes = [cerchio, pentagono, rettangolo, quadrato, triangolo]
    print(listOfShapes)
    print(cerchio.calculate_area(), pentagono.calculate_area(), rettangolo.calculate_area(), quadrato.calculate_area(), triangolo.calculate_area())
    print([x.calculate_area() for x in  shape.shape.sortarea(listOfShapes)])
