from datetime import date


class Person(object):

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


class Student(Person):

    lectures = dict()

    def __init__(self, name, lastname, birthday, LectMarkTuples):
        super(Student, self).__init__(name, lastname, birthday)
        for lect, mark in LectMarkTuples:
            self.lectures[lect] = mark

    def _getAverageGrade(self):
        summark = 0
        for lect, mark in self.lectures.items():
            summark += mark
        return summark / len(self.lectures)

    grade_average = property(_getAverageGrade, None, None, "Average grade")


class Worker(Person):

    def __init__(self, name, lastname, date, pay_per_hour):
        super(Worker, self).__init__(name, lastname, date)
        self.pay_per_hour = pay_per_hour

    def _getSalaryDay(self):
        return self.pay_per_hour * 8

    def _getSalaryWeek(self):
        return self.day_salary * 5

    def _getSalaryMonth(self):
        return self.week_salary * 4

    def _getYearSalary(self):
        return self.month_salary * 12

    day_salary = property(_getSalaryDay, None, None, "get day salary")
    week_salary = property(_getSalaryWeek, None, None, "get week salary")
    month_salary = property(_getSalaryMonth, None, None, "get monthy salary")
    year_salary = property(_getYearSalary, None, None, "get year salary")


class Wizard(Person):

    def __init__(self, name, lastname, birthday):
        super(Wizard, self).__init__(name, lastname, birthday)

    def _getPassedDay(self):
        return 0

    def _setNewAge(self, date):
        self.birthday = date

    age = property(_getPassedDay, _setNewAge, None, "Magick aging")


if __name__ == '__main__':
    person = Person("Marco", "Odore", date(1985, 10, 27))
    sameperson = eval(repr(person))
    print(repr(person), repr(sameperson))
    lectmark = [("Matematica1", 24), ("Matematica2", 27), ("Statistica", 30),
                ("Programmazione", 27), ("Sistemi Operativi", 27),
                ("Tecnocivismo", 28), ("Basi di dati", 23),
                ("Progr. funzionale", 25), ("ArchitetturaI", 25),
                ("ArchitetturaII", 24), ("Crittografia", 30),
                ("Linguaggi formali", 25), ("Prog. Software", 24),
                ("Fisica", 24), ("Reti Calcolatori", 26)]
    student = Student("Marco", "Odore", date(1985, 10, 27), lectmark)
    print("Average grade: ", student.grade_average)
    worker = Worker("Marco", "Odore", date(1985, 10, 27), 8)
    print("day: ", worker.day_salary)
    print("week: ", worker.week_salary)
    print("month: ", worker.month_salary)
    print("year: ", worker.year_salary)
