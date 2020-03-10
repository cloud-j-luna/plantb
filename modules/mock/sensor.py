from modules.abstract.sensor import DigitalSensor
from utils.setinterval import set_interval

class MockSensor(DigitalSensor):

    def __init__(self, ground, vcc, gpio):
        self.ground = ground
        self.vcc = vcc
        self.gpio = gpio

    def setup(self, high, low):
        set_interval(high, 1)