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
