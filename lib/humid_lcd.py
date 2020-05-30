import Adafruit_DHT
import lcddriver
import datetime
import math
from phue import Bridge
from time import *

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

lcd = lcddriver.lcd()
lcd.lcd_clear()

b = Bridge('192.168.86.174')
b.connect()


def info():
    now = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        atmDisplay = "Hum:{0}% Tmp:{1}*C".format(math.floor(humidity), math.floor(temperature))
        lcd.lcd_display_string(now.strftime("%a %d %I:%M:%S"), 1)
        lcd.lcd_display_string(atmDisplay, 2)
        # adjustHues()
    else:
        lcd.lcd_display_string("Calculating...")


def adjustHues():
    b.lights[0].on = not b.lights[0].on


if __name__ == "__main__":
    while True:
        sleep(0.5)
        info()
