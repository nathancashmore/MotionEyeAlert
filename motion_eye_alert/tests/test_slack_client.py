import unittest
import motion_eye_alert
import os

from motion_eye_alert.slack_client import SlackClient


class TestSlackClient(unittest.TestCase):
    def setUp(self):
        self.client = motion_eye_alert.slack_client.SlackClient()
        self.server_url = os.environ.get('MOTION_EYE_SERVER_URL')
        self.user = os.environ.get('MOTION_EYE_USER')
        self.sign = os.environ.get('MOTION_EYE_SIGNATURE')

    def test_success_call(self):
        test_url = self.server_url + \
                   "/picture/1/current/?_username=" + self.user + "&_signature=" + self.sign
        self.client.notify(os.environ.get('MOTION_EYE_SERVER_URL'), test_url, "Camera 1")


if __name__ == '__main__':
    unittest.main()
