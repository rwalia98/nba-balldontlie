
class BallDontLie:
    def __init__(self,):
        self.base_url = 'https://www.balldontlie.io/api/v1/'

    def build_url(self, players=False,teams=False,games=False,team_id=None,player_id=None,start_date=None,end_date=None):
        if players:
            self.base_url += 'players'
        if teams:
            self.base_url += 'teams'
        if games:
            self.base_url += 'games?'
        if player_id:
            self.base_url += f'/{player_id}'
        if team_id:
            self.base_url += f'/{team_id}'
        if start_date:
            self.base_url += f'&start_date={start_date}'
        if end_date:
            self.base_url += f'&end_date={end_date}'

        return self.base_url