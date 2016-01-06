import re


class String(str):

    # classical way
    def palindrom(self):
        lowerself = re.sub("[ ,.;:?!]", "", self.lower())
        n = len(lowerself)
        for i in range(n//2):
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
        for char in lowerself[0:len(lowerself)//2]:
            if next(iteratorReverse) != char:
                return False
        return True

    def subtract(self, other):
        return ''.join([x for x in self if x not in other])

    def anagram(self, other):
        if len(self) != len(other):
            return False
        selfCount = {x: self.count(x) for x in set(self)}
        otherCount = {x: other.count(x) for x in set(other)}
        if selfCount == otherCount:
            return True
        else:
            return False

    def anagramOfStringFromDictionary(self, dictionary):
        anagrams = [value for key, value in dictionary.items()
                    if self.anagram(value)]
        return anagrams

if __name__ == '__main__':
    mystring = String("Do geese see God?")
    print(mystring.palindrom())  # True
    print(mystring.pythonicPalindrom())  # True
    print(mystring.iteratorPalindrom())  # True

    mystring = String("Do gees see God?")
    print(mystring.palindrom())  # True
    print(mystring.pythonicPalindrom())  # True
    print(mystring.iteratorPalindrom())  # True

    mystring = String("Do geese see Godd?")
    print(mystring.palindrom())  # False
    print(mystring.pythonicPalindrom())  # False
    print(mystring.iteratorPalindrom())  # False

    mystring = String("Do gees see Godd?")
    print(mystring.palindrom())  # False
    print(mystring.pythonicPalindrom())  # False
    print(mystring.iteratorPalindrom())  # False

    mystring = String("Walter Cazzola")
    toSubtract = String("abcwxyz")
    print(mystring.subtract(toSubtract))

    string1 = String("ciao")
    string2 = String("caio")
    string3 = String("caioooo")
    string4 = String("aiocccco")
    string5 = String("oiacoccc")
    string6 = String("aioocccc")
    string7 = String("aicoccco")
    print(string1.anagram(string2))
    print(string1.anagram(string3))
    print(string1.anagram(string4))
    print(string4.anagram(string5))
    mydict = {0: string1, 1: string2, 2: string3, 3: string4, 4: string5,
              5: string6}
    print(string7.anagramOfStringFromDictionary(mydict))
