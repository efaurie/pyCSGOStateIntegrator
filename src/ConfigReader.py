import ConfigParser


class ConfigReader:

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.read_config(config_path)

    @staticmethod
    def read_config(config_path):
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        return config

    @property
    def address(self):
        raw_address = self.config.get('Server Settings', 'Address')
        return raw_address

    @property
    def port(self):
        raw_port = self.config.get('Server Settings', 'Port')
        return int(raw_port)