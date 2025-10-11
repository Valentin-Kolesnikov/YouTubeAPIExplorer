from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import glob
import os
import sys

def youtube_OAuth2():
    try:
        if getattr(sys, "frozen", False):
            app_folder = os.path.dirname(sys.executable)
        else:
            app_folder = os.path.dirname(__file__)

        file = glob.glob(os.path.join(app_folder, "client_secret_*.json"))
        if not file:
            raise FileNotFoundError
        client_file = file[0]

        link = ["https://www.googleapis.com/auth/youtube.readonly"]

        delivery = InstalledAppFlow.from_client_secrets_file(client_file, link)
        credits = delivery.run_local_server(port=8080)

        OAuth2youtube = build("youtube", "v3", credentials=credits)

        return OAuth2youtube, False
    
    except FileNotFoundError:
        print("The file client_secret_*.json is not found.")

        input("\nPress Enter to return...")

        return {}, True