import os
import slack


class SlackPublisher:

    def __init__(self):
        slack_token = os.environ["SLACK_PLANTB_TOKEN"]

        self.client = slack.WebClient(token=slack_token)

    def publish(self, result):
        self.client.chat_postMessage(
            channel="plantb",

            text="Hey! This is how I feel:\n" + result
        )