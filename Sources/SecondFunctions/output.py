from datetime import datetime





def output_videos(results, statrequest, dict_channels):
    number = 0
    for item in statrequest["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]
        published_at = item["snippet"]["publishedAt"]
        dt = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")

        likes = results.get(video_id, {}).get("likes", "No")
        dislikes = results.get(video_id, {}).get("dislikes", "No")
        views = results.get(video_id, {}).get("viewCount", "No")
        comments = item["statistics"].get("commentCount", "No")

        channel_id = item["snippet"]["channelId"]
        channel_info = dict_channels.get(channel_id, {})

        number += 1

        print(
            f"{number}.\n"
            f"{title}\n"
            f"https://www.youtube.com/watch?v={video_id}\n"
            f"{views} views; {likes} likes; {dislikes} dislikes; {comments} comments\n"
            f"{formatted_date}\n"
            f"{channel_info.get('title', 'N/A')}\n"
            f"Channel Link: https://www.youtube.com/channel/{channel_id}\n")