from unittest import TestCase
from unittest import main
import re

converting_value = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

matchingregex = re.compile('''
                           ^
                           M{0,3}
                           (CM|CD|D?C{0,3})
                           (XC|XL|L?X{0,3})
                           (IX|IV|V?I{0,3})
                           $''', re.VERBOSE)


class OutOfRangeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidRomanNumeralError(Exception):

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


def fromRoman(roman):
    if not matchingregex.search(roman):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(roman))
    index = 0
    result = 0
    for number, roman1 in converting_value:
        while roman[index:index+len(roman1)] == roman1:
            result += number
            index += len(roman1)
    return result


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

    def test_from_roman_know_values(self):
        for number, roman in self.know_values:
            number1 = fromRoman(roman)
            print(number1, number)
            self.assertEqual(number, number1)

    def test_roundtrip(self):
        for number, roman in self.know_values:
            roman1 = toRoman(number)
            number1 = fromRoman(roman1)
            self.assertEqual(number, number1)

    def test_bad_input(self):
        self.assertRaises(InvalidRomanNumeralError, fromRoman, 'XXXX')
        self.assertRaises(InvalidRomanNumeralError, fromRoman, 'VVV')
        self.assertRaises(InvalidRomanNumeralError, fromRoman, 'MMMMX')
        self.assertRaises(InvalidRomanNumeralError, fromRoman, 'VIIII')
        self.assertRaises(InvalidRomanNumeralError, fromRoman, 'XLXL')


if __name__ == '__main__':
    main()
