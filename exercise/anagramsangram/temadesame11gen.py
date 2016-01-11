diction = dict()


def anagrams():
    for key, value in diction.items():
        if value > 1:
            print("Parola: {0} anagrammi: {1}".format(key, value))


def anagram(word):
    if word in diction and diction[word] > 1:
        print("Parola: {0} anagrammi{1}".format(word, diction[word]))
    else:
        print("Nessun anagramma")


def initDict(file):
    f = open(file, 'r')
    for w in f.readlines():
        sw = sorted(w)
        if sw in diction:
            diction[sw] += w
        else:
            diction[sw] = list(w)


if __name__ == '__main__':
    initDict()
    anagrams()
