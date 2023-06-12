import socketio
import uuid
import eventlet
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

# Read server IP from file
server_addr = '127.0.1.1'
with open('server.conf') as f:
    server_addr = f.read()

# Variable Declaration
BB_FREQ = 250e3
LED_PIN = "P9_14"
LEDE = "P9_14"
LEDS = "P9_16"
LEDN = "P9_21"
LEDW = "P9_22"
LED = [LEDN, LEDE, LEDS, LEDW]
port = '8080'

# Initialization
sio = socketio.Client()
PWM.start(LEDE, 0, BB_FREQ)
PWM.start(LEDW, 0, BB_FREQ)
PWM.start(LEDN, 0, BB_FREQ)
PWM.start(LEDS, 0, BB_FREQ)


@sio.event
def connect():
    print("Connected to the server")
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    sio.emit('my_event', {'mac_address': mac_address}) # sending mac address to server


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
        sleep(0.5)
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
        sleep(0.5)
        response = 0
    else:
        response = "Invalid command"
    
    # Add a small delay to ensure the client is fully connected
    eventlet.sleep(0.5)
    
    sio.emit('response', {'command': command, 'value': response})
    print(f"Sent '{command}' response to the server")


@sio.event
def pwm_comm(msg):
    # Receives a PWM command from the server
    # msg is a 4 integer list to specify PWM values for LEDs
    print(msg)
    # PWM.set_duty_cycle(LED['name'][i], LED['PWM'][i])
    for i in range(4):
        print(f"{LED[i]}:{msg[i]}")
        PWM.set_duty_cycle(LED[i], msg[i])


if __name__ == '__main__':
    sio.connect(f'http://{server_addr}:{port}')
    sio.wait()
