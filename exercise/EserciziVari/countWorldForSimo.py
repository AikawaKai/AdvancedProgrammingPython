dictionary = {"pippo": 0, "paperino": 0, "ciccio": 0, "ziopaperone": 0}


testo = ""


def firstWordArray(listOfWords):
    for i in range(len(listOfWords)):
        if listOfWords[i] in dictionary:
            return listOfWords[i:]

def countWords(listOfWords, word):
    if len(listOfWords) > 0:
        if listOfWords[0] in dictionary:
            countWords(listOfWords[1:], listOfWords[0])
        else:
            dictionary[word] += 1
            countWords(listOfWords[1:], word)


if __name__ == '__main__':
    listOfWords = testo.split()
    listOfWords = firstWordArray(listOfWords)
    print(listOfWords)
    countWords(listOfWords, listOfWords[0])
    print(dictionary)
