from unittest import TestCase

from lib.solutions.checkout import checkout


class CheckoutTestCase(TestCase):

    # Going to have to modify all my test if it turns out that we have a different
    # method of getting SKUs

    # Notes.
    # A - 50, B - 30, C - 20, D - 15
    # AAA - 130, BB - 45

    def test_pricing_simple(self):
        self.assertEqual(checkout("ABC"), 50 + 30 + 20)
        self.assertEqual(checkout("ABD"), 50 + 30 + 15)

    def test_pricing_multi_A(self):
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AABA"), 130 + 30)
        self.assertEqual(checkout("BACDAA"), 130 + 30 + 20 + 15)

    def test_pricing_multi_B(self):
        self.assertEqual(checkout("BB"), 45)
        self.assertEqual(checkout("BBAD"), 45 + 50 + 15)
        self.assertEqual(checkout("BBAADA"), 45 + 130 + 15)
