from flask import Flask, redirect, render_template, request, session

# configure application
app = Flask(__name__)

# ensure templates are auto-reloaded so we don't have to restart the app every time!
app.config["TEMPLATES_AUTO_RELOAD"] = True

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
    print(url)
    return redirect("/")