import socketio
import socket
from eventlet import tpool, wsgi, listen
from time import sleep
from math import pi, cos
from os import system
from cubesat import Cubesat


local_address='192.168.1.66' 
hostname = socket.gethostname()
ip_addresss = socket.gethostbyname(hostname) #get the host IP

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

def simulation():
    step = pi/100
    theta = 0
    oresat = Cubesat()
    while theta < 2 * pi:
        system('clear')
        oresat.rotate(step)
        print(f"theta: {oresat.cube['theta']:.2f}\n")
        theta += step
        for i in range(4):
            side_norm = oresat.get_normal(i)
            print(f'Side {i+1} Normal: {side_norm:.2f}')
            if side_norm < pi/2 and side_norm > -pi/2:
                print(f'Side {i+1} facing Sun, PWM: {cos(side_norm) * 100:.0f}')
            else:
                print(f'Side {i+1} not facing Sun.')  
            print('\n')
        sleep(0.1)

if __name__ == '__main__':
    wsgi.server(listen((local_address, port)), app)