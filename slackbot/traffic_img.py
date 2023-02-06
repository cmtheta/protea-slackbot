import requests
import tempfile

class TrafficImg:
    def __init__(self, client, api_server_url):
        self.client = client
        self.api_server_url = api_server_url

    def return_traffic_img(self, chanel_id: str, initial_comment=""):
        traffc_image = self.fetch_img()
        with tempfile.NamedTemporaryFile(dir=".", delete=True) as f:
            f.write(traffc_image)
            filename = f.name
            # FIXME: file_upload_v2の使用をすすめられる。2023/01/21時点でv2の情報があまりなかった。
            self.client.files_upload(
                channels=chanel_id,
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

        try:
            r_get = requests.get(url=self.api_server_url+"/traffic_img", params=params)
            r_get.raise_for_status()
        except Exception:
            # TODO: エラー処理
            exit(1)
        return r_get.content

