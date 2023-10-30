import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 23
RELAIS_2_GPIO = 24
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode


def relay_on():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_2_GPIO, GPIO.LOW)

def relay_off():
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)