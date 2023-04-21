import os
import sys
import socket
import socketio
import eventlet

import netifaces as ni 
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'] #get the current ip

local_address='192.168.50.114'
hostname = socket.gethostname()
ip_addresss = socket.gethostbyname(hostname) #get the host IP
#addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET6)
port = 8000 #port to listen on

sio = socketio.Server(logger=False,async_mode='eventlet')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Client connected:', sid)
    
    if( len(sys.argv) > 1 and len(sys.argv) <= 2):
        mes = sys.argv[1]
        print(f"Arg is: {mes}")
        #print(addr_info)
        #print('connect ', sid)
        if mes =='GET_TEMP':
            sio.emit('get_temp', mes, room=sid)
        else:
            sio.emit('cmd', mes, room=sid)
    else:
        print("Type a cmd to send to client")
        print("example \"server.py ON\" ")
    
# Define an event for receiving a message from a client
@sio.on('message')
def handle_message(sid, data):
    print('Received message from', sid, ':', data)
    sio.emit('response', 'Received message: ' + data, room=sid)   

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
   # eventlet.wsgi.server(eventlet.listen((addr_info, port)), app) #using old method
    eventlet.wsgi.server(eventlet.listen((ip, port)), app) #using netifaces
