from BaseHTTPServer import BaseHTTPRequestHandler


class StateServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        print 'Headers:\n\t' + self.headers
        print '\nRequest:\n\t' + self.request
        print '\nrFile:\n\t' + self.rfile

