import socketio
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

server_addr='192.168.1.66' 

with open('server.conf') as f:
    server_addr=f.read() 

BB_FREQ = 250e3
LED_PIN = "P9_14"
sio = socketio.Client(logger=True, engineio_logger=False)
GPIO.setup(LED_PIN, GPIO.OUT)


@sio.event
def connect():
    print('connected to server')
    
    
@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print('disconnected from server')


#this event gets the from the sever and execute or
#emit a response to the server 
@sio.event
def cmd(msg):
    print(msg)
    if msg == 'ON':
        print("LED Should Be on")
        # Simulate Transition
        # Gradually adjust the PWM to 0
        for i in range(100, 0, -1):
            PWM.start(LED_PIN, i, BB_FREQ)
            sleep(0.1)
    if msg == 'OFF':
        print("LED Should Be OFF")
        GPIO.output(LED_PIN, GPIO.LOW)
    if msg == 'GET_TEMP':
        dummyTemp = 34
        print('Sending temp...')
        print(dummyTemp)
        #sio.emit('my message', {'foo': 'bar'})
        #sio.emit('cmd',"dummyTemp")
    if msg == 'GET_LIGHT_LEVEL':
        print('Sending entenaity')

if __name__ == '__main__':
    sio.connect(f'{server_addr}:8080')
    sio.wait()
    #hello()