
import json
import requests
import pandas as pd
from datetime import datetime
from balldontlie import BallDontLie
from grab_all_players import GrabAllPlayers

class TipOff:
    def __init__(self,):
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.team_ids = []
        self.team_names = []


    def pretty(self,data):
        print(json.dumps(data, indent=3, default=str))

    def run(self):

        self.get_schedule()
        self.get_teams()

    def get_schedule(self):
        schedule_url = self.ball_dont_lie(games=True,start_date=self.today,end_date=self.today)
        self.schedule_data = self.get_data(schedule_url)['data']
        # self.pretty(self.schedule_data)

    def get_teams(self):
        for game in self.schedule_data:
            if game['home_team']:
                self.team_ids.append(game['home_team']['id'])
                self.team_names.append(game['home_team']['full_name'])

            if game['visitor_team']:
                self.team_ids.append(game['visitor_team']['id'])
                self.team_names.append(game['visitor_team']['full_name'])

        print(self.team_ids)
        print(self.team_names)

    def get_data(self, url):
        print(f'Making a call to {url}')

        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return r.json()

    def ball_dont_lie(self, players=False,teams=False,games=False,team_id=None,player_id=None,start_date=None,end_date=None):
        bdl = BallDontLie()
        return bdl.build_url(players=players,teams=teams,games=games,team_id=team_id,player_id=player_id,start_date=start_date,end_date=end_date)

    # Only use to grab all players and their player ID
    def grab_all_players(self):
        gap = GrabAllPlayers()
        gap.grab_players()
        exit()
