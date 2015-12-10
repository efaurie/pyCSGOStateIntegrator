import BaseHTTPServer
from StateServerHandler import StateServerHandler


class StateServer:
    def __init__(self, bind_address, port):
        self.server = self.setup_server(bind_address, port)

    @staticmethod
    def setup_server(bind_address, port):
        server_class = BaseHTTPServer.HTTPServer
        address = (bind_address, port)
        return server_class(address, StateServerHandler)

    def start_server(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.shutdown()
