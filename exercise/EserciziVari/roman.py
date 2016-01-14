from unittest import TestCase
from unittest import main

converting_value = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def toRoman(number):
    string = ""
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
            print(roman1, roman2)
            self.assertEqual(roman1, roman2)


if __name__ == '__main__':
    main()
