from googleapiclient.discovery import build
import re
import requests

def find_channel_name(video_id, api_key):
    name = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={"part": "snippet", "id": video_id, "key": api_key}
    )
    return name.json()["items"][0]["snippet"]["channelTitle"]

def youtube_api_key(api_key):
    while True:
        if len(api_key) == 39:
            youtube = build('youtube', 'v3', developerKey=api_key)
            return youtube
        else:
            api_key = input("\nTry entering the API key again: ")

def youtube_id_finder(url):
    while True:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            url = input("\nTry entering the url again: ")


api_key = input("\nEnter your YouTube API key: ")

youtube = youtube_api_key(api_key)

url = input("\nEnter the url: ")     
video_id = youtube_id_finder(url)
                                            
channel = find_channel_name(video_id, api_key)

while True:
    search_terms = input("\nEnter the keyword (press Enter to continue without the keyword): ")
    if search_terms:
        break
    elif not search_terms:
        break

which_order = input("\nDo you need to sort comments? By relevance - 1; By time - 2: ")
if which_order == "1":
    which_order = "relevance"
elif which_order == "2":
    which_order = "time"
else:
    which_order = "relevance"

def collect_comments(video_id, search_terms, which_order):
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part= "snippet",
            videoId= video_id,
            pageToken= next_page_token,
            maxResults= 100,
            textFormat= "plainText",
            order= which_order,
        ).execute()

        for item in request["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            if search_terms.lower() in comment.lower():
                comments.append(comment)

        next_page_token = request.get("nextPageToken")
        if not next_page_token:
            break

    return comments

comments = collect_comments(video_id, search_terms, which_order)

number = int(input("\nHow many comments do you need?: "))

print(f"\n\nChannel: {channel}\n")
for i, c in enumerate(comments[:number], 1):
    print(f"{i}: {c}")

input("Press Enter to exit...")