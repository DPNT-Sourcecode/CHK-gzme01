from unittest import TestCase

from lib.solutions.checkout import checkout


class CheckoutTestCase(TestCase):

    #     Our price table and offers:
    # +------+-------+------------------------+
    # | Item | Price | Special offers         |
    # +------+-------+------------------------+
    # | A    | 50    | 3A for 130, 5A for 200 |
    # | B    | 30    | 2B for 45              |
    # | C    | 20    |                        |
    # | D    | 15    |                        |
    # | E    | 40    | 2E get one B free      |
    # +------+-------+------------------------+

    # The total value of the price of the B type products
    # is now dependent on the total number of E type products purchased.
    # We _COULD_ apply deductions at the end of the calculations.

    # For every 3 A type products apply a cash reduction of 20.
    # For every 5 A type products apply a cash deduction of 50. The larger deduction takes
    # priority.

    # For every 2 E type products apply a deduction of 30 upto to the total count of the B
    # type products.

    def test_pricing_simple(self):
        self.assertEqual(checkout("ABC"), 50 + 30 + 20)
        self.assertEqual(checkout("ABD"), 50 + 30 + 15)
        self.assertEqual(checkout("EAD"), 40 + 50 + 15)

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
        self.assertEqual(checkout("EE B BBB"), 40 + 40 + 45 + 30)

    def test_illegal_input(self):
        self.assertEqual(checkout("a"), -1)
