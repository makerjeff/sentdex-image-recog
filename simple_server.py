#!usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

class testHTTPRequestServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_headers()

        message = 'Hello world!'

        self.wfile.write('<h1>' + message + '</h1>')
        return

def run():
    print 'Starting server now...'
    server_address = ('127.0.0.1', 3000)
    httpd = HTTPServer(server_address, testHTTPRequestServer_RequestHandler)
    print 'running server...'
    httpd.serve_forever()


if __name__ == '__main__':
    run()