import Adafruit_BBIO.PWM as PWM # Used for demo validation
from time import sleep
from Adafruit_I2C import Adafruit_I2C
import adafruit_mcp4728
from debugdata import fake_photo, fake_temp

import socketio

global client_connected
client_connected = False
sio = socketio.Client(logger=True)

# TODO: Read from file
server_address = '192.168.6.1'
server_port = '8000'
client_id = 2


### PWM Demo Remove for Final Code
BB_FREQ = 250e3
LED_PIN = "P9_16"
PWM.start(LED_PIN, 0, BB_FREQ)
###

'''
    This event (connect()) is a predifined function that emit 
    at the start of the communication in this case we are using it
    to get the client to identify itself upon connection
'''
@sio.event
def connect():
    global client_connected
    print('Connected to server')
    # Set the sid for the client upon reconnection
    sio.emit('set_sid', client_id)
    client_connected = True
    
'''
This event is waiting for the server to acknoledge the client 
then send the get_command data to retreive the commands that was passed
at the command line
'''
@sio.event
def disconnect():
    global client_connected
    print('Disconnected from server')
    client_connected = False


# main loop event that the client will receive
@sio.event
def pwm_comm(msg):
    LEDPWM = msg
    print(f'my LED is at {LEDPWM}')
    PWM.set_duty_cycle(LED_PIN, LEDPWM) # Remove for final
    sio.emit('sim_response', [client_id, fake_temp[client_id], fake_photo[client_id]])

def notificationLED():
    '''
    Not working, for now the call is removed
    '''
    global client_connected
    while True:
        if client_connected:
            print('We are connected :)')
        else:
            print('We are not connected :(')
        sio.sleep(5)

# Connect to the server
sio.connect(f'http://{server_address}:{server_port}')

# thread = sio.start_background_task(notificationLED)

# Wait for events
sio.wait()
