import copy


def diff1(string1, string2):
    differ = sum([0 if list(string1)[i] == list(string2)[i] else 1 for i in range(len(string1))])
    if differ == 1:
        return True
    else:
        return False

listOfWords = [word for word in open("dizionario.txt")]

print(listOfWords)

if __name__ == '__main__':
    # print(diff1("warring", "warning"))
    # print(diff1("ciao", "ciaa"))
    # print(diff1("ciao", "ciaa"))
    # print(diff1("ziao", "ciaa"))
    # print(diff1("ziao", "ciao"))
    # print(diff1("ziao", "ciao"))
     chain("witness", "fatness")
