import re
import requests
import bs4
import itertools

"""

This block of code is for live scrapping however the html on "https://www.chewy.com/b/pharmacy-2515" has already been
stored inside (test_html/chewy_pharmacy_test.html).  This allows us to create a scraping algorithm without constantly
sending GET requests to "chewy.com";  Constant requests get the ip blacklisted.

----------------------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36'

}  # Headers that allow get request to wesbite

website = "https://www.chewy.com/b/pharmacy-2515"
webtxt = requests.get(website, headers=headers).text

try:
    with open("test_html/chewy_pharmacy_test.html", "w") as html_file:
        html_file.write(webtxt)
except Exception as e:
    print("unsuccesful")
    print(e)
    
----------------------------------------------------

"""

with open("test_html/chewy_pharmacy_test.html", "r") as html_file:
    webtxt = html_file.read()

# all_foundb = re.finditer(r"<div>(<\w+>\w+</\w+>)?\W+([a-zA-Z0-9]+|\s|[()\"\',-\.])+", webtxt)

within_div = re.compile(r"<div>.*?</div>")

within_div_list = re.finditer(within_div, webtxt)

# for _ in within_div_list:
#     print(webtxt[_.span()[0]:_.span()[1]])

div_list = [webtxt[_.span()[0]:_.span()[1]] for _ in within_div_list]

refined_list = []

for _ in div_list:
    if re.search("<!-- -->", _) is not None:
        refined_list.append(_)

print(refined_list)

