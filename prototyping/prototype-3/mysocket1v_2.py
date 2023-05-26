import socketio
import time
from time import sleep
retry_count = 0
max_retries = 1000
retry_interval = 30000  # Retry interval in seconds
sio = socketio.Client(logger=True)

'''This event (connect()) is a predifined function that emit 
    at the start of the communication in this case we are using it
    to get the client to identify itself upon connection
'''
@sio.event
def connect():
    print('Connected to server')
    # Set the sid for the client upon reconnection
    sio.emit('set_sid', '2') 
    
'''
This event is waiting for the server to acknoledge the client 
then send the get_command data to retreive the commands that was passed
at the command line
'''
@sio.event
def response(data):
    print('Server response:', data)
    sio.emit('get_command',data)

@sio.event
def disconnect():
    print('Disconnected from server')

''' 
This is the events that handles all the commands sent from the client
'''
@sio.event
def message_to_send(data):
    sleep(1)
    if data == "ON":
        print("LED Should Be on")
        # Turn LED on
        '''GPIO.setup(LED_PIN, GPIO.OUT)
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)'''
        print("ON form DT")
    elif data == "OFF":
        print('OFF')
               
    elif data == 'PWM':
        print("LED Should Be PWM'ing")
        # Simulate Transition
        # Gradually adjust the PWM to 0
        '''for i in range(100, 0, -1):
            PWM.start(LED_PIN, i, BB_FREQ)
            sleep(0.1)
        sleep(.5)
        PWM.cleanup(LED_PIN)'''
        
    elif data == 'OFF':
        print("LED Should Be OFF")
        '''time.sleep(0.5)
        PWM.stop(LED_PIN)
        PWM.cleanup(LED_PIN)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)'''
    
    elif data == 'GET_LIGHT_LEVEL':
        intensity = 22
        print('Sending intensity')
        sleep(1)
        sio.emit("light_intensity",f"light instensity{intensity}")
        #sio.emit('response', {'data': command, 'value': intensity})
      #  print(f"Sent '{command}' response to the server")
      
    #thinking about  having all the command for the LED_stuff here

# Connect to the server
sio.connect('http://192.168.50.114:8000')


# Join a specific room
#sio.emit('join_room', 'room1')

# Send a message to the server
sio.emit('message', 'Hello, server!')

# Wait for events
sio.wait()