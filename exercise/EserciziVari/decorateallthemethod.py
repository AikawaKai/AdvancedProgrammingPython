from types import FunctionType
import time


def timer(fun):
    def wrapper(*args, **kargs):
        start = time.time()
        result = fun(*args, **kargs)
        end = time.time()
        print("Executed in {0:.10} seconds".format(end-start))
        return result
    return wrapper


def metaclasswithdecorator(decorator):
    class decoraAllMethod(type):

        def __new__(meta, classname, supers, dictionary):
            for (key, value) in dictionary.items():
                if isinstance(value, FunctionType):
                    dictionary[key] = decorator(value)
            return type.__new__(meta, classname, supers, dictionary)
    return decoraAllMethod


class TestClass(metaclass=metaclasswithdecorator(timer)):

    def __init__(self, value):
        self.value = value

    def method1(self):
        print(self.value)

    def method2(self):
        print(self.value * 2)

    def method3(self):
        print(self.value ** 10000)

    def method4(self):
        print(pow(self.value, 10000))


if __name__ == '__main__':
    test = TestClass(5)
    test.method1()
    test.method2()
    test.method3()
    test.method4()
