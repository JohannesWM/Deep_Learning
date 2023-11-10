import requests
import re
import time
from random import randint

'''
The purpose of this file is to attempt to create algorithms that will scrape all given websites of their products.

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
    with open("../html_files/ASOS/asos.html", "r") as asos_file:
        asos_as_txt = asos_file.read()
        a_tags = re.finditer("<a.*?>.*?</a>", asos_as_txt)

    a_tags_list = [asos_as_txt[_.span()[0]:_.span()[1]] for _ in a_tags]  # all a tags in text format
    WM_page_list = [i for i in a_tags_list if re.search("id=\"women-floor\">WOMEN<", i) is not None or
                    re.search("id=\"men-floor\">MEN<", i) is not None]  # these are the given a_tags that contain links
    # to the mens page and women's page
    men_women_links = [re.search("\"https://.*?\"", i).group().replace("\"", "") for i in WM_page_list]  # these are
    # the links to the men's page and the women's page of the website
    """
    This is the code that is used to store the women's page and men's page into different files
    
    for _ in men_women_links:
        gender = re.search("women", _) if re.search("women", _) is not None else re.search("men", _)
        with open(f"../html_files/ASOS/{gender.group()}_ASOS.html", "w") as gender_file:
            gender_file.write(requests.get(_, headers=headers).text)
            time.sleep(randint(1, 10))
    """

    with open("../html_files/ASOS/women_ASOS.html", "r") as men_file:
        page = men_file.read()
        product_links = re.findall("<a class=\"feature__link\" href=\"/us/women.*?\".*?>", page)
        for _ in product_links:
            without_href = _.replace("<a class=\"feature__link\" href=\"", "").replace("\"", "").replace(">", "")
            link_self = f"https://www.asos.com{without_href}"
            without_href = _.replace("<a class=\"feature__link\" href=\"", "").replace("\"", "").replace(">", ""). \
                replace("/", "DEV")
            with open(f"../html_files/ASOS/{without_href[:25]}.html", "w") as file:
                file.write(requests.get(link_self, headers=headers).text)


def scrape_lowes():
    print(f"{Warning_Text}This function has been completed: scrape_lowes()!")
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


def scrape_bath_and_body():
    """
    with open("../html_files/overstock.html", "r") as overstock_file:
        overstock_text = overstock_file.read()
        a_tags = re.findall("<a.*?>.*?</a>", overstock_text)

        needed_tags = [tag for tag in a_tags if re.search("ImageTilesSectionStyles_tileWrap__RfrjP TileImageStyles_Link"
                                                          "__QjiYx", tag) is not None]
        needed_tags.pop()

    links_sections = []

    for necessary_tag in needed_tags:
        found = re.search("/c/.*?\"", necessary_tag).group().replace("\"", "")
        links_sections.append(f"https://www.bedbathandbeyond.com{found}")

    sub_link_uno = []

    file_num = 0
    for section_link in links_sections:
        product_page = requests.get(section_link, headers=headers).text
        sub_a_tags = re.findall("<a class=\"topTileSection_tierOneTileLink__NDCdh tile-.\" .*?>.*?</a>", product_page)
        for _ in sub_a_tags:
            indiv_link = re.findall("href=\".*?\"", _)
            for indiv_i_link in indiv_link:
                indiv_i_link = indiv_i_link.replace("href=\"", "").replace("\"", "")
                indiv_i_link = f"https://www.bedbathandbeyond.com{indiv_i_link}"
                sub_link_uno.append(indiv_i_link)
        print(sub_link_uno)
        print(len(sub_link_uno))
        time.sleep(randint(1, 10))
        # with open(f"../html_files/bath_body/before_products/{file_num}_{randint(1, 255)}.html", "w") as quick_write:
        #     quick_write.write(product_page)
        file_num += 1
    """

    sub_link_uno = ['https://www.bedbathandbeyond.com/c/furniture/bathroom-furniture?t=24355',
                    'https://www.bedbathandbeyond.com/c/outdoor/patio-furniture?t=7908',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=8225',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=3973',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=7112',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=7113',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=3688',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=7152',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=4386',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a1589=7151',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2415=2915',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2415=2926',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2415=3912',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2415=2947',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2046=415769',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2046=415812',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2046=3613',
                    'https://www.bedbathandbeyond.com/c/rugs/area-rugs?t=17603&amp;a2046=3974',
                    'https://www.bedbathandbeyond.com/c/bedding/comforters-and-sets?t=50',
                    'https://www.bedbathandbeyond.com/c/bedding/quilts-bedspreads?t=11',
                    'https://www.bedbathandbeyond.com/c/bedding/bed-sheets-pillowcases?t=5',
                    'https://www.bedbathandbeyond.com/c/bedding/mattress-pads-toppers?t=36',
                    'https://www.bedbathandbeyond.com/c/bedding/bedding-sets?t=276&amp;a1001=2855',
                    'https://www.bedbathandbeyond.com/c/bedding/bedding-sets?t=276&amp;a1001=2854',
                    'https://www.bedbathandbeyond.com/c/bedding/bedding-sets?t=276&amp;a1001=2857',
                    'https://www.bedbathandbeyond.com/c/bedding/bedding-sets?t=276&amp;a1001=2856',
                    'https://www.bedbathandbeyond.com/Madison-Park,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Laura-Ashley,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Eddie-Bauer,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Nautica,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/c/home-decor/mirrors?t=28403',
                    'https://www.bedbathandbeyond.com/c/home-decor/decorative-accessories?t=28398',
                    'https://www.bedbathandbeyond.com/c/home-decor/window-treatments?t=28400',
                    'https://www.bedbathandbeyond.com/c/home-decor/throw-pillows?t=28447',
                    'https://www.bedbathandbeyond.com/c/art?t=28454',
                    'https://www.bedbathandbeyond.com/c/home-decor/wall-decor?t=28401',
                    'https://www.bedbathandbeyond.com/c/decorative-accessories/decorative-objects?t=28432',
                    'https://www.bedbathandbeyond.com/c/lighting?t=31087',
                    'https://www.bedbathandbeyond.com/c/rugs?t=17602',
                    'https://www.bedbathandbeyond.com/c/home-decor/slipcovers?t=28399',
                    'https://www.bedbathandbeyond.com/c/bath/towels?t=18650',
                    'https://www.bedbathandbeyond.com/c/bath/bathroom-rugs-bath-mats?t=19459',
                    'https://www.bedbathandbeyond.com/c/bath/shower-curtains-and-accessories?t=18666',
                    'https://www.bedbathandbeyond.com/c/bath/bathroom-accessories?t=18656',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/small-kitchen-appliances?t=24635',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/dinnerware?t=24766',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/cookware?t=24666',
                    'https://www.bedbathandbeyond.com/c/small-kitchen-appliances/kitchen-mixers?t=28194',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/kitchen-tools?t=24660',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/serveware?t=24770',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/bakeware?t=24665',
                    'https://www.bedbathandbeyond.com/c/large-kitchen-appliances/ranges-ovens?t=31176',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/kitchen-linen?t=24639',
                    'https://www.bedbathandbeyond.com/c/kitchen-dining/flatware?t=24765',
                    'https://www.bedbathandbeyond.com/Ninja,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Kitchenaid,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Cuisinart,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/Zwilling,/brand,/results.html',
                    'https://www.bedbathandbeyond.com/c/outdoor/patio-furniture?t=7908',
                    'https://www.bedbathandbeyond.com/c/outdoor-dining-furniture/outdoor-dining-sets?t=7924',
                    'https://www.bedbathandbeyond.com/c/outdoor/outdoor-decor?t=22439',
                    'https://www.bedbathandbeyond.com/c/outdoor-decor/outdoor-cushions-throw-pillows?t=22497',
                    'https://www.bedbathandbeyond.com/c/outdoor-shade-structures/gazebos?t=22456',
                    'https://www.bedbathandbeyond.com/c/storage-organization/outdoor-storage?t=31377',
                    'https://www.bedbathandbeyond.com/c/outdoor/garden?t=22440',
                    'https://www.bedbathandbeyond.com/c/outdoor/grills-outdoor-cooking?t=22477',
                    'https://www.bedbathandbeyond.com/c/lighting/outdoor-lighting?t=31288',
                    'https://www.bedbathandbeyond.com/c/outdoor-play/swing-sets?t=31279',
                    'https://www.bedbathandbeyond.com/c/bathroom-fixtures/bathroom-vanities?t=24474',
                    'https://www.bedbathandbeyond.com/c/showers-bathtubs/shower-stalls-kits?t=31254',
                    'https://www.bedbathandbeyond.com/c/showers-bathtubs/bathtubs?t=70501',
                    'https://www.bedbathandbeyond.com/c/bathroom-fixtures/toilets-bidets?t=31197',
                    'https://www.bedbathandbeyond.com/c/home-decor/mirrors?t=28403&amp;a1004=36522',
                    'https://www.bedbathandbeyond.com/c/bathroom-sinks-faucets/bathroom-sinks?t=31204',
                    'https://www.bedbathandbeyond.com/c/bathroom-sinks-faucets/bathroom-sink-faucets?t=31205',
                    'https://www.bedbathandbeyond.com/c/bathroom-fixtures/bathroom-hardware?t=31203',
                    'https://www.bedbathandbeyond.com/c/kitchen-sinks-faucets/kitchen-faucets?t=31209',
                    'https://www.bedbathandbeyond.com/c/kitchen-sinks-faucets/kitchen-sinks?t=70278',
                    'https://www.bedbathandbeyond.com/c/lighting?t=31087',
                    'https://www.bedbathandbeyond.com/c/home-improvement/flooring?t=31240',
                    'https://www.bedbathandbeyond.com/c/appliances/large-kitchen-appliances?t=31164',
                    'https://www.bedbathandbeyond.com/c/storage-organization?t=31157',
                    'https://www.bedbathandbeyond.com/c/hardware/cabinet-hardware?t=31262',
                    'https://www.bedbathandbeyond.com/c/ceiling-wall-coverings/wallpaper?t=31238',
                    'https://www.bedbathandbeyond.com/c/home-improvement/doors?t=31263',
                    'https://www.bedbathandbeyond.com/c/home-improvement/tiles?t=70255',
                    'https://www.bedbathandbeyond.com/c/storage-organization/outdoor-storage?t=31377',
                    'https://www.bedbathandbeyond.com/c/landscaping/decking?t=31221',
                    'https://www.bedbathandbeyond.com/c/lighting/outdoor-lighting?t=31288',
                    'https://www.bedbathandbeyond.com/c/outdoor-heating-cooling/fire-pits?t=22443',
                    'https://www.bedbathandbeyond.com/c/outdoor/outdoor-shade-structures?t=22598',
                    'https://www.bedbathandbeyond.com/c/outdoor/garden?t=22440',
                    'https://www.bedbathandbeyond.com/c/outdoor/yard-tools?t=31520',
                    'https://www.bedbathandbeyond.com/c/storage-organization/tool-storage?t=31357',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2856',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2859',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2857',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2854',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2855',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2858',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1001=2860-7470-8820-8821-10213-32473',
                    'https://www.bedbathandbeyond.com/c/baby-furniture/crib-mattresses?t=19428',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1093=19388',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1093=19389',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1093=9379',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;a1093=134497',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;brand=lucid+comfort+collection',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;brand=linenspa+essentials',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;brand=zinus',
                    'https://www.bedbathandbeyond.com/c/mattresses?t=24351&amp;brand=slumber+solutions',
                    'https://www.bedbathandbeyond.com/c/ceiling-lighting/chandeliers?t=31344',
                    'https://www.bedbathandbeyond.com/c/ceiling-lighting/flush-mount-ceiling-lights?t=31345',
                    'https://www.bedbathandbeyond.com/c/ceiling-lighting/pendant-lights?t=31346',
                    'https://www.bedbathandbeyond.com/c/lamps/floor-lamps?t=31333',
                    'https://www.bedbathandbeyond.com/c/lighting/ceiling-fans?t=31287',
                    'https://www.bedbathandbeyond.com/c/lamps/table-lamps?t=31332',
                    'https://www.bedbathandbeyond.com/c/lamps/lamp-sets?t=60679',
                    'https://www.bedbathandbeyond.com/c/ceiling-lighting/track-lighting?t=31394',
                    'https://www.bedbathandbeyond.com/c/bathroom-lighting/vanity-lights?t=31193',
                    'https://www.bedbathandbeyond.com/c/wall-lighting/wall-sconces?t=70172']

    file_num_second = 6
    for section_link in sub_link_uno:
        print(f"The section link is currrently: {section_link}")
        product_page = requests.get(section_link, headers=headers).text

        with open(f"../html_files/bath_body/{file_num_second}_{randint(266, 999)}.html", "w") as new_fil:
            new_fil.write(product_page)

        numbers = re.search("lastPage\":\{\"value\":\d+", product_page).group()
        number_self = ""
        for char in numbers:
            if char.isdigit():
                number_self = f"{number_self}{char}"

        numbers = int(number_self)
        print(f"The hightest pagenumber is: {numbers}")

        second_second_num = 0

        print("Starting page loop")

        for num in range(numbers):
            if num > 1:
                try:
                    print(f"Attempting page: {num}")
                    new_formed_link = f"{section_link}&page={str(num)}"
                    num_product_page = requests.get(new_formed_link, headers=headers).text
                    print(f"Link sent to: {new_formed_link}")
                    with open(f"../html_files/bath_body/{file_num_second}_{randint(266, 999)}_{second_second_num}.html",
                              "w") as new_fil:
                        new_fil.write(num_product_page)
                except Exception as e:
                    print(e)
            else:
                pass
            sleep_number = randint(1, 10)
            print(f"sleeping for: {sleep_number}")
            time.sleep(sleep_number)
            second_second_num += 1

        print("Finished Section", end="\n\n\n_________________________________________________\n\n\n")
        file_num_second += 1
        time.sleep(randint(1, 10))


def scrape_chewy(chewy_page_links=None):
    if chewy_page_links is None:
        # chewy_page_links = ["https://www.chewy.com/b/devices-supplies-11578",
        #                     "https://www.chewy.com/b/compounding-pharmacy-11718",
        #                     "https://www.chewy.com/b/cat-pharmacy-11589",
        #                     "https://www.chewy.com/b/immune-support-11612",
        #                     "https://www.chewy.com/b/gastrointestinal-care-digestive-11582",
        #                     "https://www.chewy.com/b/antibiotics-11602",
        #                     "https://www.chewy.com/b/dog-pharmacy-11561",
        #                     "https://www.chewy.com/b/pharmacy-2515",
        #                     "https://www.chewy.com/b/horse-pharmacy-11617",
        #                     "https://www.chewy.com/b/vitamins-electrolytes-11633",
        #                     "https://www.chewy.com/b/allergy-relief-11568"]
        chewy_page_links = ["https://www.chewy.com/b/pain-relief-arthritis-11566"]
    on_link = 12

    for page_link in chewy_page_links:
        page_text = requests.get(page_link, headers=headers).text

        with open(f"../html_files/Chewy/{on_link}_Chewy.html", "w") as main_file:
            main_file.write(page_text)

        print(f"\033[0mSuccessfully pushed html to: ../html_files/Chewy/{on_link}_Chewy.html")

        # this function will later be used for vectorization
        def get_product_divs():
            div_tags_ppage = re.findall("<div.*?>.*?</div>", page_text)

            for div in div_tags_ppage:
                print(f"{Warning_Text}THIS FUNCTION IS NOT COMPLETE")

        more_pages = True
        all_digits = [i for i in page_link if i.isdigit()]
        number_string = ""

        for digit in all_digits:
            number_string = f"{number_string}{digit}"

        before_numbers = page_link.replace(number_string, "")

        current_page = 2
        reference = ""
        print("Starting all page scrape", end="\n|__|\n")
        while more_pages:

            print(f"\033[0mRequesting: {before_numbers}_c{number_string}_p{current_page.__str__()}")
            new_page = requests.get(f"{before_numbers}_c{number_string}_p{current_page.__str__()}", headers=headers). \
                text

            if current_page == 2:
                reference = re.search("<h2 class=\"ProductListing_plpProductCardTitleWrapper___8s4y\">.*?</h2>",
                                      page_text).group()
            if current_page > 2:
                htwo_tags = re.findall("<h2 class=\"ProductListing_plpProductCardTitleWrapper___8s4y\">.*?</h2>",
                                       new_page)
                print(f"{Warning_Text}Length of <h2> list: {htwo_tags.__len__()}")
                for htwotag in htwo_tags:
                    if reference == htwotag:
                        print(f"{Warning_Text}Finished All Pages")
                        more_pages = False
                        break

            if more_pages:
                with open(f"../html_files/Chewy/{on_link}_{current_page}_Chewy.html", "w") as writing_file:
                    writing_file.write(new_page)
                print(f"\033[0mSuccessfully puched html to: /html_files/Chewy/{on_link}_{current_page}_Chewy.html")

            sleep_time = randint(1, 10)

            print(f"\033[0mReference is: {reference}")
            print(f"\033[0mCurrently on Page: {current_page}")
            print(f"\033[0mSleeping for: {sleep_time}", end="\n\n")

            time.sleep(sleep_time)
            current_page += 1

        on_link += 1


scrape_chewy()
