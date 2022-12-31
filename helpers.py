import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import re
from datetime import timedelta
from functools import reduce
from urllib.parse import urlparse

load_dotenv()
API_KEY = os.getenv("API_KEY")

# TODO: make async await
def playlist_items_from_playlist_id(id: str) -> list[dict]:
    youtube = build("youtube", "v3", developerKey=API_KEY)
    
    page_token = ""
    playlist_items = []
    while True:
        request = youtube.playlistItems().list(part="contentDetails", playlistId=id, pageToken=page_token)
        response = request.execute()
        playlist_items += [playlist_item for playlist_item in response["items"]]

        if "nextPageToken" in response:
            page_token = response["nextPageToken"]
        else:
            break

    return playlist_items

def video_objects_from_video_ids(ids: list[str]) -> list[dict]:
    youtube = build("youtube", "v3", developerKey=API_KEY)

    videos = []    

    while True:
        request = youtube.videos().list(
            part="contentDetails", id=",".join(ids[:min(40, len(ids))])
        )
        response = request.execute()

        videos += response["items"]

        if len(ids) > 40:
            ids = ids[40:]
        else:
            break

    return videos


def playlist_duration_from_video_objects(videos: list[dict]) -> int:
    duration_strings = [video["contentDetails"]["duration"] for video in videos]
    durations = [
        duration_from_duration_string(duration_string)
        for duration_string in duration_strings
    ]
    duration_seconds = reduce(lambda a, b: a + b, durations)
    return duration_seconds


def duration_from_duration_string(duration: str) -> float:
    hours_search = re.compile(r"(\d+)H")
    minutes_search = re.compile(r"(\d+)M")
    seconds_search = re.compile(r"(\d+)S")

    hours = hours_search.search(duration)
    minutes = minutes_search.search(duration)
    seconds = seconds_search.search(duration)

    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0

    video_seconds = timedelta(
        hours=hours, minutes=minutes, seconds=seconds
    ).total_seconds()

    return video_seconds


def parse_url(url: str) -> tuple[str]:
    video_id_pattern = re.compile(r"(v=[\w-]+)&?")
    video_match = video_id_pattern.search(url)
    
    playlist_id_pattern = re.compile(r"(list=[\w-]+)&?")
    playlist_match = playlist_id_pattern.search(url)

    if video_match:
        return ("video", video_match.group(1)[2:]) 
    elif playlist_match:
        return ("playlist", playlist_match.group(1)[5:])


def check_valid_url(url: str) -> bool:
    parse_obj = urlparse(url)
    return parse_obj.netloc == "www.youtube.com" and parse_obj.path in ["/watch", "/playlist"] and len(parse_obj.query) > 5

