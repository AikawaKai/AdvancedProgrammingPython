
class Mydict(dict):

    def __init__(self):
        super(Mydict, self).__init__()
        self.__orderedPairs = []

    def __setitem__(self, key, value):
        super(Mydict, self).__setitem__(key, value)
        self.__orderedPairs.append((key, value))
        self.__orderedPairs = sorted(self.__orderedPairs, key=lambda x: x[0])

    def popitem(self):
        (x, y) = self.__orderedPairs.pop()
        super(Mydict, self).pop(x)
        return (x, y)

    def items(self):
        return self.__orderedPairs

    def __str__(self):
        stringFormat = lambda x: "'"+str(x)+"'" if isinstance(x, str) else str(x)
        listStringx = list(map(stringFormat, [x for x, y in self.__orderedPairs]))
        listStringy = list(map(stringFormat, [y for x, y in self.__orderedPairs]))
        listString = zip(listStringx, listStringy)
        return "{" + ", ".join([x+": "+y for x, y in listString]) + "}"

if __name__ == '__main__':
    miodictOld = dict()
    miodict = Mydict()
    miodict["cavallo"] = 1
    miodict["cane"] = 2
    miodict["gatto"] = 3
    miodict["topo"] = 4
    miodictOld["cavallo"] = 1
    miodictOld["cane"] = 2
    miodictOld["gatto"] = 3
    miodictOld["topo"] = 4
    print(miodict)
    print(miodictOld)
    #   pop: Mydict popitem the last (in order) element. Dict remove a random element
    print("Elemento estratto dal mio dict: {0}".format(miodict.popitem()))
    print("Elemento estratto dal default dict: {0}".format(miodictOld.popitem()))
    print(miodict, miodictOld)  # checks the values

    print(miodict.popitem())
    print(miodictOld.popitem())
    print(miodict)
    print(miodictOld)
