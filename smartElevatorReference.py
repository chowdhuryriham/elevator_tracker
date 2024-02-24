from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import imutils



def process_picture(img):
    img = imutils.resize(img, height=500)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    edged_img = cv2.Canny(blurred_img, 100, 200)
    return edged_img


camera = PiCamera()
camera.resolution = (512, 400)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(512, 400))
# clear the stream in preparation for the next frame
rawCapture.truncate(0)
time.sleep(0.3)
count = 0

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    #image = image[50:450, 75:350]
    #floor = find_floor(image)
    #print(floor)
    cv2.imshow("frame", image)
    image = process_picture(image)
    cv2.imshow("frameSaved", image)
    key= cv2.waitKey(1)
    rawCapture.truncate(0)
    if key == ord("c"):
        if count == 0:
            #image = process_picture(image)
            cv2.imwrite("0.jpg", image)
            count = count + 1
        elif count == 1:
            #image = process_picture(image)
            cv2.imwrite("1.jpg", image)
            count = count + 1
        elif count == 2:
            #image = process_picture(image)
            cv2.imwrite("2.jpg", image)
            count = count + 1
        elif count == 3:
            #image = process_picture(image)
            cv2.imwrite("3.jpg", image)
            count = count + 1
        elif count == 4:
            #image = process_picture(image)
            cv2.imwrite("4.jpg", image)
            count = count + 1
        elif count == 5:
            #image = process_picture(image)
            cv2.imwrite("5.jpg", image)
            count = count + 1
        elif count == 6:
            #image = process_picture(image)
            cv2.imwrite("6.jpg", image)
            count = count + 1
        elif count == 7:
            #image = process_picture(image)
            cv2.imwrite("7.jpg", image)
            count = count + 1
        elif count == 8:
            #image = process_picture(image)
            cv2.imwrite("8.jpg", image)
            count = count + 1
        elif count == 9:
            #image = process_picture(image)
            cv2.imwrite("9.jpg", image)
            count = count + 1        
    if key== ord("q"):
        break