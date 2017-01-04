import config
from online_convert_client import OnlineConvertClient
from slack_client import SlackClient

SLACK_CHANNEL = config.SLACK_CHANNEL


class AlertHandler(object):
    online_convert_client = OnlineConvertClient()
    slack_client = SlackClient()

    def alert(self, file_source):
        converted_file = self.online_convert_client.convertFile(file_source)
        self.slack_client.notify(SLACK_CHANNEL, converted_file)

if __name__ == '__main__':
    AlertHandler().alert()
