from unittest import TestCase

import utils


class TestUtils(TestCase):
    def test_validate_string(self):
        with self.subTest("Raises TypeError if type is not str"):
            with self.assertRaises(TypeError):
                utils.validate_string(42)
        with self.subTest("Raises ValueError if given an empty string"):
            with self.assertRaises(ValueError):
                utils.validate_string("")
        with self.subTest("Returns the given string if passes validation"):
            test_string: str = "Hello"
            self.assertEqual(test_string, utils.validate_string(test_string))
