from flask import Flask, render_template

app = Flask(__name__)
session = False
sessionstart = None


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/startsession")
def start():
    pass


@app.route("/endsession")
def end():
    pass


@app.route("/time")
def get_time():
    pass


@app.route("/checksession")
def get_session():
    pass


if __name__ == "__main__":
    app.run("localhost", 8080)
