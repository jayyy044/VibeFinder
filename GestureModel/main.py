import imageapp as ia
from inference_classifier import image

# Run the gesture analysis to capture and save the image
image()
ia.app.run(host='127.0.0.1', port=5000)
