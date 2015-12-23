import os
# print(os.listdir("./"))


def openAndGetFile(file):
    baseString = ""
    with open(file) as f:
        for line in f:
            baseString += line + "\n"
    return baseString


def cat(listOfFile):
    stringList = map(openAndGetFile, listOfFile)
    for string in stringList:
        print(string)
    return None

if __name__ == '__main__':
    listOfFile = os.listdir("./")
    cat(listOfFile)
