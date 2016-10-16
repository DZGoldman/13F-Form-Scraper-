import os
from scrape_funcs import *

from IPython import embed

# https://www.sec.gov/Archives/edgar/data/1600217/000160021716000001/table2016Q1.xml

# if a url is given, use it

def main():
    # url = get_url()
    # embed()

    url = get_url()

    root = get_xml_root(url)
    embed()
    new_file, file_path = make_new_file()


    write_tab_text_file(root, new_file)
    new_file.close()
    os.system('open ' + file_path)
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
