def cleaning(string):
    return " ".join(string.split())


class IterFile(object):

    def __init__(self, fileToOpen):
        self.count = 1
        self.file = fileToOpen
        self.openedfile = open(fileToOpen, "r")
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        line = self.openedfile.readline()
        lineCouple = (line, self.count)
        if line == "":
            raise StopIteration
        self.cache.append(lineCouple)
        self.count +=1
        return lineCouple


if __name__ == '__main__':
    itera = IterFile("test.txt")
    lista = [(cleaning(elem[0]), elem[1]) for elem in itera]
    #  print(lista)
    lista1 = [[(str.lower(token), num, line) for token in line.split()] for line, num in lista]
    #  print(lista1)
    basiclist = []
    for liste in lista1:
        basiclist += liste
    print(basiclist)
    stopwords = ["and", "the"]
    filterLambda = lambda x:  len(x[0])<=2 or x[0] not in stopwords
    basiclist = list(filter(filterLambda, basiclist))
    basiclist = sorted(basiclist, key=lambda x: x[0])
    print(basiclist)
    for elem in basiclist:
        print("{0:>5} {1: ^50}".format(elem[1], elem[2]))
