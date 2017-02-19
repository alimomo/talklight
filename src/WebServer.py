
'''
Start a HTTP Web Server instance
'''

import BaseHTTPServer

ADDR = ("127.0.0.1",8088)

def keep_running():
    return True

def myWebServer(server_class=BaseHTTPServer.HTTPServer,handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_addr = (ADDR)
    httpd = server_class(server_addr,handler_class)
    while keep_running():
        httpd.handle_request()

if __name__ == '__main__':
    print 'Running WebServer!'
    myWebServer()