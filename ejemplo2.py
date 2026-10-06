import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
try:
    while(True):
        GPIO.output(17,True)
        time.sleep(1)
        GPIO.output(17,False)
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa terminado por el Usuario")
finally:
    GPIO.cleanup()
