

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
    print(a.my_attr) #attributo definito
    x.z_attr = 0 # attributo definito!!!!
    print(a.z_attr) # la get non passa da __getattr__ ,perché z_attr è definito!!!
    print(a.x_attr) # attributo non definito, che chiamo e basta
    print(a.y_attr)# attributo non definito, che chiamo e basta
