import datetime

import cv2
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)   #getting width of window
height = GetSystemMetrics(1)   #getting height of window
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')     #for encoding and decoding
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))    #saving video
print("WEBCAM? \n 1= Yes\n 2= NO")
n= int(input())

if(n==1):
    webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))  # grabing image from screen
    img_np = np.array(img)      #converting it into a array of image data
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)     #fixing color of output file

    if(n==1):
        _,frame = webcam.read()
        fr_height, fr_width, _ = frame.shape
        img_final[0:fr_height, 0:fr_width, :] = frame[0: fr_height, 0: fr_width, :]  #embedding webcam on screen forever
    cv2.imshow('screen', img_final)      #showing window
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break