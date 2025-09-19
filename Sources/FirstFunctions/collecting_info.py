from googleapiclient.errors import HttpError
from Patterns.httperror import http_error
import requests
import json

def channel_name(video_id, api_key):
    try:
        name = requests.get(
            "https://www.googleapis.com/youtube/v3/videos",
            params={"part": "snippet", "id": video_id, "key": api_key}
        )
        return name.json()["items"][0]["snippet"]["channelId"], False
    
    except HttpError as exc:
        
        http_error(exc)

        return {}, True
    
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