def searching_for_videos():
    keywords = input("Enter a request on YouTube: ")

    region = input("What region would you like? (Enter as US, RU, UK, etc): ")

    which_orderQ = input("Do you need a filter?: ")
    if which_orderQ.lower() == "yes" or "yeah" or "+" or "1" or "of course":
        which_order = input('Which fulter (enter it literally as written): date, rating, relevance, title, popularity: ')
        if which_order == "popularity":
            which_order = "viewCount"
    else:
        which_order = None

    if which_order == "date":
        age = None
    else:
        date = input("Do you need to enter the certain time?: ")

        if date.lower() == "yes" or "yeah" or "+" or "1" or "of course":
            year = input("Enter the year: ")
            month = input("Enter the month (as 01, 02, etc): ")
            day = input("Enter the day")

            age = (f"{year}-{month}-{day}T00:00:00Z")
        
    
    durationQ = input("Do you need a duration of video: ")
    if durationQ.lower() == "yes" or "yeah" or "+" or "1" or "of course":
        duration = input('Enter it literally: "short", "medium", "long": ')

    return keywords, region.upper(), age, duration.lower(), which_order

def collect_videos(youtube, keywords, region, age, duration, which_order):
    request = youtube.search().list(
        q=keywords,
        regionCode=region,
        publishedAfter=age,
        videoDuration=duration,
        part="snippet",
        type="video",
        maxResults=5,
        order=which_order,
    ).execute()