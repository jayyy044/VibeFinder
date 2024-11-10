import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try changing the camera index to 0
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        cv2.rectangle(frame, (440,0), (640,40),(255,255,255),-1)
        cv2.rectangle(frame, (220,440), (420,480),(255,255,255),-1)
        cv2.putText(frame,"Start",(280,470),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
        cv2.putText(frame,"Quit",(500,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
        cv2.putText(frame,"Image Dataset Collection",(25,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"Before Starting Make Sure You Are In A Well",(25,75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"Lit Room",(295,95),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"When You Are Ready Pick A Hand To Use With The Program",(25,100),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"With That Hand Create An L Sign With Your Hand",(25,150),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"When The Images Are Being Taken Slowly Move The Hand Towards And Away From The Camera Until All The Images Are Taken",(25,175),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.putText(frame,"Press Start When Ready",(25,200),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
