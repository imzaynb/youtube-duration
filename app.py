from flask import Flask, redirect, render_template, request, flash
import os

from helpers import (
    parse_url,
    check_valid_url,
    playlist_items_from_playlist_id,
    video_objects_from_video_ids,
    playlist_duration_from_video_objects
)

# configure application
app = Flask(__name__)

# ensure templates are auto-reloaded so we don't have to restart the app every time!
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = os.getenv("SECRET_KEY")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/duration", methods=["GET"])
def duration():
    url = request.args.get("url")

    if not url:
        flash("Please input a url into the search bar.")
        return redirect("/")
    elif not check_valid_url(url):
        flash("The url type was not valid. Please put a valid YouTube video or playlist URL into the search bar.")
        return redirect("/")

    match_type, id = parse_url(url)
    duration = 0
    if match_type == "playlist":
        playlist_items = playlist_items_from_playlist_id(id)
        if playlist_items == None:
            flash("The YouTube playlist id could not be found. Please try a different URL.")
            return redirect("/")
        video_ids = [item["contentDetails"]["videoId"] for item in playlist_items]
        videos = video_objects_from_video_ids(video_ids)
        duration = playlist_duration_from_video_objects(videos)
    elif match_type == "video":
        video = video_objects_from_video_ids([id])
        if video == None:
            flash("The YouTube video id could not be found. Please try a different URL.")
            return redirect("/")
        duration = playlist_duration_from_video_objects(video)
    
    return render_template("duration.html", id=id, match_type=match_type, duration=duration)