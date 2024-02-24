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

def find_floor(inputImage):
    for i in range(10):
        img = cv2.imread(f'{i}.jpg')
        img = process_picture(img)
        check = cv2.subtract(inputImage, img)
        n_white_pix = np.sum(check == 255)
        if n_white_pix < 200:
            print(i)
            # return i
            break
    else:
        print('No floor found')
        
camera = PiCamera()
camera.resolution = (512, 400)
camera.framerate = 1
rawCapture = PiRGBArray(camera, size=(512, 400))
# clear the stream in preparation for the next frame
rawCapture.truncate(0)
time.sleep(1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    
    image = process_picture(image)
    cv2.imshow("frame", image)
    find_floor(image)
    
    key= cv2.waitKey(1)
    rawCapture.truncate(0)
    
    if key== ord("q"):
        break