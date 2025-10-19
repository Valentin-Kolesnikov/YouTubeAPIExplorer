from SecondFunctions.fileCalendar import age_calendar
import re






def search_engine():
    keywords = input("\nEnter a request on YouTube without (| and -): ")

    while True:
        if not keywords:
            keywords = input("\nEnter again: ")

        else:
            break

    keywords = re.sub(r"[|-]", " ", keywords)

    filterQ = input("\nDo you need to filter videos?(y/n): ")
    if filterQ == "y":

        sort = input("\nDo you need to sort by something?(y/n):")
        if sort == "y":
            which_orderDict = {
                "1": "relevance",
                "2": "date",
                "3": "viewCount",
                "4": "rating",
                "5": "title",
                "6": "help"
            }

            which_order = input("\n1. relevance\n2. date\n3. viewCount\n4. rating\n5. title\n6. help\n\nEnter: ")
            while True:
                if which_order == "6":

                    which_order = input("" \
                    "\n1. relevance - default" \
                    "\n2. date - sort by upload date" \
                    "\n3. viewCount - sort from highest to lowest number of views" \
                    "\n4. rating - sort from highest to lowest rating" \
                    "\n5. title - sort alphabetically by title\n" \
                    "\nEnter again: ")

                elif which_order in which_orderDict:
                    which_order = which_orderDict[which_order]
                    break

                else:
                    which_order = input("\nEnter again: ")

            dimensionDict = {
                "1": "2d",
                "2": "3d",
                "3": "any"
            }
            dimension = input("\nWhat dimension do you need?\n1. 2d\n2. 3d\n3. any: ")

            while True:
                if dimension in dimensionDict:
                    dimension = dimensionDict[dimension]
                    break

                else:
                    dimension = input("\nEnter again: ")
        else:
            which_order = "relevance"
            dimension = "any"

        dateBefore = input("\nDo you need videos before some time?(y/n): ")

        if dateBefore.lower() == "y":
            yearB, monthB, dayB = age_calendar(dateBefore=True)

            ageBefore = (f"{yearB}-{monthB}-{dayB}T00:00:00Z")

        else:
            ageBefore = None


        dateAfter = input("\nDo you need videos after some time?(y/n): ")

        if dateAfter.lower() == "y":
            yearA, monthA, dayA = age_calendar(dateAfter=True)
            
            ageAfter = (f"{yearA}-{monthA}-{dayA}T00:00:00Z")

        else:
            ageAfter = None
        

        durationQ = input("\nDo you need a duration of video?(y/n): ")
        if durationQ == "y":
            durationDict = {
                "1": "short",
                "2": "medium",
                "3": "long"
            }
            duration = input('\n1. Short - less 4 minutes\n2. medium - from 4 to 20 minutes\n3. long - from 20 minutes\n\nEnter: ')

            while True:
                if duration in durationDict:
                    duration = durationDict[duration]
                    break

                else:
                    duration = input("\nEnter again: ")
        else:  
            duration = "any"
    else:
        which_order = "relevance"
        dimension = "any"
        ageBefore = None
        ageAfter = None
        duration = "any"


    maximum = input("\nHow much do you want to receive videos?: ")

    while True:
        if maximum.isdigit():
            break

        else:
            maximum = input("\nEnter again: ")
            
    maximum = int(maximum)
    if maximum > 51:
        maximum = 50
        
    elif maximum < 1:
        maximum = 1

    return keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension