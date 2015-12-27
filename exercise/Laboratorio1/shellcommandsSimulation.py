import os
from stat import *
# print(os.listdir("./"))


def openAndGetFile(file):
    baseString = ""
    with open(file) as f:
        for line in f:
            baseString += line + "\n"
    return baseString


def cat(listOfFile):
    listOfFile = [fd for fd in listOfFile if S_ISDIR(os.stat(fd).st_mode) is False]
    stringList = map(openAndGetFile, listOfFile)
    for string in stringList:
        print(string)
    return None


def chmod(listOfFile, mode):
    for fd in listOfFile:
        filemode = os.stat(fd).st_mode
        os.chmod(fd, filemode | mode)
    return mode


def do_print(listOfLine):
    for line in listOfLine:
        print(line, end="")


def more(File):
    with open(File) as f:
        start = 0
        threshold = 30
        listOfLine = list(f)
        while start < len(listOfLine):
            currentList = listOfLine[start:threshold]
            do_print(currentList)
            input("PRESS ANY KEY")
            start = threshold
            threshold += 30
        # input("PRESS ANY KEY")


if __name__ == '__main__':
    listOfFile = os.listdir("./")
    cat(listOfFile)
    chmod(listOfFile, S_IXOTH)
    more("file.txt")
