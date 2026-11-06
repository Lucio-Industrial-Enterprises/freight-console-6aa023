import unittest

from warehouse.quantity import parse_quantity


class ParseQuantityTests(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_trimmed(self):
        self.assertEqual(parse_quantity("  12  "), 12)

    def test_zero_is_valid(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")
