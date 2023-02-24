import Adafruit_BBIO.PWM as PWM
from time import sleep

BB_FREQ = 250e3
# PWM.start(channel, duty, freq=2000, polarity=0)

# Initialize LED to full brightness
PWM.start("P9_14", 100, BB_FREQ)

# Simulate Transition Loop
while True:
# Gradually adjust the PWM to 0
    for i in range(100, 0, -1):
        PWM.set_duty_cycle("P9_14", i)
        sleep(0.1)

# Gradually adjust the PWM to 100
    for i in range(0, 100):
        PWM.set_duty_cycle("P9_14", i)
        sleep(0.1)

# Simulate User Set value
#PWM.set_duty_cycle("P9_14", 42)