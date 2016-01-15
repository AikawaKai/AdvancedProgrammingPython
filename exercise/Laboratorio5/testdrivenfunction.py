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

victoryposition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                   (2, 5, 8), (0, 4, 8), (2, 4, 6))


def validate(string):
    if len(string) > 9 or abs(string.count('X') - string.count('O')) > 1:
        return (False, None, None)
    else:
        for pos1, pos2, pos3 in victoryposition:
            if string[pos1] == string[pos2] == string[pos3]:
                return (True, string[pos1], 'no moves')
        return (True, None, 'moves')


class CheckAnagram(TestCase):

    def testCheckTruePalindrom(self):
        self.assertEqual(True, anagram("Do geese see God?"))
        self.assertEqual(True, anagram("Rise to vote, sir."))

    def testCheckFalsePalindrom(self):
        self.assertEqual(False, anagram("Do geese seeee God?"))
        self.assertEqual(False, anagram("Rise to vote, sirasdas."))


class CheckValidate(TestCase):

    def testValidConfiguration(self):
        (correct, winner, moves) = validate("XXXOOXOO")
        self.assertEqual(True, correct)
        self.assertEqual('X', winner)
        self.assertEqual('no moves', moves)
        (correct, winner, moves) = validate("XO OXOXOX")
        self.assertEqual('X', winner)
        self.assertEqual('no moves', moves)
        (correct, winner, moves) = validate("OOOXXOXX")
        self.assertEqual(True, correct)
        self.assertEqual('O', winner)
        self.assertEqual('no moves', moves)
        (correct, winner, moves) = validate("OX XOXOXO")
        self.assertEqual('O', winner)
        self.assertEqual('no moves', moves)

    def testNonValidConfiguration(self):
        (correct, winner, moves) = validate("XXXOOXOOOOO")
        self.assertEqual(False, correct)
        (correct, winner, moves) = validate("XXXOOOOO")
        self.assertEqual(False, correct)
        (correct, winner, moves) = validate("XXXOOOOO")
        self.assertEqual(False, correct)

    def testNoMovesConfiguration(self):
        pass

if __name__ == '__main__':
    main()
