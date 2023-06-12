import socketio
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

server_addr = '10.200.231.245'

# with open('server.conf') as f:
#     server_addr=f.read() 

BB_FREQ = 1e6
LED_PIN = "P9_14"
LEDE = "P9_14"
LEDS = "P9_16"
LEDN = "P9_21"
LEDW = "P9_22"
LED = [LEDN, LEDE, LEDS, LEDW]
LEDPWM = [0, 0, 0, 0]
# for i in range(4):
#     print(f'{type(LED[i])} : {LEDPWM[i]}')
#     PWM.start(LED[i], LEDPWM[i], BB_FREQ)
PWM.start(LEDE, 0, BB_FREQ)
PWM.start(LEDW, 0, BB_FREQ)
PWM.start(LEDN, 0, BB_FREQ)
PWM.start(LEDS, 0, BB_FREQ)
sio = socketio.Client(logger=True, engineio_logger=False)
# GPIO.setup(LED_PIN, GPIO.OUT)


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
        # Turn LED on
        # GPIO.setup(LED_PIN, GPIO.OUT)
        # GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(0.5)
    if msg == 'PWM':
        print("LED Should Be PWM'ing")
        # Simulate Transition
        # Gradually adjust the PWM to 0
        # for i in range(100, 0, -1):
        #     PWM.start(LED_PIN, i, BB_FREQ)
        #     sleep(0.1)
        # sleep(.5)
        # PWM.cleanup(LED_PIN)
        # print(data)
    if msg == 'OFF':
        print("LED Should Be OFF")
        sleep(0.5)
        PWM.stop(LED_PIN)
        PWM.cleanup(LED_PIN)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)
    if msg == 'GET_TEMP':
        dummyTemp = 34
        print('Sending temp...')
        print(dummyTemp)
        sio.emit('my message', {'foo': 'bar'}, namespaces='/chat')
        #sio.emit(data =str, dummyTemp)
        #sio.emit('cmd',"dummyTemp")
    if msg == 'GET_LIGHT_LEVEL':
        print('Sending entenaity')
    else:
        sio.wait()
    
@sio.event
def pwm_comm(msg):
    print(msg)
    LEDPWM = msg
    # PWM.set_duty_cycle(LED['name'][i], LED['PWM'][i])
    for i in range(4):
        print(f"{LED[i]}:{LEDPWM[i]}")
        PWM.set_duty_cycle(LED[i], LEDPWM[i])

if __name__ == '__main__':
    sio.connect(f'http://{server_addr}:8080')
    sio.wait()
    #hello()