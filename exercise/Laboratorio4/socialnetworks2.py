class Nodo():

    def __init__(self, value):
        self.__value = value
        self.__adiacenti = set()

    def addAdiacente(self, adiacente):
        self.add(adiacente)
        adiacente.add(self)

    def add(self, adiacente):
        self.__adiacenti.add(adiacente)

    def getDegree(self):
        return len(self.__adiacenti)

    def getValue(self):
        return self.__value

    def getAdiacenti(self):
        return self.__adiacenti

    def __str__(self):
        return "Nodo {0}, Adiacenti{1}".format(self.__value,
                                               [x.getValue()
                                                for x in self.__adiacenti])


class SocialNetwork():

    def __init__(self, firstNode):
        self._setOfNodes = set()
        self._firstnode = firstNode
        self._setOfNodes.add(firstNode)

    def visitAll(self):
        iterVisit = Visit(self._firstnode)
        breadth_first_nodes = []
        for nod in iterVisit:
            breadth_first_nodes.append(nod)
        return breadth_first_nodes

    def __str__(self):
        nodes = self.visitAll()
        base = ""
        for nod in nodes:
            base += "\nnodo {0}, adiacenti {1}".format(nod.getValue(),
                                                       [ad.getValue() for ad
                                                       in nod.getAdiacenti()])
        return base


# visita in ampiezza
class Visit():
    def __init__(self, seed):
        self.__seed = seed

    def __iter__(self):
        currentNode = self.__seed
        self.__toVisit = []
        self.__index = 0
        self.__toVisit.append(currentNode)
        self.__visited = set()
        return self

    def __next__(self):
        if self.__index >= len(self.__toVisit):
            raise StopIteration
        currentNode = self.__toVisit[self.__index]
        if currentNode.getDegree() > 0:
            adiacenti = currentNode.getAdiacenti()
            self.__visited.add(currentNode)
            adiacentiNotVisited = [nod for nod in adiacenti if nod not in
                                   self.__visited and nod not in
                                   self.__toVisit]
            self.__toVisit.extend(adiacentiNotVisited)
            self.__index += 1
        else:
            self.__visited.add(currentNode)
            self.__index += 1
        return currentNode


if __name__ == '__main__':
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)
    nodo1.addAdiacente(nodo2)
    nodo1.addAdiacente(nodo3)
    nodo3.addAdiacente(nodo2)
    nodo3.addAdiacente(nodo4)
    nodo5.addAdiacente(nodo3)
    nodo5.addAdiacente(nodo2)
    social = SocialNetwork(nodo1)
    social.visitAll()
    print(str(social))
