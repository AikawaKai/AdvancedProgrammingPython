def cleaning(string):
    return " ".join(string.split())

def generateWhiteSpaces(lenght):
    return "".join([" " for i in range(lenght)])

def formatting(line, token):
    indexT = line.index(token)
    listLine = list(line)
    whitespaces = generateWhiteSpaces(40-6-indexT)
    if indexT > 33:
        print("capita")
        diff = indexT - 33
        listLine = listLine[diff-1:]
        line = "".join(listLine)
        indexT = line.index(token)
        whitespaces = ""
    diff = (len(line) - indexT) -40
    if diff > 0:
        listLine = list(line)
        listLine = listLine[:-diff]
        line = "".join(listLine)
        indexT = line.index(token)
    return (line, whitespaces)

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
    lista1 = [[(token, num, line) for token in line.split()] for line, num in lista]
    #  print(lista1)
    basiclist = []
    for liste in lista1:
        basiclist += liste
    stopwords = ["and", "the"]
    filterLambda = lambda x:  len(x[0])>2 and x[0].lower() not in stopwords
    basiclist = list(filter(filterLambda, basiclist))
    basiclist = sorted(basiclist, key=lambda x: x[0].lower())
    basiclist = [(token, num, line, formatting(line, token)) for token, num, line in basiclist]
    for elem in basiclist:
        print("{0:>5} {1}{2}".format(elem[1], elem[3][1], elem[3][0]))
