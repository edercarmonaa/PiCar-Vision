import sys
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
izquierda = 4
derecha = 27
avanza = 22
retrocede = 23
led_derecho = 26 
led_izquierdo = 16
led_atras = 13
GPIO.setup(izquierda, GPIO.OUT)
GPIO.setup(derecha, GPIO.OUT)
GPIO.setup(avanza, GPIO.OUT)
GPIO.setup(retrocede, GPIO.OUT)
GPIO.setup(led_derecho, GPIO.OUT)
GPIO.setup(led_izquierdo, GPIO.OUT)
GPIO.setup(led_atras, GPIO.OUT)

#APAGA CARRO
print("APAGA LOS RELAYS")
GPIO.output(izquierda, GPIO.HIGH)
GPIO.output(derecha, GPIO.HIGH)
GPIO.output(avanza, GPIO.HIGH)
GPIO.output(retrocede, GPIO.HIGH)
#ENCIENDE LEDS
print("led derecho")
GPIO.output(led_derecho, GPIO.HIGH)
time.sleep(1)
GPIO.output(led_derecho, GPIO.LOW)
print("led izquierdo")
GPIO.output(led_izquierdo, GPIO.HIGH)
time.sleep(1)
GPIO.output(led_izquierdo, GPIO.LOW)
print("led atras")
GPIO.output(led_atras, GPIO.HIGH)
time.sleep(1)
GPIO.output(led_atras, GPIO.LOW)
print("AVANZA")
GPIO.output(avanza, GPIO.LOW)
time.sleep(1.58)
GPIO.output(avanza, GPIO.HIGH)
print("RETROCEDE")
GPIO.output(retrocede, GPIO.LOW)
time.sleep(1)
GPIO.output(retrocede, GPIO.HIGH)
print("IZQUIERDA")
GPIO.output(izquierda, GPIO.LOW)
time.sleep(1)
GPIO.output(izquierda, GPIO.HIGH)
print("DERECHA")
GPIO.output(derecha, GPIO.LOW)
time.sleep(1)
GPIO.output(derecha, GPIO.HIGH)
#avanza derecha
print("AVANZA DERECHA")
GPIO.output(derecha, GPIO.LOW)
GPIO.output(avanza, GPIO.LOW)
time.sleep(1)
GPIO.output(derecha, GPIO.HIGH)
GPIO.output(avanza, GPIO.HIGH)
#avanza derecha
print("atras izquierda")
GPIO.output(izquierda, GPIO.LOW)
GPIO.output(retrocede, GPIO.LOW)
time.sleep(1)
GPIO.output(izquierda, GPIO.HIGH)
GPIO.output(retrocede, GPIO.HIGH)
GPIO.cleanup

