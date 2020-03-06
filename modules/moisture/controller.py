class MoistureController:
    def __init__(self, sensor):
        self.sensor = sensor

    def setup(self):
        self.sensor.setup(lambda h: print(h), lambda l: print(l))