from flask import Flask, send_file
app = Flask(__name__)

@app.route('/', methods=['GET'])
def send_image():
    return send_file('./Final.jpg', mimetype='image/jpeg')

