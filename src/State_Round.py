class State_Round:
    def __init__(self):
        self.state_round = None

    @property
    def phase(self):
        try:
            return self.state_round['phase']
        except KeyError:
            return None

    @property
    def as_string(self):
        state = ''
        if self.phase is not None:
            state += '\tPhase: ' + self.phase

        return state

    def update(self, state_round):
        self.state_round = state_round