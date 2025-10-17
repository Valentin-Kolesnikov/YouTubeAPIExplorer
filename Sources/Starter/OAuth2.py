from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import glob
import os
import sys

link = ["https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/youtube.force-ssl"]


if getattr(sys, "frozen", False):
    app_folder = os.path.dirname(sys.executable)
else:
    app_folder = os.path.dirname(__file__)


key_folder = os.path.join(app_folder, "Keys")
os.makedirs(key_folder, exist_ok=True)


token_dir = os.path.join(key_folder, "Client_token.json")


def credentials(client_file):
    credits = None
    if os.path.exists(token_dir):
        credits = Credentials.from_authorized_user_file(token_dir, link)
    

    if not credits or not credits.valid:
        if credits and credits.expired and credits.refresh_token:
            credits.refresh(Request())

        else:    
            delivery = InstalledAppFlow.from_client_secrets_file(os.path.join(key_folder, client_file), link)
            credits = delivery.run_local_server(port=8080)

            with open(token_dir, "w") as ct:
                ct.write(credits.to_json())
    
    return credits


def youtube_OAuth2():
    try:
        file = glob.glob(os.path.join(key_folder, "client_secret_*.json"))
        if not file:
            raise FileNotFoundError
        client_file = file[0] 
        

        credits = credentials(client_file)


        OAuth2youtube = build("youtube", "v3", credentials=credits)

        return OAuth2youtube, False
    
    except FileNotFoundError:
        print("The file client_secret_*.json is not found.")

        input("\nPress Enter...")

        return {}, True