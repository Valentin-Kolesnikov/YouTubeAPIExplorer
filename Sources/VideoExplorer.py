from datetime import datetime
from time import sleep
from googleapiclient.errors import HttpError
import asyncio
import aiohttp
import re

def age_calendar(dateBefore=False, dateAfter=False):
    plus_year = False
    now = datetime.now()
    sleep(1)
    year = input("\nEnter the year: ")

    if year.isdigit() and 2006 <= int(year) <= now.year:
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            plus_year = True
    elif year.isdigit() and 6 <= int(year) <= (now.year - 2000):
        year = str(20) + str(year.zfill(2))
        if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
            plus_year = True
    elif dateAfter:
        year = 2005
    elif dateBefore:
        year = now.year

    sleep(1)
    month = input("\nEnter the month numerously: ")

    if month.isdigit() and int(month) < 13 and int(month) != 0:
        if int(year) == now.year and int(month) > now.month:
            month = str(now.month).zfill(2)
        month = str(month).zfill(2)
    elif dateAfter:
        month = str(1).zfill(2)
    elif dateBefore:
        month = str(now.month).zfill(2)

    sleep(1)
    day = input("\nEnter the day numerously: ")

    if day.isdigit() and int(day) != 0 and int(day) < 32:
        if int(year) == now.year and int(month) == now.month and int(day) > now.day:
            day = str(now.day).zfill(2)

        elif month in ['01', '03', '05', '07', '08', '10', '12']:
            day = str(day).zfill(2)

        elif int(day) < 31 and month in ['04', '06', '09', '11']:
            day = str(day).zfill(2)

        elif plus_year == True and month == "02" and int(day) < 30:
            day = str(day).zfill(2)
        
        elif plus_year == False and month == "02" and int(day) < 29:
            day = str(day).zfill(2)
        
        else:
            day = str(1).zfill(2)
    
    elif dateAfter:
        day = str(1).zfill(2)
    elif dateBefore:
        day = str(now.day).zfill(2)
        
    return year, month, day


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
    filterQ = input("\nDo you need to sort the video?(y/n): ")
    if filterQ == "y":
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


def collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension):
    try:
        request = youtube.search().list(
            videoDimension=dimension,
            q=keywords,
            regionCode=region,
            publishedBefore=ageBefore,
            order=which_order,
            publishedAfter=ageAfter,
            videoDuration=duration,
            part="snippet",
            type="video",
            maxResults=maximum,
        ).execute()

        video_ids = []
        channel_ids = []

        for item in request["items"]:
            videos = item["id"]["videoId"]
            video_ids.append(videos)

            channels = item["snippet"]["channelId"]
            channel_ids.append(channels)

        return video_ids, channel_ids, False
    
    except HttpError as exc:
        status = exc.resp.status

        if status == 400:
            print(f"\n\u001b[31mError {status}: Bad Request. There is some issues with Google requests.\u001b[0m")

        elif status == 403:
            print(f"\n\u001b[31mError {status}: Forbidden. Probably, you exceeded your YouTube API quota.\u001b[0m")

        elif status == 404:
            print(f"\n\u001b[31mError {status}: Not Found. Probably, the non-existent video was found.\u001b[0m")

        else:
            print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")
        
        input("\nPress Enter to return...")
        
        return {}, {}, True


async def fetch_ryd(session, vid):
    ryd_url = f"https://returnyoutubedislikeapi.com/votes?videoId={vid}"
    async with session.get(ryd_url) as dislike:
        if dislike.status == 200:
            return vid, await dislike.json()
        else:
            return vid, {"error": "N/A"}
        
async def ryd(video_ids):
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_ryd(session, vid) for vid in video_ids]
        responses = await asyncio.gather(*tasks)
        for vid, data in responses:
            results[vid] = data
    return results


def collect_stats(youtube, video_ids, channel_ids):
    try:
        statrequest = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        channelrequest = youtube.channels().list(
            part="snippet",
            id=",".join(channel_ids)
        ).execute()

        dict_channels = { 
            ch["id"]: {
                "title": ch["snippet"]["title"]
            }
            for ch in channelrequest["items"]
        }
        
        return statrequest, dict_channels, False
    
    except HttpError as exc:
        status = exc.resp.status

        if status == 400:
            print(f"\n\u001b[31mError {status}: Bad Request. There is some issues with Google requests.\u001b[0m")

        elif status == 403:
            print(f"\n\u001b[31mError {status}: Forbidden. Probably, you exceeded your YouTube API quota.\u001b[0m")

        elif status == 404:
            print(f"\n\u001b[31mError {status}: Not Found. Probably, the non-existent video was found.\u001b[0m")

        else:
            print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")
        
        input("\nPress Enter to return...")

        return {}, {}, True
    
    except Exception:
        print("Probably, YouTube has problems with submitted objects")

        return {}, {}, True
    
def output_videos(results, statrequest, dict_channels):
    number = 0
    for item in statrequest["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]
        published_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y")

        likes = results.get(video_id, {}).get("likes", "No")
        dislikes = results.get(video_id, {}).get("dislikes", "No")
        views = results.get(video_id, {}).get("viewCount", "No")
        comments = item["statistics"].get("commentCount", "No")

        channel_id = item["snippet"]["channelId"]
        channel_info = dict_channels.get(channel_id, {})

        number += 1

        print(
            f"{number}.\n"
            f"{title}\n"
            f"https://www.youtube.com/watch?v={video_id}\n"
            f"{views} views; {likes} likes; {dislikes} dislikes; {comments} comments\n"
            f"{formatted_date}\n"
            f"{channel_info.get('title', 'N/A')}\n"
            f"Channel Link: https://www.youtube.com/channel/{channel_id}\n")