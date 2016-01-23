def cleaning(string):
    return " ".join(string.split())

def generateWhiteSpaces(lenght):
    return "".join([" " for i in range(lenght)])

def formatting(line, totalLenght):
    lineLenght= len(line)
    if totalLenght < 79:
        white = generateWhiteSpaces(79 - totalLenght)
        liststring = list(white)
        liststring[-1] = "."
        white = "".join(liststring)
        return line + white
    if totalLenght == 79:
        return line
    else:
        diff = totalLenght-79
        listline = list(line)
        return "".join(listline[:-diff])


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
    stopwords = ["and", "the"]
    filterLambda = lambda x:  len(x[0])<=2 or x[0] not in stopwords
    basiclist = list(filter(filterLambda, basiclist))
    basiclist = sorted(basiclist, key=lambda x: x[0])
    basiclist = [(token, num, line, line.lower().index(token)) for token, num, line in basiclist]
    basiclist = [(token, num, line, 40-6-index) for token, num, line, index in basiclist]
    basiclist = [(token, num, line, white, 6+white+len(line)) for token, num, line, white in basiclist]
    for elem in basiclist:
        print("{0:>5} {2}{1}".format(elem[1], formatting(elem[2], elem[4]), generateWhiteSpaces(elem[3])))
