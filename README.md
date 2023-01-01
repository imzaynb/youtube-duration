# YouTube Duration

Often, when watching YouTube, I like to increase the playback rate to consume the video quicker. It's often easy to figure out the new video duration for a video, but what about for playlists?

I created the YouTube Duration app to figure out how long a YouTube playlist/video would take at higher speeds!

Simply enter in the link of a YouTube video/playlist URL and adjust the slider to the desired speed!

Visit this as a website @ [imzaynb.pythonanywhere.com](http://imzaynb.pythonanywhere.com)!

Also, here is a video demo of the app!: [https://youtu.be/hr1DW5v6IL4](https://youtu.be/hr1DW5v6IL4)

## About The Project

This project is a Flask web application using Python, HTML, CSS, JavaScript, and Bootstrap. I took a lot of inspiration from the Finance project we made for Week 9 of CS50.

As it is a Flask project, it follows many of the typical Flask program patterns (i.e. the `app.py` and `requirements.txt` files, and the `templates/` and `static/` folders). Along with that there is a `.env` file which I keep to store the `API_KEY`, and a `.gitignore` file to keep that file from being added into the GitHub repository. In addition to some `.css` and `.js` files, I keep a `favicon.ico` file in the `static/` directory as that is the icon which becomes the icon on the tab for the website.

In `app.py`, I have two routes, the index (`/`) route and the `/duration` route. The index route simply serves the home page which explains how to use the app and has an input for inputting a YouTube URL. The `GET` request sent by the home page is sent to the `/duration` route. In that route, the URL provided by the user is extracted and validated by a couple of functions. Then I have some logic which determines whether the inputted URL is a video or a playlist so I can display the right duration. That is passed into a `render_template` call along with enough information to populate an iframe with their given video/playlist.

In `helpers.py`, I have a couple of functions that calls the [YouTube Data API v3](https://developers.google.com/youtube/v3). The idea to make this app came from a YouTube video by Corey Schafer ([his channel](https://www.youtube.com/@coreyms)), in which I thought to extend his [example](https://www.youtube.com/watch?v=coZbOM6E47I) of totaling a YouTube playlist's duration into a web app! I also have a couple of functions to look at specific parts of the returned data to get the duration, etc. Finally, I have a couple of functions for validating the input from the user, just to ensure that the API won't break!

In the `templates/` directory, I have some files which use Jinja syntax to pass information from the Python into HTML. Nothing too special. I did utilize the `flash` functionalities of Flask which allows you to send messages that can be accounted for in the UI. These "flashed" messages I utilize to announce errors in what the user inputted. 

In `main.js`, I select some components in the `duration.html` file which I use to programmatically update when the user moves the slider. I also created a helper function to turn a duration of seconds into a more readable `HH:MM:SS` format.

I used [pythonanywhere.com](https://www.pythonanywhere.com) to host my website as it was the easiest host for a Flask app (according to a 10-second Google Search, that is :)). I was considering Heroku, but was kind of miffed that they removed their free tier. I will likely eventually migrate it over there though as I keep learning and deploying web apps. Like the Google Search explained, pythonanywhere was pretty easy to use, and, other than some hiccups from me not reading the instructions thoroughly, it works like a charm!

That basically sums up an overview of my program. I tried to keep the variable names verbose enough to easily understand. Also, most of the styles come from Bootstrap as I am still working on my CSS capabilities.

It seems pretty simplistic, and arguably it is, but this was the only thing I could think of making that I would legitimately use in the future. In terms of future plans, I definitely could extend this into like a Chrome/Firefox Extension or some CLI app (which would not actually be terribly hard since most of the code is on the back-end anyways). Thanks for taking interest in my project!

Zayn B.