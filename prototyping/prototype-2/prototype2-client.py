import socketio
import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep


BB_FREQ = 250e3
LED_PIN = "P9_14"
IP = '192.168.50.114'
PORT = '8000'
address = 'ws://' + IP + ':' + PORT
#get mac address

sio = socketio.Client(logger=False, engineio_logger=False)
GPIO.setup(LED_PIN, GPIO.OUT)
print(address)

@sio.event
def connect():
    print("connected")
    #print(f"connected to server {sio.sid}")
    print('my sid is', sio.sid)
@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print('disconnected from server')

# Define an event for receiving a message from the server
@sio.event
def response(data):
    print('Received response:', data)
@sio.on('message')
def send_it(data):
    print("im here")
    sio.emit('message', 'Hello, server!')
 #event to gete the temperature   
@sio.on('GET_TEMP')
def get_temp(data):
        print('message',data)
        dummyTemp = 34
        print('Sending temp...')
        print(dummyTemp)
        message = 'Hello, server!'
        sio.emit('my_message', message)

@sio.event
def cmd(msg):
    print(msg)
    if msg == 'ON':
        print("LED Should Be on")
        # Turn LED on
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
    if msg == 'PWM':
        print("LED Should Be PWM'ing")
        # Simulate Transition
        # Gradually adjust the PWM to 0
        for i in range(100, 0, -1):
            PWM.start(LED_PIN, i, BB_FREQ)
            sleep(0.1)
        sleep(.5)
        PWM.cleanup(LED_PIN)
    if msg == 'OFF':
        print("LED Should Be OFF")
        time.sleep(0.5)
        PWM.stop(LED_PIN)
        PWM.cleanup(LED_PIN)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)
    
    if msg == 'GET_LIGHT_LEVEL':
        print('Sending intensity')
    

if __name__ == '__main__':
    sio.connect('http://192.168.50.114:8000')

    #sio.connect('ws://192.168.50.114:8000', transports=['websocket'])
    #sio.connect(str(address))
    sio.wait()
 
