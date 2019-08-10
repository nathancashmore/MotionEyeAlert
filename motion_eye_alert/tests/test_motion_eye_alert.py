import unittest

import motion_eye_alert
from motion_eye_alert.alert_handler import AlertHandler


class TestAlertHandler(unittest.TestCase):
    def setUp(self):
        self.client = motion_eye_alert.alert_handler.AlertHandler()

    def test_success_call(self):
        self.client.alert('1', 'Motion Cam')


if __name__ == '__main__':
    unittest.main()
