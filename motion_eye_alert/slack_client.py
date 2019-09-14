# Python 2.7.10
# slack_client.py

import requests
import os

SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')


class SlackClient(object):
    @staticmethod
    def notify(server_url, snapshot_url, camera_name):
        """Make a REST call to Slack webhook with an associated movie url to be included in message"""

        payload = {
            "channel": SLACK_CHANNEL,
            "attachments": [
                {
                    "fallback": "See " + server_url + " for the latest message",
                    "color": "#317CAD",
                    "pretext": "Something has been seen on the <" + server_url + "|MotionEye Camera>",
                    "author_name": camera_name,
                    "author_link": server_url,
                    "image_url": snapshot_url
                }
            ]
        }

        return requests.post(SLACK_WEBHOOK_URL, json=payload)

        # --------------------------------------------------------------------------#
