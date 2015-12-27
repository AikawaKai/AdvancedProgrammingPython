import re
stopwords = ["e", "o", "and", "or"]


def freqs(filetext, number):
    totaltext = ""
    with open(filetext) as f:
        for line in f:
            totaltext += "\n"+line
    totaltext = totaltext.lower()
    totaltext = re.sub("[,.:;}{]", " ", totaltext)
    words = [x for x in totaltext.split() if x not in stopwords]
    dictword = {x: 1 for x in words}
    for word in dictword:
        word_n = list(filter(lambda x: x == word, words))
        dictword[word] = len(word_n)
    filteredlist = sorted([w for w in dictword.items() if w[1] >= number], key=lambda x: x[1], reverse = True)
    print(filteredlist)


if __name__ == "__main__":
    freqs(input("\nInserisci il path del file di test: "), 10)
