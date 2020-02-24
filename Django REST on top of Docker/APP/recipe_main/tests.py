from django.test import TestCase
from .calc import sum

class Test(TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(sum(1,2), 4)