import imageapp as ia
from inference_classifier import image
import threading

# Run the gesture analysis to capture and save the image
image()

# Start the Flask server in a new thread
def start_flask():
    ia.app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)


# Start the Flask app after the gesture analysis is done
if __name__ == '__main__':
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()
