import re

def youtube_id_finder():
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
    terms = input("\nEnter the keywords by one (press Enter to continue): ")

    while True:
        if terms == "":
            break
        search_terms.append(terms)
        terms = input("More?: ")

    search_terms = set(search_terms)


    which_order = input("\n1. By relevance\n2. By time\nEnter the choice: ")

    while True:
        if which_order == "1":
            which_order = "relevance"
            break
        elif which_order == "2":
            which_order = "time"
            break
        else:
            which_order = input("Enter again: ")

    return which_order, search_terms