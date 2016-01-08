class Desc(object):
    '''descrittore'''

    def __init__(self, value=0.0):
        self.__value = value

    def __get__(self, instance, owner):
        print("Questa è l'istanza: {0}, questa è la classe: {1} ritorno self.__value".format(self, owner))
        return self.__value

    def __set__(self, instance, value):
        print("qui setto value")
        self.__value = float(value)

    def __delete__(self, instance):
        print("cancello l'istanza")


class ClasseConAttributo(object):

    attributo = Desc()

    def __init__(self, value):
        self.attributo = value

    def getNewValue(self):
        return self.newvalue

    def setNewValue(self, value):
        self.newvalue = value

    proprieta = property(getNewValue, setNewValue)


if __name__ == '__main__':
    istanza = ClasseConAttributo(10)
    risultato = istanza.attributo  # printa
    print(risultato)
    istanza.attributo = 5  # setto un nuovo valore
    new_risultato = istanza.attributo
    print(new_risultato)
    #  print("Prima di settare", istanza.getNewValue())  # dovrebbe dare vuoto
    istanza.setNewValue(15)
    print("Prima di settare", istanza.getNewValue())  # dovrebbe dare 15
