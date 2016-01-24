from functools import reduce


def cleaning(string):
    string = string.replace("\n", "")
    string = string.replace('""', "")
    return " "+" ".join(string.split())+" "


def prettyCSV(file):
    maxM = lambda x, y: y if len(y) > len(x) else x
    output = open(file, 'r')
    lines = [i.split(";") for i in output]
    regroup = [[cleaning(lines[i][j]) for i in range(len(lines))] for j in range(len(lines[0]))]
    maxSizeColumns = [len(reduce(maxM, regroup[i])) for i in range(len(regroup))]
    print(regroup, maxSizeColumns)
    newRegroup = [["{0:<{1}}".format(regroup[j][i], maxSizeColumns[j]) for j in range(len(regroup))] for i in range(len(regroup[0]))]
    newRegroup = [[newRegroup[i][j] for j in range(len(newRegroup[0]))] for i in range(len(newRegroup))]
    print("\n".join(["|"+"|".join(elem) for elem in newRegroup]))


if __name__ == '__main__':
    prettyCSV("books.csv")
