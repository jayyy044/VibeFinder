from flask import Flask, request
from mainCopy import *


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return recommendTrack()


if __name__== "__main__":
    app.run(debug=True)