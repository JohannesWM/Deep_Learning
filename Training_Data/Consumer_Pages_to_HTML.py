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
