from googleapiclient.errors import HttpError
import re
import requests
import json

def youtube_id_finder(url):
    while True:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            url = input("\nTry entering the url again: ")

def channel_name(video_id, api_key):
    try:
        name = requests.get(
            "https://www.googleapis.com/youtube/v3/videos",
            params={"part": "snippet", "id": video_id, "key": api_key}
        )
        return name.json()["items"][0]["snippet"]["channelTitle"], False
    
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

        return {}, True

def youtube_which_order():
    which_order = input("\nDo you need to sort comments? By relevance - 1; By time - 2: ")

    if which_order == "1":
        which_order = "relevance"
    elif which_order == "2":
        which_order = "time"
    else:
        which_order = "relevance"

    return which_order

def collect_comments(video_id, search_terms, which_order, youtube):
    comments = []
    next_page_token = None

    try:
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

        return comments, False
    
    except HttpError as exc:
        status = exc.resp.status

        if status == 400:
            print(f"\n\u001b[31mError {status}: Bad Request. There is some issues with Google requests.\u001b[0m")

        elif status == 403:
            error_reason = exc.content.decode("utf-8")
            error_json = json.loads(error_reason)
            reason = error_json["error"]["errors"][0]["reason"]

            if reason == "commentsDisabled":
                    print(f"\n\u001b[31mError {status}: Forbidden. Comments of the video are disabled.\u001b[0m")
            else:
                print(f"\n\u001b[31mError {status}: Forbidden. Probably, you exceeded your YouTube API quota.\u001b[0m")

        elif status == 404:
            print(f"\n\u001b[31mError {status}: Not Found. Probably, the non-existent video was found.\u001b[0m")

        else:
            print(f"\n\u001b[31mUnexpected HTTP error: {status}\u001b[0m")
        
        input("\nPress Enter to return...")

        return {}, True

def count_keys(comments, search_terms):
    counts = {kw: 0 for kw in search_terms}
    amount_comments = 0
    for comment in comments:
        amount_comments += 1
        for kw in search_terms:
            counts[kw] += comment.lower().count(kw.lower())

    print(f"Total comments: {amount_comments}")
    for kw, count in counts.items():
        print(f"{kw}: {count}")
    
def numberofcomments(comments, number, channel):
    print(f"Channel: {channel}")
    for i, c in enumerate(comments[:int(number)], 1):
        print(f"\n\n{i}:\n{c}")