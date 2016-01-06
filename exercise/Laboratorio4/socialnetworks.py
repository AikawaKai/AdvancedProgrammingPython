class Nodo():

    def __init__(self, value, nodi):
        self.__value = value
        self.__adiacenti = nodi

    def addAdiacente(self, adiacente):
        self.add(adiacente)
        adiacente.add(self)

    def add(self, adiacente):
        self.__adiacenti.add(adiacente)

    def getValue(self):
        return self.__value

    def __str__(self):
        return "Nodo {0}, Adiacenti{1}".format(self.__value, [x.getValue() for x in self.__adiacenti])


class SocialNetwork():

    def __init__(self, firstNode):
        self._setOfNodes = set()
        self._setOfNodes.add(firstNode)

    def addAdiacenteToNode(self, node, adiacente):
        if node in self._setOfNodes:
            node.addAdiacente(adiacente)


if __name__ == '__main__':
    nodo1 = Nodo(1, set())
    nodo2 = Nodo(2, set())
    nodo3 = Nodo(3, set())
    nodo4 = Nodo(4, set())
    setdiprova = {nodo4, nodo2, nodo3}
    print(nodo1 in setdiprova)
    nodo1.addAdiacente(nodo2)
    print(str(nodo1), str(nodo2))
    social = SocialNetwork(nodo1)
    social.addAdiacenteToNode(nodo1, nodo3)
    print(str(nodo1), str(nodo3), str(nodo2))
