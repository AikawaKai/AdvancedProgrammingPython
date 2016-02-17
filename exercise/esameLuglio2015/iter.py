import re


def getWordsFromRawLine(line):
    line = line.strip()
    words = re.split('\W', line)
    return list(filter(lambda x: len(x) > 0, words))


class UpDownFile():

    def __init__(self, filetoopen):
        self.file = open(filetoopen, 'r')
        self.index = 0
        self.cache = []
        self.len = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == self.len:
            words = []
            while len(words) == 0:
                curline = self.file.readline()
                if curline == "":
                    raise StopIteration
                words = getWordsFromRawLine(curline)
            self.cache += words
            self.len += len(words)
        toReturn = self.cache[self.index]
        self.index += 1
        return toReturn

    def ungetw(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1


if __name__ == '__main__':
    prova = "ciao. sono, marco?[] come,; va? "
    words = re.split("\W+", prova)
    print(list(filter(lambda x: len(x) > 0, words)))
    fileo = open("text.txt", 'r')
    while fileo.readline():
        print("yes")
