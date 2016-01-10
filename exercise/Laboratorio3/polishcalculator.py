
def add(elem):
    if len(elem) > 1:
        return elem[0]+elem[1]
    else:
        return elem


def sub(elem):
    if len(elem) > 1:
        return elem[0]-elem[1]
    else:
        return -elem


def prod(elem):
    return elem[0]*elem[1]


def div(elem):
    return elem[0]/elem[1]


def power(elem):
    return elem[0]**elem[1]


def orOp(elem):
    return elem[0] or elem[1]


def andOp(elem):
    return elem[0] and elem[1]


def notOp(elem):
    return not elem


listOfOper = {"+": add, "-": sub, "*": prod, "/": div, "**": power, "or": orOp,
              "and": andOp, "not": notOp}

dictBool = {"T": True, "F": False}


class PolishCalculator(object):

    def __init__(self, stringPolish):
        self.__string = stringPolish
        self.__val = PolishCalculator.eval(stringPolish)

    def __str__(self):
        stack = []
        listOfWords = self.__string.split()
        for word in listOfWords:
            if word not in listOfOper:
                stack.append(word)
            else:
                if len(stack) > 1:
                    elem = [stack.pop() for i in range(0, 2)]
                    stack.append("("+elem[0]+" "+word+" "+elem[1]+")")
                else:
                    elem = stack.pop()
                    stack.append(" "+word+"("+elem+")")
        return stack.pop()

    def getVal(self):
        return self.__val

    def eval(stringPolish):
        stack = []
        listOfWords = stringPolish.split()
        mapFloat = lambda x: float(x) if x not in dictBool and x not in listOfOper else x
        listOfWords = map(mapFloat, listOfWords)
        mapBool = lambda x: dictBool[x] if x in dictBool else x
        listOfWords = map(mapBool, listOfWords)
        for word in listOfWords:
            if word not in listOfOper:
                stack.append(word)
            else:
                if len(stack) > 1:
                    elem = [stack.pop() for i in range(0, 2)]
                    stack.append(listOfOper[word](elem))
                else:
                    elem = stack.pop()
                    stack.append(listOfOper[word](elem))
        return stack.pop()


if __name__ == '__main__':
    Polish = PolishCalculator("1 1 + 2 + 3 1 1 + 7 - 15 / * -")
    print(Polish.getVal())
    print(str(Polish))
    Polish = PolishCalculator("F F and not")
    print(Polish.getVal())
    print(str(Polish))
    Polish = PolishCalculator("3 4 + 5 *")
    print(Polish.getVal())
    print(str(Polish))
