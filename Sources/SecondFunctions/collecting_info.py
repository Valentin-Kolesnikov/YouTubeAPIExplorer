from googleapiclient.errors import HttpError
import asyncio
import aiohttp

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