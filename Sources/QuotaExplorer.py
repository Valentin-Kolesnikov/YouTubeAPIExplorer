from googleapiclient.errors import HttpError

def test_quota(youtube):
    try:
        youtube.channels().list(
            part="snippet",
            id="UC0PhYO05DXdztwxvRSDfSiw"
        ).execute()
        return True

    except HttpError as exc:
        status = exc.resp.status
        if status == 403:
            print(f"\u001b[31mYou exceeded your YouTube API quota. Error: 403\u001b[0m")
        else:
            print(f"HttpError {status}")

        return False
    
    except Exception as exc:
        print(f"Exception: {exc.resp.status}")

        return False

