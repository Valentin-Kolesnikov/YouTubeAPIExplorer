from googleapiclient.errors import HttpError

from Patterns.errors import http_error, WinError





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
        
        http_error(exc)
        
        return {}, {}, True
    
    
    except OSError as exc:

        WinError(exc)

        return {}, {}, True


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

        http_error(exc)

        return {}, {}, True
    

    except Exception:
        print("Probably, YouTube has problems with submitted objects")

        return {}, {}, True
        

    except OSError as exc:

        WinError(exc)

        return {}, {}, True