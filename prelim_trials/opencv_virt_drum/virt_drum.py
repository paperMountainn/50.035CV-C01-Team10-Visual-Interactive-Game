from curses import newpad, nocbreak
from decimal import getcontext
from unicodedata import numeric
import cv2
import numpy as np
from make_sound import play_snare, play_hihat, play_tom
import time

# if you only have 1 webcam, 0 iplay_drums the default webcam
# if you have more than 1, add the id as you go along

# define webcam object
cap = cv2.VideoCapture(0)

# of specific size, 3 is width, 4 is height
# frameWidth = 640
# frameHeight = 480
frameWidth, frameHeight = 1280, 720 #(720p)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# change brightness according to the id
cap.set(10, 150)

# define a list of colors of min and max for the hues
myColors = [[105, 67, 100, 128, 255, 255],
            [0, 165, 192, 179, 255, 255]
            ]

# points to loop around
myPoints = [] #[x, y, colorId]

# format of BGR -> draw the circle tip based on these values
myColorValues = [[255, 0, 0], [0, 0, 255]]

# define function to find color
def findColor(img, myColors, myColorValues):
    # convert to hsv space
    imgHSV = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2HSV
    )

    count = 0
    newPoints = []
     # create mask to filter out the car of interest
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])

        # filter out and give us the filtered image of that color
        mask = cv2.inRange(
            imgHSV,
            lower,
            upper

        )
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1
        
        cv2.imshow(str(color[0]), mask)
    return newPoints
    

# get contours func
def getContours(img):
    # 2: retrieval method: retrieve extreme outer contours, good for outer corners
    # 3: approximation: compressed values (SIMPLE) or all of it (NONE)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt) 
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, closed=True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, closed=True )

            # draw bounding box for the shapes detected
            x, y, w, h = cv2.boundingRect(approx)
    # give top point
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
        
def playSound_snare(myPoints, snare_x, snare_y, snare_w):
    for point in myPoints:
        if (snare_x < point[0] < snare_x + snare_w) and (snare_y < point[1] < snare_y + snare_w):
            play_snare()
            print(f"coordinates in snare: {(point[0], point[1])}")
            break

def playSound_hihat(myPoints, hihat_x, hihat_y, hihat_w):
    for point in myPoints:
        if (hihat_x < point[0] < hihat_x + hihat_w) and (hihat_y < point[1] < hihat_y + hihat_w):
            play_hihat()
            print(f"coordinates in snare: {(point[0], point[1])}")
            break

def playSound_tom(myPoints, tom_x, tom_y, tom_w):
    for point in myPoints:
        if (tom_x < point[0] < tom_x + tom_w) and (tom_y < point[1] < tom_y + tom_w):
            play_tom()
            print(f"coordinates in snare: {(point[0], point[1])}")
            break

# need a while loop to go through each frame one by one
while True:
    # save img in the variable, and tell us if it is succ
    success, img = cap.read()
    img = cv2.flip(img, 1) # mirrors input, flipped to correct mirroring
    
    # final info image on here:
    imgResult = img.copy()

    # bounding box representing hihat, snare, tom
    hihat_x, hihat_y, hihat_w = 270, 360, 100
    snare_x, snare_y, snare_w = 590, 540, 100
    tom_x, tom_y, tom_w = 910, 360, 100
    #hihat
    cv2.rectangle(imgResult,(hihat_x, hihat_y),(hihat_x + hihat_w, hihat_y + hihat_w),(0,255,0),3)
    cv2.putText(imgResult, 'hihat', (hihat_x + hihat_w, hihat_y + hihat_w), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    #snare
    cv2.rectangle(imgResult,(snare_x, snare_y),(snare_x + snare_w, snare_y + snare_w),(0,255,0),3)
    cv2.putText(imgResult, 'snare', (snare_x + snare_w, snare_y + snare_w), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    #tom
    cv2.rectangle(imgResult,(tom_x, tom_y),(tom_x + tom_w, tom_y + tom_w),(0,255,0),3)
    cv2.putText(imgResult, 'tom', (tom_x + tom_w, tom_y + tom_w), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)


    # add on to points
    newPoints = findColor(img, myColors, myColorValues)

    # check if newPoints are actuallythere
    if len(newPoints)!=0:
        for newPoint in newPoints:
            myPoints.append(newPoint)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)
        playSound_snare(myPoints, snare_x, snare_y, snare_w)
        playSound_hihat(myPoints, hihat_x, hihat_y, hihat_w)
        playSound_tom(myPoints, tom_x, tom_y, tom_w)
        myPoints = []

    # show result
    cv2.imshow("webcam vid", img)
    cv2.imshow("contour", imgResult)

    # add delay to break out of the loop -> adds a delay and looks for key press 'q
    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break


