import unittest

import motion_eye_alert
import motion_eye_alert.config
from motion_eye_alert.custom_exceptions import TooManyRequests
from motion_eye_alert.online_convert_client import OnlineConvertClient


class TestConvertClient(unittest.TestCase):
    def setUp(self):
        self.client = motion_eye_alert.online_convert_client.OnlineConvertClient()

    def test_success_call(self):
        test_file = motion_eye_alert.config.MOTION_EYE_SERVER_URL + "/movie/1/download/integration-test/00-00-00.avi"
        self.client.convertFile(test_file)

    def test_fail_requesting_source_file(self):
        test_file = motion_eye_alert.config.MOTION_EYE_SERVER_URL + "/movie/1/download/integration-test/xx-xx-xx.avi"
        self.assertRaises(TooManyRequests, self.client.convertFile, test_file)

if __name__ == '__main__':
    unittest.main()
