class MoistureController:
    def __init__(self, sensor):
        self.sensor = sensor

    def onHigh(self, value):
        print(value)

    def onLow(self, value):
        print(value)

    def setup(self):
        self.sensor.setup(lambda h: self.onHigh(h), lambda l: self.onLow(l))

    def ask_probe(self):
        return self.sensor.probe()