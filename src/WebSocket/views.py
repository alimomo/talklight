
from django.shortcuts import render_to_response, render
import datetime
import WebSocketServer
import threading

#

def current_base(request):
    now = datetime.datetime.now()
    threading.Thread(target=WebSocketServer.websocket_server).start()
    return render_to_response('WebSocket/base.html',locals())


# 2nd view) render the home page content which explains 'how the project words' & renders a few images
def index(request):
    now = datetime.datetime.now()
    return render(request, 'WebSocket/index.html', {'time':now})
