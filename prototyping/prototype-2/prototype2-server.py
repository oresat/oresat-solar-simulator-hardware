import os
import sys
import socket
import socketio
import eventlet
from cubesat import Cubesat
from os import system
from math import pi, cos, floor

import netifaces as ni 
#ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'] #get the current ip

local_address='168.168.1.66'
hostname = socket.gethostname()
ip_addresss = socket.gethostbyname(hostname) #get the host IP
#addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET6)
port = 8080 #port to listen on

sio = socketio.Server(logger=False,async_mode='eventlet')
app = socketio.WSGIApp(sio)

def ping_in_intervals():
    # i = 20
    step = pi/100
    theta = 0
    oresat = Cubesat()
    LEDPWM = [0, 0, 0, 0]
    while theta < 3 * pi:
        system('clear')
        oresat.rotate(step)
        print(f"theta: {oresat.cube['theta']:.2f}\n")
        theta += step
        for i in range(4):
            side_norm = oresat.get_normal(i)
            if side_norm <= pi/2 and side_norm >= -pi/2:
                LEDPWM[i] = floor(cos(side_norm) * 100)
            else:
                LEDPWM[i] = 0
            print(f'Side {i+1} Normal: {side_norm:.2f}')
            if side_norm < pi/2 and side_norm > -pi/2:
                print(f'Side {i+1} facing Sun, PWM: {cos(side_norm) * 100:.0f}')
            else:
                print(f'Side {i+1} not facing Sun.')  
            print('\n')
            # PWM.set_duty_cycle(LED['name'][i], LED['PWM'][i])
        sio.emit('pwm_comm', LEDPWM)
        sio.sleep(0.1)
        if theta > 2 * pi:
            theta = 0
    # while True:
    #     sio.sleep(0.5)
    #     sio.emit('pwm_comm', [i, i+10, i - 10, i]) 
    #     i += 1
    #     if i > 70:
    #         i = 20

@sio.event
def connect(sid, environ):
    print('Client connected:', sid)
    thread = sio.start_background_task(ping_in_intervals)
    if( len(sys.argv) > 1 and len(sys.argv) <= 2):
        mes = sys.argv[1]
        print(f"Arg is: {mes}")
        #print(addr_info)
        #print('connect ', sid)
        if mes =='GET_TEMP':
            sio.emit('get_temp', mes, room=sid)
        else:
            print('sending')
            # sio.emit('cmd', mes,room=sid)
            sio.emit('pwm_comm', [1, 2], room=sid)
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
    
    eventlet.wsgi.server(eventlet.listen((ip_addresss, port)), app) #using netifaces
