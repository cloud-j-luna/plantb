import RPi.GPIO as GPIO
from modules.abstract.sensor import DigitalSensor

class MoistureSensor(DigitalSensor):

    def __init__(self, ground, vcc, gpio):
        self.ground = ground
        self.vcc = vcc
        self.gpio = gpio

    def setup(self, high, low):
        def callback(channel):  
            if GPIO.input(channel):
                high()
            else:
                low()

        GPIO.setmode(GPIO.BCM)

        channel = self.gpio
        GPIO.setup(channel, GPIO.IN)

        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
        GPIO.add_event_callback(channel, callback)