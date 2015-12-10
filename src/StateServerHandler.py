import BaseHTTPServer


class StateServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self):
        pass

    def do_POST(self):
        self.send_response(200)
        print 'Headers:\n\t' + self.headers
        print '\nRequest:\n\t' + self.request
        print '\nrFile:\n\t' + self.rfile

