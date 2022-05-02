import mediapipe as mp
import cv2
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound
import time
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

drum_labels = ["ridecymbal","midtom","hightom","crashcymbal","hihats"]
drum_pos = [[(0,336),(139,415)],[(139,366),(269,480)],[(275,366),(416,480)],[(416,402),(537,455)],[(503,336),(640,402)]]
drum_playing = [False, False, False, False, False]

def play_drum(drum):
    #gotta use mp3
    #pip install playsound==1.2.2 first
    audiofile = os.path.dirname(__file__)+'/drumsounds/'+drum_labels[drum]+'.mp3'
    playsound(audiofile,False)
    drum_playing[drum]= not drum_playing[drum]

def draw_drumstick(image, results, drum_joint_list):
    '''
    Output: POIs (2D-Array)

    Returns a 2D-array for left and right hand. 

    Each element of 2D-array contains 2 coordinates (idx 0: base of drumstick, idx 1: tip of drumstick)
    '''
    
    POIs = []

    # Loops through the different hands
    for hand in results.multi_hand_landmarks:
        POI = []
        # Loops through the sets of triplet joints
        for joint in drum_joint_list:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y, hand.landmark[joint[0]].z])    # Coordinates of 1st joint
            b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y, hand.landmark[joint[1]].z])    # Coordinates of 2nd joint
            c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y, hand.landmark[joint[2]].z])    # Coordinates of 3rd joint

            joint_sim = np.add(a,b)/2
            joint_sim = np.add(joint_sim, c)/2
            joint_sim = tuple(np.multiply(joint_sim[:2], [640,480]).astype(int))

            POI.append(joint_sim)

        POI[1] =    (int((POI[1][0]-POI[0][0])*2.5 + POI[0][0]),
                    int((POI[1][1]-POI[0][1])*2.5 + POI[0][1]))
            
        POIs.append(POI)

    # print(POIs)
    # print(POIs[0][1], type(POIs[0][1]))

    for poi in POIs:

        # tip = (poi[1][0]*1.5, poi[1][1]*1.5)

        # print(f'tip: {tip}, type: {type(tip)}')

        # poi[1]: tip of drumstick (type: tuple)
        cv2.circle(image, poi[1], 10, (255,255,255),5)

        # drawing stick itself
        cv2.line(image, poi[0], poi[1], (0,128,0), 9)

    return POIs

def overlay_transparent(background, overlay, x, y):

    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background

def draw_drum_boxes(image):
    for i in drum_pos:
        cv2.rectangle(image,i[0],i[1],(255,0,0),3)

def check_for_drum_hit(pois):
    #two hand example: [[(429, 455), (376, 342)], [(124, 475), (104, 350)]]
    #one hand example: [[(124, 471), (149, 331)]]
    for drum in range(len(drum_pos)):
        noofpts_inside = 0
        for point in pois:
            if point[1][0] > drum_pos[drum][0][0] and point[1][0] < drum_pos[drum][1][0] and point[1][1] > drum_pos[drum][0][1] and point[1][1] < drum_pos[drum][1][1]:
                print('DRUM SOUND')
                noofpts_inside+=1
                if(drum_playing[drum] == False):
                    play_drum(drum)
        if(noofpts_inside==0):
            drum_playing[drum] = False
                