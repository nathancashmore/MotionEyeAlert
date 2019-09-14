import sys
import os
import logging

from slack_client import SlackClient

MOTION_EYE_SERVER_URL = os.environ.get('MOTION_EYE_SERVER_URL')
MOTION_EYE_USER = os.environ.get('MOTION_EYE_USER')
MOTION_EYE_SIGNATURE = os.environ.get('MOTION_EYE_SIGNATURE')

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

class AlertHandler(object):
    slack_client = SlackClient()

    def alert(self, camera_id, name):
        snapshot_url = MOTION_EYE_SERVER_URL + "/picture/" + camera_id + "/current/" + '?_username=admin&_signature=' + MOTION_EYE_SIGNATURE
        logging.info('snapshot url set to %s', snapshot_url)
        self.slack_client.notify(MOTION_EYE_SERVER_URL, snapshot_url, name)


if __name__ == '__main__':
    AlertHandler().alert(sys.argv[1], sys.argv[2])
