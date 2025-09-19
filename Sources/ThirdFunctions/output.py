from datetime import datetime
import os


def output_channel(result, statrequests, snistics):
    os.system("cls")
    print(f"Channel: {snistics["title"]}\n"
          f"https://www.youtube.com/channel/{snistics["channelId"]}\n"
          f"CustomUrl: {snistics["customUrl"]}\n"
          f"Description:\n   {snistics["description"]}\n"
          f"{snistics["subscriberCount"]} subs; {snistics["videoCount"]} videos; {snistics["viewCount"]} views.\n"
          f"Registration date: {snistics["publishedAt"]}\n")
    print("-" * 50)
    print(f"\nThree videos from the newest:\n")
    
    number = 0
    for item in statrequests["items"]:
        title_video = item["snippet"]["title"]
        videos_id = item["id"]
        vpublished_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(vpublished_at.replace("Z", "+00:00"))
        vformatted_date = dt.strftime("%d.%m.%Y")

        ch_likes = result.get(videos_id, {}).get("likes", "No")
        ch_dislikes = result.get(videos_id, {}).get("dislikes", "No")
        ch_views = result.get(videos_id, {}).get("viewCount", "No")
        ch_comments = item["statistics"].get("commentCount", "No")

        number += 1

        print(
            f"{number}.\n"
            f"{title_video}\n"
            f"https://www.youtube.com/watch?v={videos_id}\n"
            f"{ch_views} views; {ch_likes} likes; {ch_dislikes} dislikes; {ch_comments} comments\n"
            f"{vformatted_date}\n")