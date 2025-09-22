from CommentExplorer import youtube_id_finder, youtube_filters
from FirstFunctions.collecting_info import collect_comments, channel_name
from FirstFunctions.output import count_keys, number_comments
from VideoExplorer import searching_for_videos
from SecondFunctions.collecting_info import collect_searches, collect_stats
from SecondFunctions.output import output_videos
from Starter.KeyExplorer import youtube_api_key, window_title
from Starter.QuotaExplorer import test_quota
from ChannelExplorer import get_info, get_answer
from ThirdFunctions.collecting_info import * #collect_channel_info, collect_popular_videos, collect_statistics
from ThirdFunctions.output import output_channel_info
from Patterns.asyncRYD import ryd
from Patterns.SearchingSecondThird import search_engine
from time import sleep
from sys import exit
import asyncio
import os


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
    
    os.system('cls')
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
    for_id, for_handle = get_info()

    get_answers = get_answer()

    snistics, uploads_videos, exc = collect_channel_info(youtube, for_id, for_handle)
    if exc:
        os.system('cls')
        return
    
    if get_answers == "y":

        keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension = search_engine()

        video_Ids, exc = search_channel_videos(youtube, snistics, keywords, ageAfter, ageBefore, duration, maximum, which_order, dimension)
        if exc:
            os.system('cls')
            return
        
        result = asyncio.run(ryd(video_Ids))

        statrequests, exc = collect_channel_stats_videos(youtube, video_Ids)
        if exc:
            os.system('cls')
            return

        output_channel_info(result, statrequests, get_answers, snistics)

    elif get_answers == "n":
        videoIds, exc = collect_popular_videos(youtube, uploads_videos)
        if exc:
            os.system('cls')
            return

        result = asyncio.run(ryd(videoIds))

        statrequests, exc = collect_statistics(youtube, videoIds)
        if exc:
            os.system('cls')
            return
        
        output_channel_info(result, statrequests, get_answers, snistics)

    input("\nPress Enter to return...")

def launcherLikedDis(youtube):

    input("\nPress Enter to return...")

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

        questionist = input("Comments - 1; Videos - 2; Channels - 3; Exit - 0: ") # Liked-Disliked Videos - 4
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
            # elif questionist == '4':
            #     launcherLikedDis(youtube)
            #     break
            elif questionist == '0':
                exit(0)
            else:
                questionist = input("\nEnter again: ")