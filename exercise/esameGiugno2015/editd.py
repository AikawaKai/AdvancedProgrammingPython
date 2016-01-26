import copy


def diff1(string1, string2):
    return True if sum([0 if list(string1)[i] == list(string2)[i] else 1 for i in range(len(string1))]) == 1 else False

listOfWords = [word for word in open("dizionario.txt", 'r').read().split()]


def chain(string1, string2):
    return chainr(string1, string2, listOfWords, [])


def chainr(string1, string2, listOfWords, lista):
    if string1 == string2:
        lista.append(string1)
        return lista
    listOfNext = [elem for elem in listOfWords if diff1(elem, string1)]
    listOfList = []
    for nextElem in listOfNext:
        newlist = copy.deepcopy(lista)
        newlist.append(string1)
        print(newlist)
        lWCp = copy.deepcopy(listOfWords)
        lWCp.remove(string1)
        listOfList.append(chainr(nextElem, string2, lWCp, newlist))
    return listOfList


if __name__ == '__main__':
    print(diff1("warring", "warning"))
    print(diff1("ciao", "ciaa"))
    print(diff1("ciao", "ciaa"))
    print(diff1("ziao", "ciaa"))
    print(diff1("ziao", "ciao"))
    print(diff1("ziao", "ciao"))
    print(chain("witness", "fatness"))
