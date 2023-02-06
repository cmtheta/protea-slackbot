import os
from slack_bolt import App
from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

import requests
import tempfile

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)

API_SERVER_DOMAIN = os.getenv("API_SERVER_DOMAIN")
API_SERVER_URL = "http://" + API_SERVER_DOMAIN

@app.command("/hello")
def hello(ack, say, command):
    ack()
    params = {
        "name": f"<@{command['user_id']}>"
    }
    try:
        r_get = requests.get(url=API_SERVER_URL+"/hello", params=params)
        r_get.raise_for_status()
    except Exception:
        # TODO: エラー処理
        exit(1)
    content = r_get.json()
    say(content['message'])

@app.command("/traffic_img")
def traffic_img(ack, say, command):
    ack()
    params = {
        "provider" : "empty",
        "range": "empty",
        "area" : "empty"
    }
    try:
        r_get = requests.get(url=API_SERVER_URL+"/traffic_img", params=params)
        r_get.raise_for_status()
    except Exception:
        # TODO: エラー処理
        exit(1)

    traffc_image = r_get.content
    with tempfile.NamedTemporaryFile(dir=".", delete=True) as f:
        f.write(traffc_image)
        filename = f.name
        # FIXME: file_upload_v2の使用をすすめられる。2023/01/21時点でv2の情報があまりなかった。
        client.files_upload(
            channels=command['channel_id'],
            file=filename,
            initial_comment="",
            title = "Traffic Data"
        )


handler = SocketModeHandler(app, SLACK_APP_TOKEN)
handler.start()
