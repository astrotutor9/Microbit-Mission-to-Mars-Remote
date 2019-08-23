# Microbit code for Rover
"""
Microbit    Arduino
1           9
2           10
8           11
13          7
14          8
16          12
0           GND
"""

from microbit import *
import radio

# define named variables for the motor pin connections
enable_left_motor = pin1
enable_right_motor = pin2

forwards_right = pin16
backwards_right = pin8

forwards_left = pin14
backwards_left = pin13

# turn on the radio using default channel 7
radio.config(channel=7)
radio.on()

# define the functions to move the rover
def forwards():
    enable_left_motor.write_digital(1)      # on
    enable_right_motor.write_digital(1)     # on
    forwards_right.write_digital(1)     # on
    backwards_right.write_digital(0)    # off
    forwards_left.write_digital(1)      # on
    backwards_left.write_digital(0)     # off
    
def backwards():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(0)  
    backwards_right.write_digital(1)
    forwards_left.write_digital(0)
    backwards_left.write_digital(1) 
    
def stop():
    enable_left_motor.write_digital(0)
    enable_right_motor.write_digital(0)
    forwards_right.write_digital(0)
    backwards_right.write_digital(0)
    forwards_left.write_digital(0)
    backwards_left.write_digital(0)
    
def left():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(1)
    backwards_right.write_digital(0)
    forwards_left.write_digital(0)
    backwards_left.write_digital(1)
    
def right():
    enable_left_motor.write_digital(1)
    enable_right_motor.write_digital(1)
    forwards_right.write_digital(0)
    backwards_right.write_digital(1)
    forwards_left.write_digital(1)
    backwards_left.write_digital(0)
    
while True:
    message = radio.receive()
    if message == "F":
        forwards()
        display.show(Image.ARROW_S)
    elif message == "B":
        backwards()
        display.show(Image.ARROW_N)
    elif message == "L":
        left()
        display.show(Image.ARROW_E)
    elif message == "R":
        right()
        display.show(Image.ARROW_W)
    else:
        stop()
        display.show(Image.HAPPY)
    sleep(10)