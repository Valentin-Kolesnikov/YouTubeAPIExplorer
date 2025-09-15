import re
from time import sleep

def youtube_id_finder():
    sleep(0.6)
    url = input("\nEnter the url: ")

    while True:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            url = input("\nTry entering the url again: ")

def youtube_filters():
    search_terms = []
    while True:
        terms = input("\nEnter the keywords by one (press Enter to continue): ")
        if terms == "":
            break
        search_terms.append(terms)

    search_terms = set(search_terms)

    sleep(0.6)
    which_order = input("\nDo you need to sort comments? By relevance - 1; By time - 2: ")

    if which_order == "1":
        which_order = "relevance"
    elif which_order == "2":
        which_order = "time"
    else:
        which_order = "relevance"

    return which_order, search_terms