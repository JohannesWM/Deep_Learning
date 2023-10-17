import requests
import re
import time
from random import randint

'''
The purpos of this file is to attempt to create algorithms that will scrape all given websites of their products.

To begin this process I will make individual functions for specific websites;  with the given information and knowledge
aquired from individual functions I will attempt to create a more robust function for scrapping the majority of these
websites (this function may have many inputs).

Inputs for universal fuctions may include but are not limited too:  specific links, class names, specific labels,
formatting styles...
'''

headers = {"User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"}

Warning_Text = "\033[4m\033[1m\033[93m"


# to be completed later current bugs include request.get() differing from website html and therefore scraping for proper
# links is near impossible
def scrape_ASOS():
    print(f"{Warning_Text}This function has not been completed: scrape_ASOS()")
    with open("../html_files/asos.html", "r") as asos_file:
        asos_as_txt = asos_file.read()
        a_tags = re.finditer("<a.*?>.*?</a>", asos_as_txt)

    a_tags_list = [asos_as_txt[_.span()[0]:_.span()[1]] for _ in a_tags]
    WM_page_list = [i for i in a_tags_list if re.search("id=\"women-floor\">WOMEN<", i) is not None or
                    re.search("id=\"men-floor\">MEN<", i) is not None]


def scrape_lowes():
    print(f"{Warning_Text}This function has not been completed: scrape_lowes()")
    with open("../html_files/Lowes/lowes.html", "r") as lowes_file:
        lowes_as_txt = lowes_file.read()
        a_tags = re.finditer("<a.*?>.*?</a>", lowes_as_txt)

    a_tags_list = [lowes_as_txt[_.span()[0]:_.span()[1]] for _ in a_tags]
    # for _ in a_tags_list:
    #     print(f"\033[0m{_}")
    SA_list = [i for i in a_tags_list if re.search("href=\".*?\"", i)]
    # for _ in SA_list:
    #     print(f"\033[0m{_}")

    # IL --> individual link
    IL_list = [re.search("href=\".*?\"", i) for i in SA_list]
    IL_list = [i.group() for i in IL_list]

    for i in IL_list:
        link = i.replace("href=", "").replace("\"", "")
        full_link = f"https://www.lowes.com{link}"

        print(full_link)
        html_page = requests.get(full_link, headers=headers).text
        link_form = link.replace("/", "DEV")

        with open(f"../html_files/Lowes/{link_form}.html", "w") as new_html_file:
            new_html_file.write(html_page)

        time.sleep(randint(1, 10))


scrape_lowes()
