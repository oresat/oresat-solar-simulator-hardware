
import socketio
import uuid
import eventlet
import time
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

BB_FREQ = 250e3
LED_PIN = "P9_14"

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server")
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    sio.emit('my_event', {'mac_address': mac_address}) #sending mac address to server
@sio.event
def disconnect():
    print("Disconnected from the server")

@sio.event
def message(data):
    command = data['command']
    if command == 'getTemp':
        response = 23
        ##The sensor code going to be here
        
    if command == 'getIntensity':
        response = 44
        #the photoresistor code gonna be here
        
    if command == 'OFF':
        print("LED Should Be OFF")
        time.sleep(0.5)
        PWM.stop(LED_PIN)
        PWM.cleanup(LED_PIN)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)
        response = 0 
    if command == 'ON':
        print("LED Should Be on")
        # Turn LED on
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        response = 0
    else:
        response = "Invalid command"
    
    # Add a small delay to ensure the client is fully connected
    eventlet.sleep(0.5)
    
    sio.emit('response', {'command': command, 'value': response})
    print(f"Sent '{command}' response to the server")


if __name__ == '__main__':
    sio.connect('http://192.168.50.114:8000')
    sio.wait()
