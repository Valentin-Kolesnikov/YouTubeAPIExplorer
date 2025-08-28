from googleapiclient.discovery import build
import os
import sys

if getattr(sys, "frozen", False):
    app_folder = os.path.dirname(sys.executable)
else:
    app_folder = os.path.dirname(__file__)

key_file = os.path.join(app_folder, "api_key.txt")

class memory():
    def save_key(api_key):
        with open(key_file, "w", encoding="utf-8") as f:
            f.write(api_key)

    def load_key():
        if os.path.exists(key_file):
            with open(key_file, "r", encoding="utf=8") as f:
                return f.read().strip()
        return None

def youtube_api_key():
    api_key = memory.load_key()
    if not api_key:
        api_key = input("Enter your YouTube API key: ")
        while len(api_key) != 39:
            api_key = input("\nThis is not the YouTube API key. Try entering the API key again: ")
        memory.save_key(api_key)
    youtube = build('youtube', 'v3', developerKey=api_key)
    return api_key, youtube