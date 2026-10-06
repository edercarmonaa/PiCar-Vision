import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO
import time
import threading
from PIL import Image
from PIL import ImageTk
import imutils
import cv2
import os
from imutils.video import VideoStream
import numpy as np
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Application(ttk.Frame):
        
    def __init__(self, main_window, vs):
        super().__init__(main_window)
        self.vs = vs
        cascade_dir = os.environ.get("HAAR_CASCADE_DIR", getattr(cv2.data, "haarcascades", "/usr/local/share/OpenCV/haarcascades/"))
        self.cara = cv2.CascadeClassifier(os.path.join(cascade_dir, "haarcascade_frontalface_alt.xml"))
        self.thread = None
        self.panel = None
        self.frame = None
        self.izquierda = 4
        self.derecha = 27
        self.avanza = 22
        self.retrocede = 23
        self.led_derecho = 26 
        self.led_izquierdo = 16
        self.led_atras = 13
        GPIO.setup(self.izquierda, GPIO.OUT)
        GPIO.setup(self.derecha, GPIO.OUT)
        GPIO.setup(self.avanza, GPIO.OUT)
        GPIO.setup(self.retrocede, GPIO.OUT)
        GPIO.setup(self.led_derecho, GPIO.OUT)
        GPIO.setup(self.led_izquierdo, GPIO.OUT)
        GPIO.setup(self.led_atras, GPIO.OUT)
        GPIO.output(self.izquierda, GPIO.HIGH)
        GPIO.output(self.derecha, GPIO.HIGH)
        GPIO.output(self.avanza, GPIO.HIGH)
        GPIO.output(self.retrocede, GPIO.HIGH)
        main_window.title("Control de Carro")
        main_window.wm_protocol("WM_DELETE_WINDOW", self.onClose)
        main_window.configure(width=820, height=640)
        #main_window.resizable(False, False)
        self.bind_all('<Any-KeyPress>', self.keypress)
        self.bind_all('<Any-KeyRelease>', self.keyrelease)
        self.place(relwidth=1, relheight=1)
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop)
        self.thread.start()
        
        
    def videoLoop(self):
        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
        COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
        #net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
        try:
            while not self.stopEvent.is_set():
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=400)
                (h, w) = self.frame.shape[:2]
                #blob = cv2.dnn.blobFromImage(cv2.resize(self.frame, (300, 300)),0.007843, (300, 300), 127.5)
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                #net.setInput(blob)
                #detections = net.forward()
                """
                for i in np.arange(0, detections.shape[2]):
                    confidence = detections[0, 0, i, 2]
                    if confidence > 0.2:
                        idx = int(detections[0, 0, i, 1])
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")
                        label = "{}: {:.2f}%".format(CLASSES[idx],confidence * 100)
                        cv2.rectangle(self.frame, (startX, startY), (endX, endY),COLORS[idx], 2)
                        y = startY - 15 if startY - 15 > 15 else startY + 15
                        cv2.putText(self.frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
		"""
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = self.cara.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
                if self.panel is None:
                    self.panel = tk.Label(image=image)
                    self.panel.image = image
                    self.panel.pack(side="left", padx=10, pady=10)
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
        except RuntimeError:
            print("[INFO] caught a RuntimeError")

    def onClose(self):		
        print("[INFO] closing...")
        self.stopEvent.set()
        self.vs.stop()
        GPIO.output(self.izquierda, GPIO.HIGH)
        GPIO.output(self.derecha, GPIO.HIGH)
        GPIO.output(self.avanza, GPIO.HIGH)
        GPIO.output(self.retrocede, GPIO.HIGH)
        GPIO.cleanup()
        self.master.quit()
        
    def keypress(self,event):
        if event.keysym == 'Up':
            self.frente()
        elif event.keysym == 'Down':
            self.atras()
        elif event.keysym == 'Right':
            self.der()
        elif event.keysym == 'Left':
            self.izq()

    def keyrelease(self,event):
        if event.keysym == 'Up':
            GPIO.output(self.avanza, GPIO.HIGH)
        elif event.keysym == 'Down':
            GPIO.output(self.retrocede, GPIO.HIGH)
        elif event.keysym == 'Right':
            GPIO.output(self.derecha, GPIO.HIGH)
        elif event.keysym == 'Left':
            GPIO.output(self.izquierda, GPIO.HIGH)
    def frente(self):
        GPIO.output(self.avanza, GPIO.LOW)
    def atras(self):
        GPIO.output(self.retrocede, GPIO.LOW)
    def izq(self):
        GPIO.output(self.izquierda, GPIO.LOW)
    def der(self):
        GPIO.output(self.derecha, GPIO.LOW)    
        
        
def main():
    main_window = tk.Tk()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    app = Application(main_window, vs)
    app.mainloop()


if __name__ == "__main__":
    main()
