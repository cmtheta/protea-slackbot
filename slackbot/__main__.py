import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import requests

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

app = App(token=SLACK_BOT_TOKEN)

API_SERVER = "http://192.168.11.9:8000"

@app.command("/hello")
def hello(ack, say, command):
    ack()
    params = {
        "name": f"<@{command['user_id']}>"
    }
    try:
        r_get = requests.get(url=API_SERVER+"/hello", params=params)
        r_get.raise_for_status()
    except Exception:
        # TODO: エラー処理
        exit(1)
    content = r_get.json()
    say(content['message'])

handler = SocketModeHandler(app, SLACK_APP_TOKEN)
handler.start()
