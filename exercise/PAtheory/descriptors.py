class Descriptor(object):



    def __get__(self, obj, cls):
        print("{0}.__get__({1}, {2})".format(self, obj, cls))
        print(self.content, obj.do_something(), cls.color)

    def __set__(self, obj, val):
        print("{0}.__set__({1}, {2})".format(self, obj, val))

    def __delete__(self, obj):
        print("{0}.__delete__({1})".format(self, obj))


class C(object):
    d = Descriptor()
    color = "red"
    d.content = "content"

    def do_something(self):
        print("I'm doing something")
        return "something"

if __name__ == '__main__':
    c = C()
    c.d
    c.d = "ciao"
