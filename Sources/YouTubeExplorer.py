from CommentExplorer import *
from ChannelExplorer import channel_name
from VideoExplorer import *
from time import sleep
from Key import youtube_api_key
import os

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
    keywords = input("\nEnter a request on YouTube: ")

    sleep(1)
    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ")
    region.upper()

    age, duration = searching_for_videos()

    sleep(1)
    maximum = int(input("\nHow much do you want to receive videos?: "))
    if maximum > 51:
        maximum = 50
    elif maximum < 0:
        maximum = 5
    sleep(2)
    os.system('cls')

    video_ids, channel_ids = collect_searches(youtube, keywords, region, age, duration, maximum)

    results = ryd(video_ids)

    statrequest, dict_channels = collect_stats(youtube, video_ids, channel_ids)

    output_videos(results, statrequest, dict_channels)

    input("\nPress Enter to exit...")
    
def launcherChannels(youtube):

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    youtube, api_key = youtube_api_key()
    os.system('cls')
    print("Key is accepted!")
    sleep(1)
    print("\nWhat do you need to explore?")
    sleep(1)
    question = int(input("Comments - 1; Videos - 2; Channels - 3: "))
    if question == 1:
        launcherComments(youtube)
    elif question == 2:
        launcherVideos(youtube)
    elif question == 3:
        launcherChannels(youtube)