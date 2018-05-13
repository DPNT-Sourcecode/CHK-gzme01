from unittest import TestCase

from lib.solutions.checkout import checkout


class CheckoutTestCase(TestCase):

    # Our price table and offers:
    # +------+-------+------------------------+
    # | Item | Price | Special offers         |
    # +------+-------+------------------------+
    # | A    | 50    | 3A for 130, 5A for 200 |
    # | B    | 30    | 2B for 45              |
    # | C    | 20    |                        |
    # | D    | 15    |                        |
    # | E    | 40    | 2E get one B free      |
    # | F    | 10    | 2F get one F free      |
    # +------+-------+------------------------+

    # The introduction of this offer does not change our code too much

    def test_pricing_simple(self):
        self.assertEqual(checkout("ABC"), 50 + 30 + 20)
        self.assertEqual(checkout("ABD"), 50 + 30 + 15)
        self.assertEqual(checkout("EAD"), 40 + 50 + 15)
        self.assertEqual

    def test_pricing_multi_A(self):
        self.assertEqual(checkout("AAA"), 130)
        self.assertEqual(checkout("AABA"), 130 + 30)
        self.assertEqual(checkout("BACDAA"), 130 + 30 + 20 + 15)
        self.assertEqual(checkout("AAAAA"), 200)
        self.assertEqual(checkout("AAAAAAAAAA"), 400)
        self.assertEqual(checkout("AAAAAAAAAAAAA"), 530)

    def test_pricing_multi_B(self):
        self.assertEqual(checkout("BB"), 45)
        self.assertEqual(checkout("BBAD"), 45 + 50 + 15)
        self.assertEqual(checkout("BBAADA"), 45 + 130 + 15)

    def test_pricing_free_B(self):
        # We need to test that we don't get more than the number of B that are in the checkout
        self.assertEqual(checkout("EEB"), 40 + 40)
        self.assertEqual(checkout("EE"), 40 + 40)
        self.assertEqual(checkout("EEEEEEB"), 40 * 6)
        self.assertEqual(checkout("EEBB"), 40 + 40 + 30)
        self.assertEqual(checkout("EEBBBB"), 40 + 40 + 45 + 30)

    # def test_free_F(self):
    #     self.assertEqual(checkout("FFF"), 10 + 10 + 10 - 10)
    #     self.assertEqual(checkout("FF"), 10 + 10)
    #     self.assertEqual(checkout("FFFF"), 40 - 10)
    #     self.assertEqual(checkout("FFFFFF"), 60 - 20)
    #     self.assertEqual(checkout("AABDFFFF"), 50 + 50 + 30 + 15 + 40 - 10)

    def test_illegal_input(self):
        self.assertEqual(checkout("a"), -1)
