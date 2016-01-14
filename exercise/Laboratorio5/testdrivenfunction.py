import re
from unittest import TestCase
from unittest import main


def anagram(string):
    string = re.sub("[ .,:;?!]", "", string)
    string = string.lower()
    reversedstring = string[::-1]
    if reversedstring == string:
        return True
    else:
        return False


class CheckAnagram(TestCase):

    def testCheckTruePalindrom(self):
        self.assertEqual(True, anagram("Do geese see God?"))
        self.assertEqual(True, anagram("Rise to vote, sir."))

    def testCheckFalsePalindrom(self):
        self.assertEqual(False, anagram("Do geese seeee God?"))
        self.assertEqual(False, anagram("Rise to vote, sirasdas."))


if __name__ == '__main__':
    main()
