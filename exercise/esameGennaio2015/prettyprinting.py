from functools import reduce
import time


def timer(fun):
    def wrapper(*args):
        startTime = time.time()
        result = fun(*args)
        endTime = time.time()
        print("Function executed in {0} seconds".format(endTime-startTime))
        return result
    return wrapper


def cleaning(string):
    string = string.replace("\n", "")
    string = string.replace('""', "")
    string = string.replace('"', "")
    return " "+" ".join(string.split())+" "


@timer
def prettyCSV(file):
    maxM = lambda x, y: y if len(y) > len(x) else x
    output = open(file, 'r')
    lines = [i.split(";") for i in output]
    regroup = [[cleaning(lines[i][j]) for i in range(len(lines))] for j in range(len(lines[0]))]
    maxSizeColumns = [len(reduce(maxM, regroup[i])) for i in range(len(regroup))]
    sizeLine = sum(maxSizeColumns)+len(regroup)+1
    stringLine = "{0:-^{1}}".format("", sizeLine)
    newRegroup = [["{0:<{1}}".format(regroup[j][i], maxSizeColumns[j]) for j in range(len(regroup))] for i in range(len(regroup[0]))]
    newRegroup = [[newRegroup[i][j] for j in range(len(newRegroup[0]))] for i in range(len(newRegroup))]
    returnstring = "\n".join(["|"+"|".join(newRegroup[i])+"|" if i != 1 else stringLine for i in range(len(newRegroup))])
    return stringLine+"\n"+returnstring+"\n"+stringLine

if __name__ == '__main__':
    print(prettyCSV("books.csv"))
    print(prettyCSV("languages.csv"))
