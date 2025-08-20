def age_calendar():
    plus_year = False
    year = input("\nEnter the year: ")

    if year.isdigit() and 2006 <= int(year) <= 2025:
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            plus_year = True
    else:
        year = str(2006)


    month = input("\nEnter the month numerously: ")

    if month.isdigit() and int(month) < 13 and int(month) != 0:
        if 0 < int(month) <= 9:
            month = str(month).zfill(2)
    else:
        month = str(1).zfill(2)

                    
    day = input("\nEnter the day numerously: ")

    if day.isdigit() and int(day) != 0 and int(day) < 32:
        if month in ['01', '03', '05', '07', '08', '10', '12']:
            day = str(day).zfill(2)

        elif int(day) < 31 and month in ['04', '06', '09', '11']:
            day = str(day).zfill(2)

        elif plus_year == True and month == "02" and int(day) < 30:
            day = str(day).zfill(2)
        
        elif plus_year == False and month == "02" and int(day) < 29:
            day = str(day).zfill(2)
        
        else:
            day = str(1).zfill(2)
    else:
        day = str(1).zfill(2)

    return year, month, day

def searching_for_videos():
    keywords = input("\nEnter a request on YouTube: ")

    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ")

    which_orderQ = input("\nDo you need a filter?(Yes, No): ")

    if which_orderQ.lower() == "yes":
        which_order = input(
            '\nWhich fulter (enter it literally as written):' \
            ' date, rating, relevance, title, popularity: '
            )
        if which_order == "popularity":
            which_order = "viewCount"
    else:
        which_order = None

    
    date = input("\nDo you need to enter the certain time?(Yes, No): ")

    if date.lower() == "yes":
        year, month, day = age_calendar()

        age = (f"{year}-{month}-{day}T00:00:00Z")
    else:
        age = None
        
    
    durationQ = input("\nDo you need a duration of video(Yes, No): ")
    if durationQ == "yes":
        duration = input('\nEnter it literally: "short", "medium", "long": ')
        duration.lower()
    else:
        duration = None

    return keywords, region.upper(), age, duration, which_order

def collect_searches(youtube, keywords, region, age, duration, which_order):
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

    video_ids = []
    for item in request["items"]:
        videos = item["id"]["videoId"]
        video_ids.append(videos)
    
    channel_ids = []
    for item in request["items"]:
        channels = item["snippet"]["channelId"]
        channel_ids.append(channels)

    return video_ids, channel_ids


def collect_stats(youtube, video_ids, channel_ids):
    statrequest = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    ).execute()

    channelrequest = youtube.channels().list(
        part="snippet,statistics",
        id=",".join(channel_ids)
    ).execute()

    return statrequest, channelrequest