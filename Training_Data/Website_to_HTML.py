import requests
import re


def WebToHTML(website_link, file_name=None, header=None):
    if header is None:
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36'}
    content = requests.get(website_link, headers=header).text

    with open(file_name, "w") as new_file:
        new_file.write(content)


with open("Websites.txt", "r") as link_file:
    links = link_file.readlines()

    for _ in links:
        print(_)
        name = re.search("\..*?\.", _)
        name = _[name.span()[0] + 1: name.span()[1] - 1]

        try:
            WebToHTML(_.replace("\n",""), f"{name}.html")
        except Exception as e:
            print(e)
