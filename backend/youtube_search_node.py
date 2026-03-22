import os
import requests
from dotenv import load_dotenv
load_dotenv()

def youtube_search_node(state: dict) -> dict:
    api_key = os.getenv("YOUTUBE_API_KEY")
    skill = state.get("skill", "")
    level = state.get("level", "")

    # More specific query to avoid unrelated results
    query = f"{skill} full course tutorial {level} english"

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 10,          # fetch more so we can filter
        "key": api_key,
        "relevanceLanguage": "en",
        "order": "relevance",
        "videoDuration": "long",   # full courses are long videos
        "videoEmbeddable": "true",
        "safeSearch": "strict"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        skill_keywords = [kw.lower() for kw in skill.split()]

        videos = []
        for item in data.get("items", []):
            video_id = item["id"].get("videoId")
            if not video_id:
                continue

            snippet = item["snippet"]
            title = snippet["title"]

            # Filter: title must contain at least one keyword from the skill
            title_lower = title.lower()
            if not any(kw in title_lower for kw in skill_keywords):
                continue

            videos.append({
                "video_id": video_id,
                "title": title,
                "channel": snippet["channelTitle"],
                "thumbnail": snippet["thumbnails"]["high"]["url"],
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })

            if len(videos) == 5:
                break

        state["recommended_videos"] = videos

    except Exception as e:
        print(f"YouTube search failed: {e}")
        state["recommended_videos"] = []

    return state