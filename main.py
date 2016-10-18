import os, sys
from scrape_funcs import *
from crawl_funcs import *

from IPython import embed



company_page = get_company_page(ticker = get_ticker())

filing_detail_page = get_filing_detail(company_page)
if not filing_detail_page:
    sys.exit('No HR filings for company')
url = get_xml_url(filing_detail_page)
if not url:
    sys.exit('XML document not found')

# url = get_xml_url(ticker)
root = get_xml_root(url)
new_file, file_path = make_new_file()

write_tab_text_file(root, new_file)
new_file.close()

os.system('open ' + file_path)
