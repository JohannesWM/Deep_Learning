import requests
import re
import bs4


'''
The purpos of this file is to attempt to create algorithms that will scrape all given websites of their products.

To begin this process I will make individual functions for specific websites;  with the given information and knowledge
aquired from individual functions I will attempt to create a more robust function for scrapping the majority of these
websites (this function may have many inputs).

Inputs for universal fuctions may include but are not limited too:  specific links, class names, specific labels,
formatting styles...
'''


def scrape_ASOS():
    with open("asos.html", "r") as asos_file:
        asos_as_txt = asos_file.read()
        a_tags = re.finditer("<a.*?>.*?</a>", asos_as_txt)

    a_tags_list = [asos_as_txt[_.span()[0]:_.span()[1]] for _ in a_tags]
    WM_page_list = [i for i in a_tags_list if re.search("id=\"women-floor\">WOMEN<", i) is not None or
                    re.search("id=\"men-floor\">MEN<", i) is not None]


scrape_ASOS()
