from time import sleep

from modules.mock.controller import MockController
from modules.mock.sensor import MockSensor
from publishers.slack import SlackPublisher

controllers = []


def main():
    print("Loading PlantB modules...")
    
    controllers.append(MockController(MockSensor(1,2,3)))
    start()


def start():
    print("Starting controllers...")

    for controller in controllers:
        controller.setup()

    print("Initializing publishers...")

    publishers = [SlackPublisher()]

    while True:
        result = "Moisture: " + controllers[0].probe()

        for publisher in publishers:
            publisher.publish(result)
        sleep(3600)


if __name__ == '__main__':
    main()