# Module for crawling the web to traverse Edgar.com; ticker leads to xml file of 13F

from urllib import request
from bs4 import BeautifulSoup as BS
import sys, random

prefix = 'https://www.sec.gov/'
# get ticker from command line — picks random static ticker if no comand line arg is given
def get_ticker():
    tickers = ['0001166559','0001040197' , '0001252007']
    return sys.argv[-1].strip() if len(sys.argv[1:]) else random.choice(tickers)

# Inputs ticker string, outputs BeautifulSoup html object of coresponding company page, displaying only 13 Forms
def get_company_page(ticker):
    ticker_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=13F' %(ticker)
    page = request.urlopen(ticker_url)
    return BS(page, "lxml")

# get company's name from page; return false if no company is found
def get_company_name (company_page):
    name = company_page.select('.companyName')
    return name[0].contents[0].strip() if len(name) else False

# inputs BeautifulSoup company page, outputs BeautifulSoup of filing page of the most recent 13F form
def get_filing_detail(company_page):
    filings = company_page.select('.blueRow')
    # Make sure at least one filing is present; if not, return False
    if len(filings):
        filing_page_url = prefix + filings[0].a.get('href')
        filing_page = request.urlopen(filing_page_url)
        return BS(filing_page, 'lxml')
    else:
        return False

# from filing page, get url of the 13F's xml page (return False if none is found just in case, though this may never apply)
def get_xml_url(filing_detail_page):
    for link in filing_detail_page.find_all('a'):
        text = link.text
        if text[-4:] == '.xml' and text[:-4] != 'primary_doc':
            return prefix+link.get('href')
    else:
        return False
