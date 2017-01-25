

class A:

    def __init__(self, attr):
        self.my_attr = attr

    def __getattr__(self, name):
        if name == 'x_attr':
            return self.__dict__['my_attr']
        else:
            raise AttributeError("Value not returned")

if __name__ == '__main__':
    a = A("ciao")
    print(a.my_attr)
    print(a.x_attr)
    print(a.y_attr)
