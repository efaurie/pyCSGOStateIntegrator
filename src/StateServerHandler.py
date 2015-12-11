from CSGO_State import CSGOState
from BaseHTTPServer import BaseHTTPRequestHandler


class StateServerHandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        self.state = CSGOState()
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        self.send_response(200)
        self.state.load_new_state(self.rfile)
        self.state.print_state()

    def do_GET(self):
        self.not_allowed('GET')

    def do_PUT(self):
        self.not_allowed('PUT')

    def not_allowed(self, message_type):
        self.send_response(406)
        print '[-] {0} Received: This server only expects POSTs'.format(message_type)

    def log_message(self, message_format, *args):
        pass
