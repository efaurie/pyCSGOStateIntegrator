import json


class CSGOState:
    def __init__(self):
        self.state_counter = 0
        self.csgo_state = dict()

    def load_new_state(self, json_payload):
        self.state_counter += 1
        new_state = json.load(json_payload)
        self.parse_state(new_state)

    def parse_state(self, new_state):
        for state_class, payload in new_state.iteritems():
            # We can skip these, we already hold the previous state in memory
            # and the added state can be inferred from the previous state
            if state_class == 'previously' or state_class == 'added':
                continue

            try:
                state_class_name = 'State_{0}'.format(state_class.capitalize())
                module = __import__(state_class_name)
                state_class = getattr(module, state_class_name)
                state_instance = state_class()
                state_instance.update(payload)
                self.csgo_state[state_class_name] = state_instance
            except ImportError:
                print "[-] Received state of class '{0}', but that state isn't supported...".format(state_class)

    def print_state(self):
        print '--------------- State {0} ---------------'.format(self.state_counter)
        for state_class, state in self.csgo_state.iteritems():
            print '[+] {0}: '.format(state_class.split('_')[1])
            print state.as_string
        print '--------------- End State --------------\n'
