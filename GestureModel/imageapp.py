from flask import Flask, send_file
# from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/image', methods=['GET'])
def send_image():
    return send_file('./Final.jpg', mimetype='image/jpeg')



# @app.route('/image', methods=['GET'])
# def send_image():
#     image_url = './Final.jpg'  # Change this to the actual path
#     return jsonify({"image_url": image_url})
