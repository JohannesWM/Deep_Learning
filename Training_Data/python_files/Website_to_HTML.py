import requests
import re


def WebToHTML(website_link, file_name=None, header=None):
    if header is None:
        header = {"User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"}
    content = requests.get(website_link, headers=header).text

    with open(file_name, "w") as new_file:
        new_file.write(content)


def get_from_list():
    with open("../html_files/Websites.txt", "r") as link_file:
        links = link_file.readlines()

        for _ in links:
            print(_)
            name = re.search("\..*?\.", _)
            name = _[name.span()[0] + 1: name.span()[1] - 1]

            try:
                WebToHTML(_.replace("\n", ""), f"{name}.html")
            except Exception as e:
                print(e)


WebToHTML("https://www.asos.com/us/", file_name="../html_files/ASOS/asos.html")