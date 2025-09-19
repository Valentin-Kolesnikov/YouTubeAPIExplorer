from googleapiclient.errors import HttpError
from Patterns.httperror import http_error
from datetime import datetime


def collect_channel_info(youtube, for_id, for_handle):
    try:
        request = youtube.channels().list(
            part="snippet,statistics,contentDetails",
            forHandle=for_handle,
            id=for_id
        ).execute()
        
        if "items" in request and request["items"]:
            channel_id = request["items"][0]["id"]
        else:
            raise ValueError
        
        snippet = request["items"][0]["snippet"]
        statistics = request["items"][0]["statistics"]

        chpublished_at = snippet.get("publishedAt")
        dt = datetime.fromisoformat(chpublished_at.replace("Z", "+00:00"))
        chformatted_date = dt.strftime("%d.%m.%Y")
        
        snistics = {
            "title": snippet.get("title"),
            "channelId": channel_id,
            "description": snippet.get("description")[:500],
            "publishedAt": chformatted_date,
            "customUrl": snippet.get("customUrl", "N/A"),  
            "viewCount": statistics.get("viewCount"),
            "subscriberCount": statistics.get("subscriberCount"),
            "videoCount": statistics.get("videoCount")
        }
        uploads_videos = request["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        
        return snistics, uploads_videos, False
    
    except HttpError as excs:

        http_error(excs)

        return {}, {}, True
    
    except Exception as excs:
        if ValueError:
            print("\nThe channel is not found.")
        else:
            print("\nUnknown problem.")

        input("\nPress Enter to return...")

        return {}, {}, True
    
def collect_popular_videos(youtube, uploads_videos):
    try:
        collection = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_videos,
            maxResults=3
        ).execute()

        videoIds = []
        for item in collection["items"]:
            videoId = item["contentDetails"]["videoId"]
            videoIds.append(videoId)

        return videoIds, False

    except HttpError as excs:

        http_error(excs)

        return {}, True
    
    
def collect_statistics(youtube, videosIds):
    try:
        statrequests = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(videosIds)
        ).execute()

        return statrequests, False
    
    except HttpError as excs:

        http_error(excs)

        return {}, True
    
    except Exception:
        print("Probably, YouTube has problems with submitted objects")

        return {}, True