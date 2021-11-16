from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def index():
    url = getMemeURL()
    return render_template("index.html", url=url[0], post=url[1], author=url[2])


if __name__ == "__main__":
    app.run(debug=True)
