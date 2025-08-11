from CommentExplorer import *
from ChannelExplorer import channel_name
from VideoExplorer import *
from time import sleep

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

    sleep(1)
    which_order = input("\nDo you need to sort comments? By relevance - 1; By time - 2: ")

    comments = collect_comments(video_id, search_terms, which_order, youtube)

    # save_comments(comments, search_terms)

    sleep(1)
    number = int(input("\nHow many comments do you need?: "))
    numberofcomments(comments, number, channel)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    print("What do you need to explore?")
    sleep(1)
    question = int(input("Comments - 1; Videos - 2; Channels - 3: "))
    if question == 1:
        launcherComments()