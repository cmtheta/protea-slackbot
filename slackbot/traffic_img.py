import requests
import tempfile
import logging

class TrafficImg:
    def __init__(self, client, messenger,api_server_url):
        self.client = client
        self.messenger = messenger
        self.api_server_url = api_server_url

    def return_traffic_img(self, channel_id: str, initial_comment=""):
        try:
            traffc_image = self.fetch_img()
        except Exception as e:
            logging.error(e)
            self.messenger.error_massage(channel_id)
            exit(1)

        with tempfile.NamedTemporaryFile(dir=".", delete=True) as f:
            f.write(traffc_image)
            filename = f.name
            # FIXME: file_upload_v2の使用をすすめられる。2023/01/21時点でv2の情報があまりなかった。
            self.client.files_upload(
                channels=channel_id,
                file=filename,
                initial_comment=initial_comment,
                title = "Traffic Data"
            )

    def fetch_img(self):
        params = {
            "provider" : "empty",
            "range": "empty",
            "area" : "empty"
        }

        r_get = requests.get(url=self.api_server_url+"/traffic_img", params=params)
        r_get.raise_for_status()

        return r_get.content

