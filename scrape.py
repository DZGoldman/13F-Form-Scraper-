import urllib.request, sys, random
# import xml.etree.ElementTree as ET
from lxml import etree as ET
from io import StringIO
from IPython import embed

# if a url is given, use it
def get_url():
    if len(sys.argv[1:]):
        return sys.argv[-1]
    # otherwise, use one of these:
    else:
        urls = ['https://www.sec.gov/Archives/edgar/data/1166559/000110465916139781/a16-16809_1informationtable.xml'
            ,'https://www.sec.gov/Archives/edgar/data/1166559/000110465915038724/a15-11748_1informationtable.xml'
            ]
        return random.choice(urls)

def main():
    url = get_url()

    result = urllib.request.urlopen(url)
    # embed()
    root = ET.fromstring(result.read())

    new_file = open('newb', 'w')

    make_text_file(root, new_file)
    new_file.close()

def make_text_file(root, new_file, index_level = 0):
    tab = '    '

    for child in root:
        print(child)
        bracket_index = child.tag.index('}')
        tag = child.tag if bracket_index == -1 else child.tag[bracket_index+1:]
        info = child.text
        new_file.write(tab*index_level + tag + ' ' + info)
        embed()
# get namespace?
# tag = root.tag
# if '{' in tag and '}' in tag:
#     ns = tag[tag.index('{') : tag.index('}') +1]
#     ns = {'infoTable': ns}
# s = ET.tostring(root)
# print(type(s))
# tree  = ET.ElementTree(root)
# ??????
# name_spaces = root.nsmap
# if None in name_spaces:
#     value = name_spaces[None]
#     name_spaces[''] = value
#     del name_spaces[None]
# print(name_spaces)
# print(root.findall('infoTable:Class', name_spaces))
# for child in root:
#     print (child)
# print(web.methods)
#tree.findall('{http://www.sec.gov/edgar/document/thirteenf/informationtable}infoTable')
# embed()
main()
