import requests

class TrafficImg:
    def __init__(self, api_server_url):
        self.api_server_url = api_server_url

    def traffic_img(self):
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

