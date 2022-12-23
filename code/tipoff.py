
import json
import requests
from datetime import datetime
from balldontlie import BallDontLie

class TipOff:
    def __init__(self,):
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.bdl = BallDontLie()

    def pretty(self,data):
        print(json.dumps(data, indent=3, default=str))

    def run(self):
        self.get_schedule()

    def get_schedule(self):
        schedule_url = self.bdl.build_url(games=True,start_date=self.today,end_date=self.today)
        self.schedule_data = self.get_data(schedule_url)
        self.pretty(self.schedule_data)

    def get_data(self, url):
        print(f'Making a call to {url}')

        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return r.json()['data']
