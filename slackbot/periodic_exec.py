import schedule
from time import sleep

from .traffic_img import TrafficImg


class PeriodicExecuter:
    def __init__(self, channel_id, trafimg: TrafficImg) -> None:
        print("Start up: Periodic Executer")
        self.trafimg = trafimg
        self.channel_id = channel_id

    def run(self):
        schedule.every().day.at("01:33").do(self.send_traffic_img_morning)

        while(True):
            schedule.run_pending()
            sleep(10)

    def send_traffic_img_morning(self):
        # Send yesterday's traffic data in the morning.
        self.trafimg.return_traffic_img(self.channel_id, initial_comment="おはようございます")
