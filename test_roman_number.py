from unittest import TestCase

import roman_number

class TestParse(TestCase):
    def test_parse_empty_string(self):
        num = roman_number.parse("")
        self.assertEqual(num, -1)

    def test_parse_not_a_string(self):
        num = roman_number.parse(None)
        self.assertEqual(num, -1)

    def test_parse_not_a_roman_number(self):
        num = roman_number.parse("None")
        self.assertEqual(num, -1)

