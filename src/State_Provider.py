class State_Provider:
    def __init__(self):
        self.state_provider = None

    @property
    def name(self):
        try:
            return self.state_provider['name']
        except KeyError:
            return None

    @property
    def appid(self):
        try:
            return self.state_provider['appid']
        except KeyError:
            return None

    @property
    def version(self):
        try:
            return self.state_provider['version']
        except KeyError:
            return None

    @property
    def steamid(self):
        try:
            return self.state_provider['steamid']
        except KeyError:
            return None

    @property
    def timestamp(self):
        try:
            return self.state_provider['timestamp']
        except KeyError:
            return None

    def update(self, state_provider):
        self.state_provider = state_provider

    @property
    def as_string(self):
        state = ''
        if self.name is not None:
            state += '\tName: {0}\n'.format(self.name)
        if self.appid is not None:
            state += '\tApp Id: {0}\n'.format(self.appid)
        if self.version is not None:
            state += '\tVersion: {0}\n'.format(self.version)
        if self.steamid is not None:
            state += '\tSteam Id: {0}\n'.format(self.steamid)
        if self.timestamp is not None:
            state += '\tTimestamp: {0}\n'.format(self.timestamp)
        return state

