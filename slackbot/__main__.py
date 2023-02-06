import os
from slack_bolt import App
from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

import requests
import threading

from .periodic_exec import PeriodicExecuter
from .traffic_img import TrafficImg

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)

API_SERVER_DOMAIN = os.getenv("API_SERVER_DOMAIN")
API_SERVER_URL = "http://" + API_SERVER_DOMAIN

CHANNEL_ID = os.getenv("CHANNEL_ID")

trafimg = TrafficImg(client, API_SERVER_URL)

if CHANNEL_ID is not None:
    # 投稿先のチャンネルIDが設定されているとき、定期実行を行う
    run_method = PeriodicExecuter(CHANNEL_ID, trafimg).run
    thread_periodic_executer = threading.Thread(target=run_method)
    thread_periodic_executer.start()

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

    trafimg.return_traffic_img(command['channel_id'])


handler = SocketModeHandler(app, SLACK_APP_TOKEN)
handler.start()
