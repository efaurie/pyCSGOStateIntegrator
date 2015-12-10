from BaseHTTPServer import BaseHTTPRequestHandler


class StateServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        print 'Headers:\n\t' + self.headers
        print '\nRequest:\n\t' + self.request
        print '\nrFile:\n\t' + self.rfile

    def do_GET(self):
        self.not_allowed('GET')

    def do_PUT(self):
        self.not_allowed('PUT')

    def not_allowed(self, message_type):
        self.send_response(406)
        print '[-] {0} Received: This server only expects POSTs'.format(message_type)

    def log_message(self, message_format, *args):
        pass
