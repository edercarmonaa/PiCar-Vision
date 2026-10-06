import lcd_i2c_driver as lcd
import os
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = int(os.environ.get("DHT_PIN", "26"))
try:
    while True:
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        lcd.lcd_string("Temperatura={0:0.1f}*".format(temperatura),lcd.LCD_LINE_1)
        lcd.lcd_string("Humedad={0:0.1f}%".format(humedad),lcd.LCD_LINE_2)
        time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    lcd.lcd_byte(0x01, lcd.LCD_CMD)
