from turtle import delay
from cv2 import dilate
import cv2
import numpy as np
"""
///picture process///

img = cv2.imread('pic\\pic1.jpg')

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('display picture', img)
cv2.waitKey(2000)
"""

"""
///video process///

video  = cv2.VideoCapture('video\\Ivyyy.mp4')

while True:
    bol, frame = video.read()
    if bol:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow('display video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('s'):
        break
"""

"""
///video(live) process///

video  = cv2.VideoCapture(0)

while True:
    bol, frame = video.read()
    if bol:
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        cv2.imshow('display video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('s'):
        break
"""

"""
///create graph with [B, G, R]///

img = np.empty((500, 500, 3), np.uint8)

for row in range(500):
    for col in range(500):
        img[row, col] = [255, 0, 0] #[B, G, R]

cv2.imshow('img', img)
cv2.waitKey(0)
"""

"""
///cut picture///

img = cv2.imread('pic\\pic1.jpg')
newimg = img[:150, 200:800]

cv2.imshow('img', img)
cv2.imshow('newimg', newimg)
cv2.waitKey(0)

"""

"""
///graph function///

kernal = np.ones((3, 3), np.uint8) # for dilate
kernal1 = np.ones((3, 3), np.uint8) # for erode

img = cv2.imread('pic\\pic4.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # picture from BGR to Gray
blur = cv2.GaussianBlur(img, (9, 9), 5) # picture Blur
canny = cv2.Canny(img, 10, 150) # picture marginalized
dilates = cv2.dilate(canny, kernal, iterations = 1) # picture dilated
erodes = cv2.erode(dilates, kernal1, iterations = 1) # picture erode


cv2.imshow('pic2', img)
cv2.imshow('pic2gray', gray) 
cv2.imshow('pic2blur', blur)
cv2.imshow('pic2canny', canny)
cv2.imshow('pic2dilate', dilates)
cv2.imshow('pic2erode', erodes)
cv2.waitKey(0)
"""

"""
///make line, rectangle, circle, text///

img = np.full((600, 600), 255, np.uint8) # create a new image(white:255) 
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # change color mod(from gray to rgb)

cv2.line(img, (0, 0), (600, 600), (255, 0, 0), 5)
cv2.rectangle(img, (200, 200), (400, 400), (0, 255, 255), cv2.FILLED)
cv2.circle(img, (500,500), 50, (0, 0, 255), 5)
cv2.putText(img, 'Wayne', (100,100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 3) # Text only use english

cv2.imshow('img', img)
cv2.waitKey(0)
"""

"""
///COLOR DETECTION///

def empty(v):
    pass

img = cv2.imread('pic\\pic2.jpg')

cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 480)

cv2.createTrackbar('Hue min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val max', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBar') #get trackbar position
    h_max = cv2.getTrackbarPos('Hue max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max]) 

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    
    cv2.waitKey(1)
"""

"""
///contours detection and identification///

img = cv2.imread('pic\\pic5.jpg')
Contours = img.copy()

cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
canny = cv2.Canny(img, 100,200)
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # find the contours and hierarchy

for cnt in contours:
    cv2.drawContours(Contours, cnt, -1, (0, 0, 255), 3) # Draw contours
    area = cv2.contourArea(cnt) # contours's area
    print(area)

    if area > 200:
        #print(cv2.arcLength(cnt, True)) # contours's length
        peri = cv2.arcLength(cnt, True) # contours's length
        vertices = cv2.approxPolyDP(cnt, peri*0.02, True) # polygon's vertices
        corners = len(vertices) # number of corners
        #print(vertices)
        x, y, w, h = cv2.boundingRect(vertices) # get rectangle information
        cv2.rectangle(Contours, (x, y), (x+w, y+h), (0, 255, 0), 4) # Draw rectangle on Contours

        if corners == 3:
            cv2.putText(Contours, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
        elif corners == 4:
            cv2.putText(Contours, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
        elif corners == 5:
            cv2.putText(Contours, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
        elif corners >= 6:
            cv2.putText(Contours, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('Contours', Contours)
cv2.waitKey(0)
"""


"""
face detection

img = cv2.imread('pic\\pic8.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('face_detected.xml')
faceRect = face.detectMultiScale(gray, 1.1, 1)
print(len(faceRect))

for(x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
"""
video  = cv2.VideoCapture(0)

while True:
    bol, frame = video.read()
    if bol:
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cv2.CascadeClassifier('face_detected.xml')
        faceRect = face.detectMultiScale(gray, 1.1, 7)
        print(faceRect)
        print(len(faceRect))

        for(x, y, w, h) in faceRect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
            cv2.imshow('display video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('s'):
        break

    
    

