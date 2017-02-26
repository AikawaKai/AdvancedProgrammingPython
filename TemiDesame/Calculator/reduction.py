import re


class Node():

    def __init__(self, fatherNode, value):
        self.father = fatherNode
        self.value = value
        self.left = None
        self.right = None

    def hasNotSons(self):
        if self.left is None and self.right is None:
            return True
        return False

    def hasOneSon(self):
        if self.left and self.right is None:
            return True
        return False


dict_operation = {"+": lambda x,y: x+y, "-": lambda x,y: x-y,
                  "/":lambda x,y: x/y, "*": lambda x,y: x*y}

class calculator():

    def __init__(self, string_):
        self.string = string_
        self.root = Node(None, string_[0])
        self._parsingExpr(self.root, string_[1:])

    def _parsingExpr(self, currentNode, string_):
        if len(string_)==0:
            return None
        if re.search("^[0-9]", string_):
            if currentNode.hasNotSons():
                currentNode.left = Node(currentNode, int(string_[0]))
                self._parsingExpr(currentNode, string_[1:])
            elif currentNode.hasOneSon():
                currentNode.right = Node(currentNode, int(string_[0]))
                self._parsingExpr(currentNode, string_[1:])
            else:
                self._parsingExpr(currentNode.father, string_)
        else:
            if currentNode.hasNotSons():
                currentNode.left = Node(currentNode, string_[0])
                self._parsingExpr(currentNode.left, string_[1:])
            elif currentNode.hasOneSon():
                currentNode.right = Node(currentNode, string_[0])
                self._parsingExpr(currentNode.right, string_[1:])
            else:
                self._parsingExpr(currentNode.father, string_)



def recstring(node):
    if type(node.value) is int:
        return str(node.value)
    else:
        return "("+recstring(node.left) + node.value + recstring(node.right)+")"




def print_reduction(calc):
    string_to_print = recstring(calc.root)
    print(string_to_print)
