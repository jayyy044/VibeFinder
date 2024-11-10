import pickle
import cv2
import mediapipe as mp
import numpy as np
import os
def image():
    model_dict = pickle.load(open('model.p', 'rb'))
    model = model_dict['model']

    cap = cv2.VideoCapture(1)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.9)

    labels_dict = {0: 'A', 1: 'B', 2: 'L'}

    counter = 0
    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            prediction = model.predict([np.asarray(data_aux)])
            if len(prediction) > 0:
                predicted_character = labels_dict[int(prediction[0])]
                if predicted_character == 'A':
                    counter += 1
                else:
                    counter = 0
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        if counter == 10:
            break
        if cv2.waitKey(25) == ord('q'):
            break

    for i in range(200):
        ret, frame = cap.read()
        if i < 50:
            cv2.putText(frame,"Get Ready For Picture",(25,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        if 50 <= i < 100:
            cv2.putText(frame,"3",(25,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        if 100 <= i < 150:
            cv2.putText(frame,"2",(25,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        if 150 <= i < 200:
            cv2.putText(frame,"1",(25,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    ret, frame = cap.read()
    cv2.imwrite('./Final.jpg', frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()