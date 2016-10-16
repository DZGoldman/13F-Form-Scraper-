import unittest
from scrape_funcs import translate

class Tests(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(translate(''), '')
        self.assertEqual(translate('infoTable'), 'Information')
        self.assertEqual(translate('fooBarBar'), 'Foo Bar Bar')

unittest.main()
