from time import sleep
from SecondFunctions.fileCalendar import age_calendar
import re

def searching_for_videos():
    sleep(0.6)
    keywords = input("\nEnter a request on YouTube without (| and -): ")
    while True:
        if not keywords:
            keywords = input("\nEnter again: ")
        else:
            break
    keywords = re.sub(r"[|-]", " ", keywords)

    sleep(0.6)
    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ")
    while True:
        if len(region) == 2 and region.isalpha():
            region = region.upper()
            break
        else:
            region = input("\nEnter again: ")
            region = region.upper()

    sleep(0.6)
    filterQ = input("\nDo you need to filter videos?(y/n): ")
    if filterQ == "y":

        sort = input("Do you need to sort by something?(y/n):")
        if sort == "y":

            print("\nRelevance - default; date - sort by upload date; viewCount - sort from highest to lowest number of views; " \
            "rating - sort from highest to lowest rating; title - sort alphabetically by title")

            which_order = input("\nEnter: relevance/date/viewCount/rating/title: ")
            while True:
                if which_order in ["relevance", "date", "viewCount", "rating", "title"]:
                    break
                else:
                    which_order = input("\nEnter again: ")

            dimension = input("\nWhat dimension do you need? Enter: 2d/3d/any: ")
            dimension = dimension.lower()
            while True:
                if dimension in ["2d", "3d", "any"]:
                    break
                else:
                    dimension = input("\nEnter again: ")
                    dimension = dimension.lower()
        else:
            which_order = "relevance"
            dimension = "any"

        sleep(0.6)
        dateBefore = input("\nDo you need videos before some time?(y/n): ")
        if dateBefore.lower() == "y":
            yearB, monthB, dayB = age_calendar(dateBefore=True)

            ageBefore = (f"{yearB}-{monthB}-{dayB}T00:00:00Z")
        else:
            ageBefore = None


        sleep(0.6)
        dateAfter = input("\nDo you need videos after some time?(y/n): ")

        if dateAfter.lower() == "y":
            yearA, monthA, dayA = age_calendar(dateAfter=True)
            
            ageAfter = (f"{yearA}-{monthA}-{dayA}T00:00:00Z")
        else:
            ageAfter = None
        

        sleep(0.6)
        durationQ = input("\nDo you need a duration of video?(y/n): ")
        if durationQ == "y":
            duration = input('\nShort - less 4 minutes; medium - from 4 to 20 minutes; long - from 20 minutes. Enter: short/medium/long: ')
            duration = duration.lower()
            while True:
                if duration in ["short", "medium", "long"]:
                    break
                else:
                    duration = input("\nEnter again: ")
                    duration = duration.lower()
        else:  
            duration = "any"
    else:
        which_order = "relevance"
        dimension = "any"
        ageBefore = None
        ageAfter = None
        duration = "any"


    sleep(0.6)
    maximum = input("\nHow much do you want to receive videos?: ")
    while True:
        if maximum.isdigit():
            break
        else:
            maximum = input("\nEnter again: ")
            
    maximum = int(maximum)
    if maximum > 51:
        maximum = 50
    elif maximum < 4:
        maximum = 5

    return keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension