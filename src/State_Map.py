class State_Map:
    def __init__(self):
        self.state_map = None

    @property
    def mode(self):
        try:
            return self.state_map['mode']
        except KeyError:
            return None

    @property
    def name(self):
        try:
            return self.state_map['name']
        except KeyError:
            return None

    @property
    def phase(self):
        try:
            return self.state_map['phase']
        except KeyError:
            return None

    @property
    def round(self):
        try:
            return self.state_map['round']
        except KeyError:
            return None

    @property
    def team_ct_score(self):
        try:
            return self.state_map['team_ct']['score']
        except KeyError:
            return None

    @property
    def team_t_score(self):
        try:
            return self.state_map['team_t']['score']
        except KeyError:
            return None

    @property
    def as_string(self):
        state = ''
        if self.mode is not None:
            state += '\tMode: ' + self.mode
        if self.name is not None:
            state += '\n\tMap: ' + self.name
        if self.phase is not None:
            state += '\n\tPhase: ' + self.phase
        if self.round is not None:
            state += '\n\tRound: ' + str(self.round)
        if self.team_ct_score is not None:
            state += '\n\tCT Score: ' + str(self.team_ct_score)
        if self.team_t_score is not None:
            state += '\n\tT Score: ' + str(self.team_t_score)

        return state

    def update(self, state_map):
        self.state_map = state_map
