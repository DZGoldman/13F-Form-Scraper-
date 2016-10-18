# Main program - input cik or ticker from command line, create tab seperated txt from company's xml 13F filing
import os, sys
from funcs.scrape_funcs import *
from funcs.crawl_funcs import *


# get company page and extract name
company_page = get_company_page(ticker = get_ticker())
company_name = get_company_name(company_page)
# stop if ticker is invalid
if not company_name:
    sys.exit('Invalid ticker: company not found')

# Get page of filing details
filing_detail_page = get_filing_detail(company_page)
# stop if page has no 13 F filings
if not filing_detail_page:
    sys.exit('No 13F filings for company')
# extract url to xml file
url = get_xml_url(filing_detail_page)
# get root of xml tree
root = get_xml_root(url)
# create new file and save file path
new_file, file_path = make_new_file()
# write header:
new_file.write('13F Filing for %s\n \n' %(company_name)  )
# write rest of file using xml data
write_tab_text_file(root, new_file)
new_file.close()
# open newly created file
print('new file created!')
os.system('open ' + file_path)
