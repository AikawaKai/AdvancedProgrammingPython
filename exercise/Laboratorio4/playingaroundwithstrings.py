import re


class string(str):

    def palindrom(self, other):
        lowerself = re.sub("[ ,.;:?!]", "", self.lower())
        other = re.sub("[ ,.;:?!]", "", other.lower())
        n = len(lowerself)
        if n != len(other):
            return False
        for i in range(n):
            if lowerself[i] != other[n-(i+1)]:
                return False
        return True


if __name__ == '__main__':
    mystring = string("Cia o")
    print(mystring.palindrom("o a.i:C"))  # True
    print(mystring.palindrom("o a.i:"))  # False
    print(mystring.palindrom("o a.i:CC"))  # False
    print(mystring.palindrom("o a.i:::C"))  # True
    profstring = string("Do geese see God?")
    print(profstring.palindrom("dog eese ,see .goD!"))  # True
    print(profstring.palindrom("dog eese ,seeD .goD!"))  # False
