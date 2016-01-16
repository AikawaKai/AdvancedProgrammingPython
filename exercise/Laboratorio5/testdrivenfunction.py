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

opposite = {'X': 'O', 'O': 'X'}


def checkvictory(string, elem):
    for pos1, pos2, pos3 in victoryposition:
        if string[pos1] == string[pos2] == string[pos3] == elem:
            return True


def validate(string):
    if not len(string) == 9 or abs(string.count('X') - string.count('O')) > 1:
        return (False, None)
    x = checkvictory(string, 'X')
    o = checkvictory(string, 'O')
    if x and o:
        return (False, None)
    elif x:
        return ('X', 'no moves') if string.count('O') <= string.count('X') else (False, None)
    elif o:
        return ('O', 'no moves') if string.count('X') <= string.count('O') else (False, None)
    if " " not in string:
        return (True, 'even')
    else:
        return (True, 'moves')


class CheckAnagram(TestCase):

    def testCheckTruePalindrom(self):
        self.assertEqual(True, anagram("Do geese see God?"))
        self.assertEqual(True, anagram("Rise to vote, sir."))

    def testCheckFalsePalindrom(self):
        self.assertEqual(False, anagram("Do geese seeee God?"))
        self.assertEqual(False, anagram("Rise to vote, sirasdas."))


class CheckValidate(TestCase):

    def testValidConfiguration(self):
        (winner, moves) = validate("XXXOOXOO ")
        self.assertEqual('X', winner)
        self.assertEqual('no moves', moves)
        (winner, moves) = validate("XO OXOXOX")
        self.assertEqual('X', winner)
        self.assertEqual('no moves', moves)
        (winner, moves) = validate("OOOXXOXX ")
        self.assertEqual('O', winner)
        self.assertEqual('no moves', moves)
        (winner, moves) = validate("OX XOXOXO")
        self.assertEqual('O', winner)
        self.assertEqual('no moves', moves)

    def testNonValidConfiguration(self):
        (winner, moves) = validate("XXXOOXOOOOO")
        self.assertEqual(False, winner)
        (winner, moves) = validate("XXXOOOOO")
        self.assertEqual(False, winner)
        (winner, moves) = validate("XXXOOOOO")
        self.assertEqual(False, winner)
        (winner, moves) = validate("XOOOXOXOX")
        self.assertEqual(False, winner)
        (winner, moves) = validate("O  XXXOOO")
        self.assertEqual(False, winner)
        (winner, moves) = validate("O  OOOXXX")
        self.assertEqual(False, winner)
        (winner, moves) = validate("OOOOXXX")
        self.assertEqual(False, winner)

    def testMovesConfiguration(self):
        (winner, moves) = validate("XOXOXXOXO")
        self.assertEqual(winner, True)
        self.assertEqual(moves, 'even')
        (winner, moves) = validate("XOXOO XXO")
        self.assertEqual(winner, True)
        self.assertEqual(moves, 'moves')


if __name__ == '__main__':
    main()
