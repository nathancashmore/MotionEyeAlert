import sys

import config
from online_convert_client import OnlineConvertClient
from slack_client import SlackClient

SLACK_CHANNEL = config.SLACK_CHANNEL
MOTION_EYE_SERVER_URL = config.MOTION_EYE_SERVER_URL


class AlertHandler(object):
    online_convert_client = OnlineConvertClient()
    slack_client = SlackClient()

    def alert(self, camera_media_path):
        file_source = MOTION_EYE_SERVER_URL + camera_media_path
        converted_file = self.online_convert_client.convertFile(file_source)
        self.slack_client.notify(SLACK_CHANNEL, converted_file)


if __name__ == '__main__':
    AlertHandler().alert(sys.argv[1:])
