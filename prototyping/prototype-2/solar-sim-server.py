import os
import sys
import socketio
import eventlet


local_address='192.168.1.66' 

with open('server.conf') as f:
    local_address=f.read() 

port = 8080

sio = socketio.Server(logger=False,async_mode='eventlet')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ, auth):
    
    print(f"Arg counts: {len(sys.argv)}")
    mes = sys.argv[1]
    print(f"Arg is: {mes}")
    print('connect ', sid)
    sio.emit('cmd', mes)
   
@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((local_address, port)), app)
