from unittest import TestCase
from unittest import main

converting_value = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


class OutOfRangeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def toRoman(number):
    string = ""
    if number >= 4000 or number <= 0:
        raise OutOfRangeError("out of range")
    for number1, roman in converting_value:
        while number >= number1:
            string += roman
            number -= number1
    return string


class RomanCaseTest(TestCase):

    know_values = ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'),
                   (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X'),
                   (50, 'L'), (100, 'C'), (400, 'CD'), (500, 'D'), (1000, 'M'),
                   (528, 'DXXVIII'), (1832, 'MDCCCXXXII'))

    def test_to_roman_know_values(self):
        for number, roman1 in self.know_values:
            roman2 = toRoman(number)
            self.assertEqual(roman1, roman2)

    def test_too_large(self):
        self.assertRaises(OutOfRangeError, toRoman, 4000)

    def test_equals_zero(self):
        self.assertRaises(OutOfRangeError, toRoman, 0)

    def test_no_negatives(self):
        self.assertRaises(OutOfRangeError, toRoman, -1)


if __name__ == '__main__':
    main()
