import socket
import threading

#WebSocket Server Address
WS_ADDR = ("127.0.0.1",9876)


def ws_handler(sock,addr):
    print 'ws handshaking...'
    print 'connected...'
    print 'closing...'


def websocket_server():
    print 'listening for a WS connection... '
    svSock = socket.socket()
    svSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    svSock.bind(WS_ADDR)
    svSock.listen(5)
    while (1):
        wSock,wAddr = svSock.accept()
        print 'accepted!'
        threading.Thread(target=ws_handler,args=(wSock,wAddr)).start()


#   a new listen thread
def listen_ws():
    threading.Thread(target=websocket_server()).start()