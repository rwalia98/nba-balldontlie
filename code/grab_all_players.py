
'''
Because balldontlie API does not have an easy way to grab all players ID, this script can be used to quickly grab all players
'''

import requests
import json

class GrabAllPlayers:
    def __init__(self):
        self.all_data = []

    def pretty(self,data):
        print(json.dumps(data, indent=3, default=str))

    def grab_players(self):

        next_page = 1
        while next_page:
            r = requests.get(f'https://www.balldontlie.io/api/v1/players?per_page=100&page={next_page}').json()

            next_page = r['meta']['next_page']

            for item in r['data']:
                self.all_data.append(item)

        f = open('player_data.json', 'w')
        f.write(json.dumps(self.all_data))
        f.close()
        print('Done')
        # self.pretty(self.all_data)


