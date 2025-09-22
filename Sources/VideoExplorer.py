from time import sleep
from Patterns.SearchingSecondThird import search_engine

def searching_for_videos():
    sleep(0.6)
    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ")
    while True:
        if len(region) == 2 and region.isalpha():
            region = region.upper()
            break
        else:
            region = input("\nEnter again: ")
            region = region.upper()

    keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine()

    return keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension