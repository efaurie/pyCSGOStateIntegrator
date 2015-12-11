from SubState_Weapons import State_Weapons


class State_Player:
    def __init__(self):
        self.state_weapons = State_Weapons()
        self.state_player = None

    def update(self, state_player):
        self.state_player = state_player
        if 'weapons' in state_player.keys():
            self.state_weapons.update(state_player['weapons'])

    @property
    def steamid(self):
        try:
            return self.state_player['steamid']
        except KeyError:
            return None

    @property
    def name(self):
        try:
            return self.state_player['name']
        except KeyError:
            return None

    @property
    def team(self):
        try:
            return self.state_player['team']
        except KeyError:
            return None

    @property
    def activity(self):
        try:
            return self.state_player['activity']
        except KeyError:
            return None

    @property
    def health(self):
        try:
            return self.state_player['state']['health']
        except KeyError:
            return None

    @property
    def armor(self):
        try:
            return self.state_player['state']['armor']
        except KeyError:
            return None

    @property
    def helmet(self):
        try:
            return self.state_player['state']['helmet']
        except KeyError:
            return None

    @property
    def flashed(self):
        try:
            return self.state_player['state']['flashed']
        except KeyError:
            return None

    @property
    def smoked(self):
        try:
            return self.state_player['state']['smoked']
        except KeyError:
            return None

    @property
    def burning(self):
        try:
            return self.state_player['state']['burning']
        except KeyError:
            return None

    @property
    def money(self):
        try:
            return self.state_player['state']['money']
        except KeyError:
            return None

    @property
    def round_kills(self):
        try:
            return self.state_player['state']['round_kills']
        except KeyError:
            return None

    @property
    def round_killhs(self):
        try:
            return self.state_player['state']['round_killhs']
        except KeyError:
            return None

    @property
    def match_kills(self):
        try:
            return self.state_player['match_stats']['kills']
        except KeyError:
            return None

    @property
    def match_assists(self):
        try:
            return self.state_player['match_stats']['assists']
        except KeyError:
            return None

    @property
    def match_deaths(self):
        try:
            return self.state_player['match_stats']['deaths']
        except KeyError:
            return None

    @property
    def match_mvps(self):
        try:
            return self.state_player['match_stats']['mvps']
        except KeyError:
            return None

    @property
    def match_score(self):
        try:
            return self.state_player['match_stats']['score']
        except KeyError:
            return None

    @property
    def as_string(self):
        state = ''
        if self.steamid is not None:
            state += 'Steam ID: ' + self.steamid
        if self.name is not None:
            state += '\nName: ' + self.name
        if self.team is not None:
            state += '\nTeam: ' + self.team
        if self.activity is not None:
            state += '\nActivity: ' + self.activity
        if self.health is not None:
            state += '\nHealth: ' + str(self.health)
        if self.armor is not None:
            state += '\nArmor: ' + str(self.armor)
        if self.helmet is not None:
            state += '\nHelmet: ' + str(self.helmet)
        if self.flashed is not None:
            state += '\nFlashed: ' + str(self.flashed)
        if self.smoked is not None:
            state += '\nSmoked: ' + str(self.smoked)
        if self.burning is not None:
            state += '\nBurning: ' + str(self.burning)
        if self.money is not None:
            state += '\nMoney: ' + str(self.money)
        if self.round_kills is not None:
            state += '\nRound Kills: ' + str(self.round_kills)
        if self.round_killhs is not None:
            state += '\nRound Kills By Headshot: ' + str(self.round_killhs)
        state += self.state_weapons.as_string