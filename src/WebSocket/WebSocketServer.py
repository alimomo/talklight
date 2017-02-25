import socket
import threading
from WebServer import WS_ADDR
def ws_handler(sock,addr):
    print 'ws handshaking'


def websocket_server():
    print 'listening for a WebSocket connection !'
    svSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    svSock.bind(WS_ADDR)
    svSock.listen(5)

    while 1:
        wSock,wAddr = socket.socket.accept(svSock)
        threading.Thread(None,ws_handler,"handler",(wSock,wAddr))
