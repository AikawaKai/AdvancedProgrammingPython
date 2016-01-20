from datetime import date


def decorCounter(fun):
    fun.count = 0
    def wrapper(*args):
        fun.count += 1
        print("istanziato {0} volte".format(fun.count))
        return fun(*args)
    return wrapper


class Counter(type):
    def __new__(meta, classname, supers, classdict):
        init = classdict["__init__"]
        newinit = decorCounter(init)
        classdict["__init__"] = newinit
        return type.__new__(meta, classname, supers, classdict)


class Person(object, metaclass=Counter):

    def __init__(self, name, lastname, birthday):
        self.name = name
        self. lastname = lastname
        self.birthday = birthday

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getLastname(self):
        return self.lastname

    def setLastname(self, newlastname):
        self.lastname = newlastname

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, newbirthday):
        self.birthday = newbirthday

    def __repr__(self):
        return "Person('{0}', '{1}', date({2}, {3}, {4}))".format(self.name, self.lastname, self.birthday.year, self.birthday.month, self.birthday.day)


if __name__ == '__main__':
    Person("Marco", "Odore", date(1985, 10, 27))
    Person("Marco", "Odore", date(1985, 10, 27))
    Person("Marco", "Odore", date(1985, 10, 27))
