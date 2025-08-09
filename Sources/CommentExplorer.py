from googleapiclient.discovery import build
from collections import Counter
from pandas import pd
import re
import os

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

def collect_comments(video_id, search_terms, which_order, youtube):
    comments = []
    next_page_token = None

    if which_order == "1":
        which_order = "relevance"
    elif which_order == "2":
        which_order = "time"
    else:
        which_order = "relevance"

    while True:
        request = youtube.commentThreads().list(
            part= "snippet,replies",
            videoId= video_id,
            pageToken= next_page_token,
            maxResults= 50,
            textFormat= "plainText",
            order= which_order,
        ).execute()

        for item in request["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            if any(search_term.lower() in comment.lower() for search_term in search_terms):
                comments.append(comment)
            elif not search_terms:
                comments.append(comment)
                continue 

            if "replies" in item:
                for reply in item["replies"]["comments"]:
                    reply_comments = reply["snippet"]["textDisplay"]
                    if any(reply_term.lower() in reply_comments.lower() for reply_term in search_terms):
                        comments.append(reply_comments)
                    elif not search_terms:
                        comments.append(reply_comments)
                        continue


        comments = list(set(comments))

        next_page_token = request.get("nextPageToken")
        if not next_page_token:
            break

    return comments

def numberofcomments(comments, number, channel):
    os.system('cls')
    print(f"Channel: {channel}")
    for i, c in enumerate(comments[:number], 1):
        print(f"\n\n{i}:\n{c}")