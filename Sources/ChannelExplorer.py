import requests

def channel_name(video_id, api_key):
    name = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={"part": "snippet", "id": video_id, "key": api_key}
    )
    return name.json()["items"][0]["snippet"]["channelTitle"]