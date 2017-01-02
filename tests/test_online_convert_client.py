import unittest

from custom_exceptions import TooManyRequests
from online_convert_client import OnlineConvertClient


class TestConvertClient(unittest.TestCase):
    def setUp(self):
        self.client = OnlineConvertClient()

    def test_success_call(self):
        test_file = "http://staticvoid.no-ip.info:9999/movie/1/download/integration-test/00-00-00.avi"
        self.client.convertFile(test_file)

    def test_fail_requesting_source_file(self):
        test_file = "http://staticvoid.no-ip.info:9999/movie/1/download/integration-test/xx-xx-xx.avi"
        self.assertRaises(TooManyRequests, self.client.convertFile, test_file)

if __name__ == '__main__':
    unittest.main()
