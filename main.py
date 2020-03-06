from modules.moisture.controller import MoistureController
from modules.moisture.sensor import MoistureSensor

controllers = []

def main():
    print("Loading PlantB modules...")
    
    controllers.append(MoistureController(MoistureSensor(1,2,3)))
    start()

def start():
    print("Starting controllers...")

    for controller in controllers:
        controller.setup()

    while True:
        sleep(0.1)


if __name__ == '__main__':
    main()