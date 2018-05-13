from unittest import TestCase

from lib.solutions.hello import hello


class HelloFriendTestCase(TestCase):

    def test_hello(self):
        self.assertEqual(hello("John"), "Hello, John!")
        self.assertEqual(hello(""), "Hello, !")
