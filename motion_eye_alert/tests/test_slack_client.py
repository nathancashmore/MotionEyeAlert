import unittest

import motion_eye_alert
import motion_eye_alert.config
from motion_eye_alert.slack_client import SlackClient


class TestSlackClient(unittest.TestCase):
    def setUp(self):
        self.client = motion_eye_alert.slack_client.SlackClient()

    def test_success_call(self):
        test_url = motion_eye_alert.config.MOTION_EYE_SERVER_URL + \
                   "/movie/1/download/integration-test/BirdCam1_00-00-00.mp4"
        self.client.notify("#test", test_url)

if __name__ == '__main__':
    unittest.main()
