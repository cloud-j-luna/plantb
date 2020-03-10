import os
import slack

class MockController:
    def __init__(self, sensor):
        self.sensor = sensor

    def x(self):
        slack_token = os.environ["SLACK_PLANTB_TOKEN"]

        client = slack.WebClient(token=slack_token)

        response = client.chat_postMessage(
            channel="plantb",
            text="Help water please"
        )

        print(response)

    def setup(self):
        self.sensor.setup(lambda: self.x(), lambda: print("0"))