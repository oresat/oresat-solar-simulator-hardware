import getopt
import sys
import socket
import socketio
import eventlet
import time
from time import sleep

import netifaces as ni 
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'] #get the current ip
sio = socketio.Server(logger=False, async_mode= 'eventlet')
verbose = False

local_address='192.168.50.114'
hostname = socket.gethostname()
ip_addresss = socket.gethostbyname(hostname) #get the host IP
#addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET6)
port = 8000 #port to listen on


# Dictionary to store client identifiers and corresponding sids
client_sids = {} #dictionary to hold the PB_ID and their sid

command_list = [''] #list to store the command

PB_ID = [] #array to store the id of the PB
try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:vc:i:", ["help", "output=","command=", "ID="])
except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
output = None
verbose = False
for o, a in opts:
    if o == "-v":
        verbose = True
    elif o in ("-h", "--help"):
        #usage()
        sys.exit()
    elif o in ("-c", "--command"):
        command = a
        print('Arg is:',a)
        command_list[0] = a #adding the command to a list
        print("CMD",command_list)
    elif o in ("-i","--ID"):
        ID = a #for PB number
        PB_ID = a
        print("PB ID: ",PB_ID[0])
    elif o in ("-o", "--output"):
        output = a
    else:
        assert False, "unhandled option"



@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)
    command_list = '' #clean up
    if sid in client_sids:
        del client_sids[sid]

@sio.event
def join_room(sid, room):
    print('Client', sid, 'joining room:', room)
    sio.enter_room(sid, room)

@sio.event
def leave_room(sid, room):
    print('Client', sid, 'leaving room:', room)
    sio.leave_room(sid, room)

@sio.event
def message(sid, data):
    print('Received message from client:', data)
    if 'room' in data:
        room = data['room']
        message_text = data['message']
        sio.emit('response', message_text, room=room)
        sio.emit('message', {'room': 'room1', 'message': 'Hello, room1!'})
        sio.emit('message', {'room': 'room4', 'message': 'Hello, room4!'})

@sio.event
def get_command(sid,data):
    print("sending messsage")
    #print(f" from get_command  {client_sids[PB_ID]}")
    sio.emit('message_to_send',command_list[0],room=client_sids[PB_ID])
    print(f"get_command{command_list[0]},ID: {PB_ID}", )
    
@sio.event
def set_sid(sid, client_id):
    print('Setting sid for client:', client_id)
    client_sids[client_id] = sid
    print(client_sids)
    sio.emit('response',f'User {client_id} was added succesfully!!', room=sid)
    
@sio.event
def light_intensity(sid,data):
    print(f"Lightintensity:{data}")

if __name__ == '__main__':
   # eventlet.wsgi.server(eventlet.listen((addr_info, port)), app) #using old method
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen((ip, port)), app) #using netifaces
    
