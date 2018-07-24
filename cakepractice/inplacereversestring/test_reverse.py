import unittest

from reverse import reverse

class TestReverse(unittest.TestCase):

    def test_nochars(self):
        self.assertEqual(reverse(''), '')

    def test_onechars(self):
        self.assertEqual(reverse('a'), 'a')

    def test_twochars(self):
        self.assertEqual(reverse('ab'), 'ba')

    def test_threechars(self):
        self.assertEqual(reverse('abc'), 'cba')

    def test_fourchars(self):
        self.assertEqual(reverse('abcd'), 'dcba')

    def test_fivechars(self):
        self.assertEqual(reverse('abcde'), 'edcba')
