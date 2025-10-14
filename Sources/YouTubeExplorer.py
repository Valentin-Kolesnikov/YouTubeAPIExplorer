from Modes.YouTubeCommentExplorer import launcherComments

from Modes.YouTubeVideoExplorer import launcherVideos

from Modes.YouTubeChannelExplorer import launcherChannels

from Modes.YouTubePlaylistExplorer import launcherPlaylists

from Starter.KeyExplorer import youtube_api_key, window_title

from Starter.QuotaExplorer import test_quota

# from Starter.OAuth2 import youtube_OAuth2     I'll try to integrate or to replace YouTube API Data v3 code with OAuth2

from sys import exit

import os







if __name__ == "__main__":
    window_title("YouTubeExplorer")
    youtube, api_key = youtube_api_key()

    if not test_quota(youtube):
        input("Press Enter to exit...")
        exit(1)

    while True:
        os.system('cls')
        print("=========  v.0.8.0  =========")
        print("1. Comments\n2. Videos\n3. Channels\n4. Playlists\n0. Exit")

        questionist = input("What do you need to explore?: ") 
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
            elif questionist == '4':
                launcherPlaylists(youtube)
                break
            elif questionist == '0':
                exit(0)
            else:
                questionist = input("\nEnter again: ")