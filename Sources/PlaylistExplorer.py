from googleapiclient.errors import HttpError
from Patterns.errors import http_error, WinError
from 

def get_infos():
    playlist = input("Do you need to explore: playlists - 1; likes-dislikes - 2: ")
    while True:
        if playlist == "1":
            another = input("Do you want to explore: your playlists - 1; other people's playlists: ")
            if another == "1":
                youtube_OAuth2()
            elif another == "2":
                #...

        elif playlist == "2":
            youtube_OAuth2()
            while True:
                rating = input("Like - 1, Dislike - 2: ")
                if rating == "1":
                    rating = "like"
                    break

                elif rating == "2":
                    rating = "dislike"
                    break

                else:
                    rating = input("Enter again: ")
        else:
            playlist = input("Enter again: ")

        return rating, 

def collect_videos(youtube, rating):
    try:
        requests = youtube.videos().list(
            part="snippet",
            myRating=rating,

        )

    except HttpError as exc:
        
        http_error(exc)
        
        return 

    except OSError as exc:

        WinError(exc)

        return 