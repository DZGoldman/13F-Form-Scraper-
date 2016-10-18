from urllib import request
from lxml import html
from bs4 import BeautifulSoup as BS
import sys, random
from IPython import embed

prefix = 'https://www.sec.gov/'

def get_ticker():
    tickers = ['0001166559']
    return sys.argv[-1].strip() if len(sys.argv[1:]) else random.choice(tickers)


def get_company_page(ticker):
    ticker_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=13F' %(ticker)
    page = request.urlopen(ticker_url)
    return BS(page, "html")

def get_filing_detail(company_page):
    filings = company_page.select('.blueRow')
    if len(filings):
        filing_page_url = prefix + filings[0].a.get('href')
        filing_page = request.urlopen(filing_page_url)
        return BS(filing_page)
    else:
        return False

def get_xml_url(filing_detail_page):
    for link in filing_detail_page.find_all('a'):
        text = link.text
        print(text)
        if text[-4:] == '.xml' and text[:-4] != 'primary_doc':
            return prefix+link.get('href')
    else:
        return False
