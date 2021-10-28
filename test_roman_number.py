from unittest import TestCase

import roman_number

class TestParse(TestCase):
    def test_parse_empty_string(self):
        num = roman_number.parse(" ")
        self.assertEqual(num, -1)

    def test_parse_not_a_string(self):
        num = roman_number.parse(None)
        self.assertEqual(num, -1)

    def test_parse_contains_roman_numbers_only(self):
        num = roman_number.parse("IICCCMMMX")
        self.assertNotEqual(num, -1)

    def test_parse_contains_roman_numbers_only_neg(self):
        num = roman_number.parse("IICCCMMMeX")
        self.assertEqual(num, -1)

    def test_parse_units(self):
        n = 1
        for unit in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']:
            num = roman_number.parse(unit)
            self.assertEqual(num, n)
            n = n + 1

    def test_parse_tens(self):
        n = 1
        for tens in ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']:
            num = roman_number.parse(tens)
            self.assertEqual(num, n * 10)
            n = n + 1

    def test_parse_hudreds(self):
        n = 1
        for tens in ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']:
            num = roman_number.parse(tens)
            self.assertEqual(num, n * 100)
            n = n + 1

    def test_parse_below_999(self):
        self.assertEqual(39, roman_number.parse("XXXIX"))
        self.assertEqual(246, roman_number.parse("CCXLVI"))
        self.assertEqual(789, roman_number.parse("DCCLXXXIX"))
