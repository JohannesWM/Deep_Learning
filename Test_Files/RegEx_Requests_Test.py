import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36'

}  # Headers that allow get request to wesbite

website = "https://chewy.com"
webtxt = requests.get(website, headers=headers).text

all_found = re.finditer(r"[$]\d+\.\d{2}", webtxt)
found = re.search(r"\B\$\d+([.,]\d{2})", webtxt, flags=10)

print(found.group() + "\n", end="\n")

for _ in all_found:
    print(_)
