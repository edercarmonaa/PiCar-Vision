from picamera.array import PiRGBArray
from picamera import PiCamera
import os
import time
import cv2

cascade_dir = os.environ.get("HAAR_CASCADE_DIR", getattr(cv2.data, "haarcascades", "/usr/local/share/OpenCV/haarcascades/"))
cara = cv2.CascadeClassifier(os.path.join(cascade_dir, "haarcascade_frontalface_alt.xml"))
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    imagen = frame.array
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    faces = cara.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow("Frame", imagen)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break
