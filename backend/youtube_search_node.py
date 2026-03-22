import os
import requests
from dotenv import load_dotenv
load_dotenv()

def youtube_search_node(state: dict) -> dict:
    api_key = os.getenv("YOUTUBE_API_KEY")
    skill = state.get("skill", "")
    
    query = f"full course {skill}"
    
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "key": api_key,
        "relevanceLanguage": "en",
        "order": "relevance"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        videos = []
        for item in data.get("items", []):
            video_id = item["id"]["videoId"]
            snippet = item["snippet"]
            videos.append({
                "video_id": video_id,
                "title": snippet["title"],
                "channel": snippet["channelTitle"],
                "thumbnail": snippet["thumbnails"]["high"]["url"],
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })
        
        state["recommended_videos"] = videos
        
    except Exception as e:
        print(f"YouTube search failed: {e}")
        state["recommended_videos"] = []
    
    return state