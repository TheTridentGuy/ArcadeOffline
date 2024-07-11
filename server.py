from flask import Flask, render_template
import datetime
import json

app = Flask(__name__)
session = False
sessionstart = None
activefile = None


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/addmsg")
def add_msg():
    if not session or not sessionstart:
        return ""
    now = datetime.datetime.now()
    # noinspection PyTypeChecker
    time = now - sessionstart
    if (time.seconds / 60) > 70:
        ts = "70:00"


@app.route("/startsession")
def start():
    global sessionstart, session, activefile
    if session:
        return "null"
    session = True
    sessionstart = datetime.datetime.now()
    activefile = f"sessions/{sessionstart.strftime('%m-%d-%Y-%H:%M:%S')}.session"
    with open(activefile, "w") as f:
        json.dump({}, f)
    return json.dumps({"activefile": activefile})


@app.route("/endsession")
def end():
    pass


# noinspection PyTypeChecker
@app.route("/time")
def get_time():
    if session and sessionstart:
        now = datetime.datetime.now()
        time = now - sessionstart
        return json.dumps({"min": int(time.seconds / 60), "sec": time.seconds % 60})


@app.route("/checksession")
def get_session():
    pass


if __name__ == "__main__":
    app.run("localhost", 8080)
