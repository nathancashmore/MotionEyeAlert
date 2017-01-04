# Python 2.7.10
# slack_client.py

import requests

import config

SLACK_WEBHOOK_URL = config.SLACK_WEBHOOK_URL
MOTION_EYE_SERVER_URL = config.MOTION_EYE_SERVER_URL


class SlackClient(object):
    @staticmethod
    def notify(channel, movie_url):
        """Make a REST call to Slack webhook with an associated movie url to be included in message"""

        payload = {
            "channel": channel,
            "attachments": [
                {
                    "fallback": "See " + MOTION_EYE_SERVER_URL +  "for the latest message",
                    "color": "#317CAD",
                    "pretext": "A bird has been seen !!",
                    "author_name": "MotionEye Camera",
                    "author_link": MOTION_EYE_SERVER_URL,
                    "title": "Play the last known spotting....",
                    "title_link": movie_url,
                    "footer": "Converted by <http://www.online-convert.com/|Online-Convert.com>",
                    "footer_icon": "http://cdn.online-convert.com/images/logo_meta.png"
                }
            ]
        }

        return requests.post(SLACK_WEBHOOK_URL, json=payload)

        # --------------------------------------------------------------------------#