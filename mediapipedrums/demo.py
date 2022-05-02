import mediapipe as mp
import cv2
import numpy as np
from matplotlib import pyplot as plt
from utils import draw_drumstick,overlay_transparent,draw_drum_boxes,check_for_drum_hit

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

drum_joint_list = [
    [0,17,19],
    [6,7,4]
]
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # Change colour format from BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip image along y axis
        image = cv2.flip(image, 1)

        # Set flag to false
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)

        # Set flag back to true
        image.flags.writeable = True

        # Change colour format from RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # print(results)
        
        # Rendering results
        if results.multi_hand_landmarks:
            for idx, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

            # draw_finger_angle(image, results, joint_list)

            # Draw drumsticks and get coordinates 
            POIs = draw_drumstick(image, results, drum_joint_list)
            print(POIs)
            check_for_drum_hit(pois=POIs)

        #frame is 640 x 480
        drumkit = cv2.imread("mediapipedrums\drumkit.png",-1)
            # if drumkit == None:
            # print("fail")
        overlay = overlay_transparent(image,drumkit,0,0)
        draw_drum_boxes(overlay)
        cv2.imshow('Hand Tracking', overlay)
        

        #press q to quit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

#run these 2 if ur cam crash (copy and run somewhere else)
cap.release()
cv2.destroyAllWindows()  