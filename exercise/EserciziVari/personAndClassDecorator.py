def classDecorator(cls):
    class Wrapper():

        def __init__(self, *args):
            self.fetches = 0
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print("Fetchs: ", name)
            self.fetches += 1
            return getattr(self.wrapped, name)
    return Wrapper



@classDecorator
class Person():

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    p = Person("Marco", 20, 40)
    print(p.name)
    print(p.pay())
    print(p.fetches)
    print(p.name)
    print(p.fetches)
