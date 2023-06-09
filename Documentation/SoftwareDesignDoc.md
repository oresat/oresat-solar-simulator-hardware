# Solar Simulator Software Design Documentation
## High Level Flow
### Control Server
This will be a main control server that will run simulation software (such as 42) and use it to drive the individual solar simulators in concert.
### Solar Simulator
These will be BeagleBone Blacks that will run a python application that will drive the lighting elements and receive input from the sensors. The state of the sensors will be fedback to the control server for processing.
## Prototyping
### Prototype 1
Simple PWM output that was used to test the setup of the BBB utilizing the adafruit library.
### Prototype 2
This will be used to test the control server and client structure and communication between the two parts. The goal of this prototyp will be to use socketIO communication from the server to control the PWM pins on the BBB.
### Prototype 3
???
### Prototype 4
Profit