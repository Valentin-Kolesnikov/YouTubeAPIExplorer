from CommentExplorer import *
# from ChannelExplorer import *
from VideoExplorer import *
from Key import youtube_api_key
from TestQuota import test_quota
from time import sleep
import asyncio

import os

def launcherComments(youtube):
    sleep(0.6)
    url = input("\nEnter the url: ")     
    video_id = youtube_id_finder(url)
                                                
    channel, exc = channel_name(video_id, api_key)
    if exc:
        os.system('cls')
        return

    sleep(0.6)
    search_terms = []
    while True:
        terms = input("\nEnter the keywords by one (press Enter to continue): ")
        if terms == "":
            break
        search_terms.append(terms)

    search_terms = set(search_terms)

    sleep(0.6)
    which_order = youtube_which_order()

    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        os.system('cls')
        return

    count_keys(comments, search_terms)

    sleep(0.6)
    number = int(input("\nHow many comments do you need?: "))
    os.system('cls')
    numberofcomments(comments, number, channel)

    input("\nPress Enter to continue...")


def launcherVideos(youtube):
    sleep(0.6)
    keywords = input("\nEnter a request on YouTube: ")

    sleep(0.6)
    region = input("\nWhat region would you like? (Enter as US, RU, UK, etc): ")
    region.upper()
    while True:
        if len(region) == 2 and region.isalpha():
            break
        else:
            region = input("\nEnter it again: ")

    age, duration = searching_for_videos()

    sleep(0.6)
    maximum = int(input("\nHow much do you want to receive videos?: "))
    if maximum > 51:
        maximum = 50
    elif maximum < 4:
        maximum = 5
    sleep(1.2)
    os.system('cls')

    video_ids, channel_ids, exc = collect_searches(youtube, keywords, region, age, duration, maximum)
    if exc:
        os.system('cls')
        return

    results = asyncio.run(ryd(video_ids))

    statrequest, dict_channels, exc = collect_stats(youtube, video_ids, channel_ids)
    if exc:
        os.system('cls')
        return

    output_videos(results, statrequest, dict_channels)

    input("Press Enter to continue...")

    
def launcherChannels(youtube):

    input("Press Enter to continue...")

if __name__ == "__main__":
    youtube, api_key = youtube_api_key()
    print("Key is accepted!")
    sleep(0.6)

    if not test_quota(youtube):
        input("Press Enter to exit...")
        exit(1)

    while True:
        os.system('cls')
        print("What do you need to explore?")
        sleep(0.6)

        questionist = input("Comments - 1; Videos - 2; Channels - 3; Exit - 0: ")
        while True:
            if questionist == '1':
                launcherComments(youtube)
                break
            elif questionist == '2':
                launcherVideos(youtube)
                break
            elif questionist == '3':
                launcherChannels(youtube)
                break
            elif questionist == '0':
                exit(0)
            else:
                questionist = input("Enter it again: ")