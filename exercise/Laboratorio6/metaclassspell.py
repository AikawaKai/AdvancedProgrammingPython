from datetime import date

def getSalaryDay(self):
    return self.pay_per_hour * 8


def getSalaryWeek(self):
    return self.day_salary * 5


def getSalaryMonth(self):
    return self.week_salary * 4


def getYearSalary(self):
    return self.month_salary * 12


def addingArg(fun):
    def wrapper(*args):
        print(args)
        args[0].pay_per_hour = args[-1]
        return fun(*args)
    return wrapper


class Spell(type):

    def __new__(meta, classname, supers, classdict):
        classdict["pay_per_hour"] = 10
        classdict["day_salary"] = property(getSalaryDay, None, None, "day salary")
        classdict["week_salary"] = property(getSalaryWeek, None, None, "week salary")
        classdict["month_salary"] = property(getSalaryMonth, None, None, "month_salary")
        classdict["year_salary"] = property(getYearSalary, None, None, "year salary")
        return type.__new__(meta, classname, supers, classdict)


class Person(object, metaclass=Spell):

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
    person = Person("Marco", "Odore", date(1985, 10, 27))
    print(person.day_salary, person.week_salary, person.month_salary, person.year_salary)
