
def stripArrayStrings(strings):
    return list(map(lambda x: x.strip(), strings))


def maxLenArrayStrings(strings):
    maxvalue = max(map(lambda x: len(x), strings))
    return list(map(lambda x: (x, maxvalue), strings))


def formattingTable(table):
    return [[" {0:{1}} ".format(line[0], line[1]) for line in row]
            for row in table]


def concatStringCsv(table, formattedString):
    if len(table) == 0:
        return formattedString + "\n"
    else:
        tempstring = "|"+"|".join(table[0])+"|"
        return concatStringCsv(table[1:], formattedString+"\n"+tempstring)


def prettyCSV(filecsv):
    file_open = open(filecsv, 'r')
    table = [stripArrayStrings(line.split(";")) for line in file_open]
    lenColumns = len(table[0])
    lenRows = len(table)
    TransposeTable = [[table[i][j] for i in range(lenRows)]
                      for j in range(lenColumns)]
    maxlentable = [maxLenArrayStrings(strings) for strings in TransposeTable]
    table = [[maxlentable[i][j] for i in range(lenColumns)]
             for j in range(lenRows)]
    totallen = sum([line[1] for line in table[0]]) + (lenColumns * 3) + 1
    table = formattingTable(table)
    separatorstring = "".join(["-" for i in range(totallen)])
    title = separatorstring+"\n|"+"|".join(table[0])+"|"+"\n"+separatorstring
    string = title + concatStringCsv(table[1:], "") + separatorstring
    return string

if __name__ == '__main__':
    print(prettyCSV("books.csv"))
    print(prettyCSV("languages.csv"))
