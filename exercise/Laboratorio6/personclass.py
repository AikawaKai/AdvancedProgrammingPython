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


if __name__ == '__main__':
    lectmark = [("Matematica1", 24), ("Matematica2", 27), ("Statistica", 30),
                ("Programmazione", 27), ("Sistemi Operativi", 27),
                ("Tecnocivismo", 28), ("Basi di dati", 23),
                ("Progr. funzionale", 25), ("ArchitetturaI", 25),
                ("ArchitetturaII", 24), ("Crittografia", 30),
                ("Linguaggi formali", 25), ("Prog. Software", 24),
                ("Fisica", 24), ("Reti Calcolatori", 26)]
    student = Student("Marco", "Odore", date(1985, 10, 27), lectmark)
    print(student.grade_average)
