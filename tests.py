import unittest
from funcs.scrape_funcs import *
from funcs.crawl_funcs import *

class Tests(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(translate(''), '')
        self.assertEqual(translate('infoTable'), 'Investment_Holding')
        self.assertEqual(translate('fooBarBar'), 'Foo_Bar_Bar')
    def test_no_hrs(self):
        for cik in ['000116399'  '0001639805','0001089052', '0001566375', 'PIH']:
            self.assertFalse(get_filing_detail(get_company_page(cik)))
    def test_get_name(self):
        self.assertEqual(get_company_name(get_company_page('0001166559')), 'BILL & MELINDA GATES FOUNDATION TRUST')
        self.assertEqual(get_company_name(get_company_page('0001566375')), 'Apple Seeds, LLC')
    def test_bad_ticker(self):
        for cik in ['12342', '', '543']:
            self.assertFalse(get_company_name(get_company_page(cik)))
unittest.main()
