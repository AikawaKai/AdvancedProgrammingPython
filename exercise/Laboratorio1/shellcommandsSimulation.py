import os
import sys
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


def more(File):
    with open(File) as f:
        count = 0
        threshold = 30
        for line in f:
            count += 1
            if count <= threshold:
                print(line, end="")
            else:
                print("Threshold: {0}".format(threshold))
                threshold += 30
                sys.stdin.read(1)


if __name__ == '__main__':
    listOfFile = os.listdir("./")
    cat(listOfFile)
    chmod(listOfFile, S_IXOTH)
    more("file.txt")
