# Helper functions, used in scrape.py
import urllib.request
from lxml import etree as ET
from IPython import embed


import sys, random, os
# get url to scrape data from; uses url from command line, or url from static list if none is given
def get_url():
    # get from command line
    if len(sys.argv[1:]):
        return sys.argv[-1]
    # otherwise, use one of these:
    else:
        urls = ['https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/a16-16809_1informationtable.xml'
            ,'https://www.sec.gov/Archives/edgar/data/1166559/000110465915038724/a15-11748_1informationtable.xml'
            ,'https://www.sec.gov/Archives/edgar/data/1600217/000160021716000001/table2016Q1.xml'
            ,'https://www.sec.gov/Archives/edgar/data/1600217/000160021716000001/table2016Q1.xml'
            ]
        return random.choice(urls)

# creates new file (gives new name/doesn't overwrite if file already exits)
def make_new_file():
    prefix = 'outputs/data_'
    suffix = 0
    possible_file_name = prefix + str(suffix) + '.txt'
    # update suffix until name is not yet taken
    while os.path.isfile(possible_file_name):
        suffix += 1
        possible_file_name = prefix + str(suffix) + '.txt'
    # return new file object and file name string:
    return open(possible_file_name, 'w') , possible_file_name

# translates common xml tags into more human readable / asthetically pleasing strings.
# Seperates other tags (that aren't statically translated) into capitalized, space seperated words:
def translate(tag):
    mapping = {'infoTable': 'Investment Holding',
            'cusip': 'CUSIP #',
            'shrsOrPrnAmt': 'Shares/Principal Amount',
            'sshPrnamt': 'SSH Principal Amount',
            'sshPrnamtType': 'SSH Principal Amount Type'
        }
    if tag in mapping:
         return mapping[tag]
    else:
        new_string = ''
        for char in (tag):
            new_string += ' '+char if char.isupper() else char
        return new_string[0].upper() + new_string[1:] if new_string else ''

# write text to file recursively - index level corresponds to call stack level for tab delineation
def write_text_file(root, new_file, index_level = 0):
    tab = '    '
    for child in root:
        # if namespace is part of tag string, ignore it
        bracket_index = child.tag.index('}')
        tag = child.tag if bracket_index == -1 else child.tag[bracket_index+1:]
        # strip new paragraph to prevent double line spacing
        info =  child.text.strip('\n').strip()
        # transalte xml tag into something more readable
        tag = translate(tag)
        # create line of text
        text = '{}{}: {} \n'.format(tab * index_level, tag, info )
        # add line break to highest level
        if index_level == 0:
            text = '\n'+text
        new_file.write(text)
        # recursively call on child nodes (with higher tab delineation)
        write_text_file(child, new_file, index_level+1)

def make_dictionary(node, dictionary = None):
    if not dictionary: dictionary = {}

    for child in node:
            # if namespace is part of tag string, ignore it
        bracket_index = child.tag.index('}')
        tag = child.tag if bracket_index == -1 else child.tag[bracket_index+1:]
        info =  child.text.strip('\n').strip()
        if info:
            dictionary[tag] = info
        make_dictionary(child, dictionary)
    return dictionary
def write_tab_text_file(root,new_file):
    # get tag order

    # create list of dictionaries
    all_listings = []

    for info_table in root:
        all_listings.append(make_dictionary(info_table))
    embed()

    # write to file one by one
def get_xml_root(url):
    result = urllib.request.urlopen(url)
    root = ET.fromstring(result.read())
    return root

def get_xml_root_2(url):
    result = urllib.request.urlopen(url)
    return result
