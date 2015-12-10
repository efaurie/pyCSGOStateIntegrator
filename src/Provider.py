class Provider:
    def __init__(self):
        self.provider = None

    @property
    def name(self):
        return self.provider['name']

    @property
    def appid(self):
        return self.provider['appid']

    @property
    def version(self):
        return self.provider['version']

    @property
    def steamid(self):
        return self.provider['steamid']

    @property
    def timestamp(self):
        return self.provider['timestamp']

    def update(self, provider):
        self.provider = provider

    @property
    def as_string(self):
        state = ''
        state += '\tName: {0}\n'.format(self.name)
        state += '\tApp Id: {0}\n'.format(self.appid)
        state += '\tVersion: {0}\n'.format(self.version)
        state += '\tSteam Id: {0}\n'.format(self.steamid)
        state += '\tTimestamp: {0}\n'.format(self.timestamp)
        return state

