import requests
from datetime import datetime

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

    return keywords, region.upper(), age, duration


def collect_searches(youtube, keywords, region, age, duration):
    request = youtube.search().list(
        q=keywords,
        regionCode=region,
        publishedAfter=age,
        videoDuration=duration,
        part="snippet",
        type="video",
        maxResults=25,
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


def ryd(video_ids):
    results = {}
    for vid in video_ids:
        ryd_url = f"https://returnyoutubedislikeapi.com/votes?videoId={vid}"
        ryd_response = requests.get(ryd_url)
        if ryd_response.status_code == 200:
            ryd_data = ryd_response.json()
            results[vid] = ryd_data
        else:
            results[vid] = {"error": "N/A"}

    return results


def collect_stats(youtube, video_ids, channel_ids):
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

    return statrequest, dict_channels
    
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
            f"{channel_info.get("title", "N/A")}\n"
            f"Channel Link: https://www.youtube.com/channel/{channel_id}\n")