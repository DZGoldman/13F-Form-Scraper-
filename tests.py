import unittest
from scrape_funcs import *
from crawl_funcs import *

class Tests(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(translate(''), '')
        self.assertEqual(translate('infoTable'), 'Investment_Holding')
        self.assertEqual(translate('fooBarBar'), 'Foo_Bar_Bar')
    def test_no_hrs(self):
        for cik in ['000116399'  '0001639805']:
            self.assertFalse(get_filing_detail(get_company_page(cik)))

unittest.main()
