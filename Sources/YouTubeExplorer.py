from googleapiclient.discovery import build
from CommentExplorer import *
from ChannelExplorer import channel_name
from VideoExplorer import *
from time import sleep
import os

def youtube_api_key(api_key):
    while True:
        if len(api_key) == 39:
            youtube = build('youtube', 'v3', developerKey=api_key)
            return youtube
        else:
            api_key = input("\nTry entering the API key again: ")

def launcherComments(youtube):
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
    os.system('cls')
    numberofcomments(comments, number, channel)

    input("\nPress Enter to exit...")

def launcherVideos(youtube):
    sleep(1)
    keywords, region, age, duration = searching_for_videos()
    sleep(1)
    os.system('cls')

    video_ids, channel_ids = collect_searches(youtube, keywords, region, age, duration)

    results = ryd(video_ids)

    statrequest, dict_channels = collect_stats(youtube, video_ids, channel_ids)

    output_videos(results, statrequest, dict_channels)

    input("\nPress Enter to exit...")
    


if __name__ == "__main__":
    api_key = input("\nEnter your YouTube API key: ")
    youtube = youtube_api_key(api_key)

    print("\nWhat do you need to explore?")
    sleep(1)
    question = int(input("Comments - 1; Videos - 2; Channels - 3: "))
    if question == 1:
        launcherComments(youtube)
    elif question == 2:
        launcherVideos(youtube)
    # elif question == 3:
    #     launcherChannels()