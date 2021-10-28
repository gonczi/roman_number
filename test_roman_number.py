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

