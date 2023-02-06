from slack_sdk import WebClient

class Messenger:
    def __init__(self, client: WebClient):
        self.client = client

    def error_massage(self, channel_id):
        self.client.chat_postMessage(
            channel=channel_id,
            text="エラーが発生しました。\n処理を中断します。"
        )
