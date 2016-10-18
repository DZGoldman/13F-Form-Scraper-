# Module for extracting data from xml of 13F and writing it to a new text file
import urllib.request, os
from lxml import etree as ET


# request xml document from url, return root
def get_xml_root(url):
    result = urllib.request.urlopen(url)
    return ET.fromstring(result.read())

# creates new file (gives new name, i.e, doesn't overwrite if file already exits)
def make_new_file():
    prefix, suffix = 'outputs/data_', 0
    possible_file_name = prefix + str(suffix) + '.txt'
    # update suffix until name is not yet taken
    while os.path.isfile(possible_file_name):
        suffix += 1
        possible_file_name = prefix + str(suffix) + '.txt'
    # return new file object and file name string:
    return open(possible_file_name, 'w') , possible_file_name


# write text to inputed file
def write_tab_text_file(root,new_file):
    # get tag order
    column_names = get_column_names(root[0])
    # create first row (column names)
    tab = '     '
    for tag in column_names:
        new_file.write(translate(tag) + tab)
    new_file.write('\n')
    # create each other row (info tables flattened into single lines)
    for info_table in root:
        write_line(info_table, new_file)
        new_file.write('\n')

# used in write_tab_text_file: recursively write all tags in node to single line in file, seperated by tab
def write_line(node, new_file):
    tab = '     '
    for child in node:
        info =  child.text.strip('\n').strip()
        new_file.write(info  + tab)
        write_line(child, new_file)

# used in write_tab_text_file: get all column names by recursively searching through single info table:
def get_column_names(node, li = None):
    # initiate list to store column names
    if not li: li = []
    for child in node:
        # if namespace is part of tag string, ignore it
        bracket_index = child.tag.index('}')
        # get tag:
        tag = child.tag if bracket_index == -1 else child.tag[bracket_index+1:]
        li.append(tag)
        get_column_names(child, li)
    return li

# used in write_tab_text_file: translates common xml tags into more human readable / asthetically pleasing strings.
# Seperates other tags (that aren't statically translated) into capitalized, space seperated words:
def translate(tag):
    mapping = {'infoTable': 'Investment_Holding',
            'cusip': 'CUSIP #',
            'shrsOrPrnAmt': 'Shares/Principal_Amount',
            'sshPrnamt': 'SSH_Principal Amount',
            'sshPrnamtType': 'SSH_Principal_Amount_Type'
        }
    if tag in mapping:
         return mapping[tag]
    else:
        new_string = ''
        for i, char in enumerate(tag):
            new_string += '_'+char if char.isupper() else char if i>0 else char.lower()
        return new_string[0].upper() + new_string[1:] if new_string else ''
