from time import sleep

from modules.mock.controller import MockController
from modules.mock.sensor import MockSensor

controllers = []


def main():
    print("Loading PlantB modules...")
    
    controllers.append(MockController(MockSensor(1,2,3)))
    start()


def start():
    print("Starting controllers...")

    for controller in controllers:
        controller.setup()

    while True:
        sleep(3)


if __name__ == '__main__':
    main()