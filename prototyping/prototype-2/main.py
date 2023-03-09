#import Adafruit_BBIO.PWM as PWM
from time import sleep
from math import pi, cos
from os import system
from cubesat import Cubesat

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