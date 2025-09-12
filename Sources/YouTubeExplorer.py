from CommentExplorer import *
from VideoExplorer import *
from KeyExplorer import youtube_api_key, window_title
from QuotaExplorer import test_quota
from time import sleep
import asyncio
import os
import sys

def launcherComments(youtube):
    video_id = youtube_id_finder()

    sleep(0.6)
    which_order, search_terms = youtube_filters()

    comments, exc = collect_comments(video_id, search_terms, which_order, youtube)
    if exc:
        os.system('cls')
        return
    
    channel, exc = channel_name(video_id, api_key)
    if exc:
        os.system('cls')
        return
    
    count_keys(comments, search_terms)

    sleep(0.6)
    number_comments(comments, channel)

    input("\nPress Enter to return...")


def launcherVideos(youtube):
    keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension = searching_for_videos()

    sleep(1.2)
    os.system('cls')

    video_ids, channel_ids, exc = collect_searches(youtube, keywords, region, ageAfter, ageBefore, duration, maximum, which_order, dimension)
    if exc:
        os.system('cls')
        return

    results = asyncio.run(ryd(video_ids))

    statrequest, dict_channels, exc = collect_stats(youtube, video_ids, channel_ids)
    if exc:
        os.system('cls')
        return

    output_videos(results, statrequest, dict_channels)

    input("Press Enter to return...")

    
def launcherChannels(youtube):

    input("Press Enter to return...")

if __name__ == "__main__":
    window_title("YouTube Explorer")
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
                sys.exit(0)
            else:
                questionist = input("Enter again: ")