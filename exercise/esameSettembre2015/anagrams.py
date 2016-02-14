dictionary = {}


def anagrams():
    fileopen = open("wordlist-anagram.txt")
    lines = [line.strip() for line in fileopen]
    for line in lines:
        sortedline = "".join(sorted(list(line.lower())))
        if sortedline in dictionary:
            if line not in dictionary[sortedline]:
                dictionary[sortedline].append(line)
        else:
            dictionary[sortedline] = [line]
    new_dict = list(filter(lambda x: len(x[1]) > 2, dictionary.items()))
    new_dict = {lista[0]: ", ".join(lista[1:]) for word, lista in new_dict}
    new_dict = sorted(new_dict.items(), key=lambda x: x[0])

    print(len(new_dict))
    base = ""
    for key, value in new_dict:
        base += "{0:<15}:- {1}\n".format(key, value)
    return base

if __name__ == '__main__':
    print(anagrams())
