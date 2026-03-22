# This test file tests is_valid_password() and is_valid_username() from main.py.
# It checks normal valid/invalid cases, edge cases like empty strings,
# special characters, spaces, and crash-causing inputs like None.

# Username with special chars like "dul!@" — should this be valid?
# Currently the function allows it which could be a bug
# "      1" is 7 chars, has a digit, has no letters — should be False



import unittest
from main import is_valid_password, is_valid_username

class TestIsValidPassword(unittest.TestCase):

    # Basic cases 
    def test_valid_password(self):
        self.assertTrue(is_valid_password("abc123"))

    def test_too_short(self):
        self.assertFalse(is_valid_password("ab1"))

    def test_no_digits(self):
        self.assertFalse(is_valid_password("abcdef"))

    def test_no_letters(self):
        self.assertFalse(is_valid_password("123456"))

    # Edge cases 
    def test_empty_string(self):
        self.assertFalse(is_valid_password(""))

    def test_spaces_and_digit(self):

        self.assertFalse(is_valid_password("      1"))

    def test_exactly_6_chars(self):
        self.assertTrue(is_valid_password("a1b2c3"))


class TestIsValidUsername(unittest.TestCase):


    def test_valid_username(self):
        self.assertTrue(is_valid_username("john"))

    def test_too_short(self):
        self.assertFalse(is_valid_username("ab"))

    def test_has_space(self):
        self.assertFalse(is_valid_username("my name"))


    def test_empty_string(self):
        self.assertFalse(is_valid_username(" "))

    def test_exactly_3_chars(self):
        self.assertTrue(is_valid_username("joe"))

    def test_special_characters(self):
        self.assertFalse(is_valid_username("dul!@"))


if __name__ == "__main__":
    unittest.main()

