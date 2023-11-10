import re
import sys
import os
import section_Labels
import bs4

'''
split_into_tags()
     - directory_path
          - This is directory where all of the html tag slices will be stored
          - must end with /
     - split_by
          - This is the tag that each section should be <a>...</a>, <div>...</div>, etc.
     - identifier
          - Just the string name of the function no ()
          - to run the indentifier_func use () ex. identifier_func()
          - This is a function name that should return a Boolean, so that split_into_tags() can label the slice either
          product or not-product (each directory_path will should have a Product and NotProduct folders within it here
          the different slices will be placed)
'''


def split_into_tags(file_name, html_file_path, directory_path, split_by, class_info, identifier=None, once_p=False,
                    alltag_can_product=False, file_type="txt"):
    if identifier is None:
        sys.exit()
    identifier_func = getattr(section_Labels, identifier)

    with open(html_file_path, "r") as html_file:
        html_text = html_file.read()

    soup = bs4.BeautifulSoup(html_text, "html.parser")

    if class_info is not None:
        split_into_products = soup.find_all(split_by, class_=class_info)  # all products
    else:
        split_into_products = soup.find(split_by)  # all of a tag

    split_into = soup.find_all(split_by)  # split by tag, this is all from tag to tag

    it_num = 0

    # Directory
    directory_yes = "cp"
    directory_no = "np"

    # Path
    path_yes = os.path.join(directory_path, directory_yes)
    path_no = os.path.join(directory_path, directory_no)

    if os.path.isdir(path_yes) and os.path.isdir(path_no):
        pass
    elif not os.path.isdir(path_yes) and not os.path.isdir(path_no):
        os.mkdir(path_yes)
        os.mkdir(path_no)
    else:
        return Exception("ERROR OCCURED WHILE CHECKING FOR DIRECTORIES")

    # These are all the non_products being placed into non_product directory
    for split_text in split_into:

        split_text = str(split_text)

        if identifier_func(split_text) and alltag_can_product:  # these are all product split sections
            with open(f"{directory_path}cp/{file_name}_{it_num}.{file_type}", "w") as cp_file:
                cp_file.write(split_text)
        else:  # these are all the not product split sections
            with open(f"{directory_path}np/{file_name}_{it_num}.{file_type}", "w") as np_file:
                np_file.write(split_text)

        it_num += 1

    # These are all products being placed into their own
    for split_text in split_into_products:

        split_text = str(split_text)

        if identifier_func(split_text):  # these are all product split sections
            with open(f"{directory_path}cp/{file_name}_{it_num}.{file_type}", "w") as cp_file:
                cp_file.write(split_text)
        elif once_p:  # these are all the not product split sections from the once products
            with open(f"{directory_path}np/{file_name}_{it_num}.{file_type}", "w") as np_file:
                np_file.write(split_text)
        else:
            pass

        it_num += 1


def chewy_identifier(text):
    if re.search("<!-- -->", text) is not None and re.search("kib-product-card ProductListing_kibProductCard__Oo6zy "
                                                             "js-tracked-product Product"
                                                             "Listing_productControl__yX_4p", text) is not None:
        return True
    else:
        return False


def asos_identifier(text):
    if re.search("class=\"productLink_.*?\"", text) is not None:
        return True
    else:
        return False

