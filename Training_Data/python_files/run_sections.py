import re
import bs4
import section_Labels as sbls
import os

for num_file in sorted(os.listdir("../html_files/ASOS")):
    print(num_file)
    sbls.split_into_tags(num_file.replace(".html", ""), f"../html_files/ASOS/{num_file}", "../Vector_Ready/ASOS/",
                         "article", None, identifier="asos_identifier")

