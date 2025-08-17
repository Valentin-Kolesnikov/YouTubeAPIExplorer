from googleapiclient.discovery import build
from CommentExplorer import *
from ChannelExplorer import channel_name
from VideoExplorer import *
from time import sleep

def youtube_api_key(api_key):
    while True:
        if len(api_key) == 39:
            youtube = build('youtube', 'v3', developerKey=api_key)
            return youtube
        else:
            api_key = input("\nTry entering the API key again: ")

def launcherComments():
    sleep(1)
    api_key = input("\nEnter your YouTube API key: ")
    youtube = youtube_api_key(api_key)

    sleep(1)
    url = input("\nEnter the url: ")     
    video_id = youtube_id_finder(url)
                                                
    channel = channel_name(video_id, api_key)

    sleep(1)
    search_terms = []
    while True:
        terms = input("\nEnter the keywords by one (press Enter to continue): ")
        if terms == "":
            break
        search_terms.append(terms)

    search_terms = set(search_terms)

    sleep(1)
    which_order = youtube_which_order()

    comments = collect_comments(video_id, search_terms, which_order, youtube)

    count_keys(comments, search_terms)

    sleep(1)
    number = int(input("\nHow many comments do you need?: "))
    numberofcomments(comments, number, channel)

    input("\nPress Enter to exit...")

def launcherVideos():
    sleep(1)
    api_key = input("\nEnter your YouTube API key: ")
    youtube = youtube_api_key(api_key)

    keywords, region, age, duration, which_order = searching_for_videos()

    collect_videos(youtube, keywords, region, age, duration, which_order)

if __name__ == "__main__":
    print("What do you need to explore?")
    sleep(1)
    question = int(input("Comments - 1; Videos - 2; Channels - 3: "))
    if question == 1:
        launcherComments()
    elif question == 2:
        launcherVideos()
    # elif question == 3:
    #     launcherChannels()