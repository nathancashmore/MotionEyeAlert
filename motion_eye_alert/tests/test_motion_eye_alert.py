import unittest

import motion_eye_alert
import motion_eye_alert.config
from motion_eye_alert.alert_handler import AlertHandler


class TestAlertHandler(unittest.TestCase):
    def setUp(self):
        self.client = motion_eye_alert.alert_handler.AlertHandler()

    def test_success_call(self):
        test_file = motion_eye_alert.config.MOTION_EYE_SERVER_URL + "/movie/1/download/integration-test/00-00-00.avi"
        self.client.alert(test_file)


if __name__ == '__main__':
    unittest.main()
