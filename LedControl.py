from time import sleep
import RPi.GPIO as GPIO
import adafruit_ds1841
from adafruit_extended_bus import ExtendedI2C as I2C

def potencjometr():
    i2c = I2C(0)
    GPIO.setmode(GPIO.BCM)
    ds1841 = adafruit_ds1841.DS1841(i2c)
    ds1841.wiper=127
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, 1)

    while True:
        GPIO.output(RELAIS_1_GPIO, 0)
        sleep(0.2)
        ds1841.wiper=75
        sleep(0.2)
        ds1841.wiper=50
        sleep(0.2)
        ds1841.wiper=25
        sleep(0.2)
        ds1841.wiper=3
        #At this point, the function that examines the PV panel should be called.
        sleep(0.2)
        GPIO.output(RELAIS_1_GPIO, 1)
        GPIO.output(BENNING_PV_GPIO, 1)
        ds1841.wiper=127
        break