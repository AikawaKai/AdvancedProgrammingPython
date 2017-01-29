import types

def push(self, value):
    self.data.append(value)
    self.top+=1

def pop(self):
    to_ret = self.data[-1]
    self.data = self.data[:-1]
    self.top-=1
    return to_ret

def become(self, fun1, fun2):
    for fun in fun2:
        try:
            del self.__dict__[fun.__name__]
        except Exception as e:
            pass
    for fun in fun1:
        self.__dict__[fun.__name__] = types.MethodType(fun, self)

class skin(type):

    def __new__(meta, classname, supers, classdict):
        classdict["become"] = become
        return type.__new__(meta,  classname, supers, classdict)
