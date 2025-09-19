import aiohttp
import asyncio

async def fetch_ryd(session, vid):
    ryd_url = f"https://returnyoutubedislikeapi.com/votes?videoId={vid}"
    async with session.get(ryd_url) as dislike:
        if dislike.status == 200:
            return vid, await dislike.json()
        else:
            return vid, {"error": "N/A"}
        
async def ryd(video_ids):
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_ryd(session, vid) for vid in video_ids]
        responses = await asyncio.gather(*tasks)
        for vid, data in responses:
            results[vid] = data
    return results