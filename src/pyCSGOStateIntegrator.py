import argparse

from ConfigReader import ConfigReader
from StateServer import StateServer


def init_state_integrator():
    parser = argparse.ArgumentParser()
    parser.add_argument('-config', default='../resources/state_integrator.conf', help='The path to the config file.')
    return parser.parse_args()


def run(config):
    csgo_state_integrator = StateServer(config.address, config.port)
    try:
        print '[+] Server Started - Listening For Requests'
        csgo_state_integrator.start_server()
    except KeyboardInterrupt:
        print '[+] Stopping Server...'
        csgo_state_integrator.stop_server()


if __name__ == '__main__':
    args = init_state_integrator()

    print '[+] Initializing CSGO State Integrator'
    config = ConfigReader(args.config)

    print "[+] Config Loaded: Starting Server At Address '{0}:{1}'".format(config.address, config.port)
    run(config)

    print '[+] Exiting...'
