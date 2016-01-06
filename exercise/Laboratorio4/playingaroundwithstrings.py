import re


class String(str):

    # classical way
    def palindrom(self):
        lowerself = re.sub("[ ,.;:?!]", "", self.lower())
        n = len(lowerself)
        for i in range(n):
            if lowerself[i] != lowerself[n-(i+1)]:
                return False
        return True

    # more compact
    def pythonicPalindrom(self):
        lowerself = re.sub("[ ,.;:?!]", "", self.lower())
        lowerReversed = lowerself[::-1]
        if lowerself == lowerReversed:
            return True
        else:
            return False

    # with iterator
    def iteratorPalindrom(self):
        lowerself = re.sub("[ ,.;:?!]", "", self.lower())
        iteratorReverse = reversed(lowerself)
        for char in lowerself:
            if next(iteratorReverse) != char:
                return False
        return True

if __name__ == '__main__':
    mystring = String("Do geese see God?")
    print(mystring.palindrom())  # True
    print(mystring.pythonicPalindrom())  # True
    print(mystring.iteratorPalindrom())  # True

    mystring = String("Do geese see Godd?")
    print(mystring.palindrom())  # False
    print(mystring.pythonicPalindrom())  # False
    print(mystring.iteratorPalindrom())  # False
