#!/usr/bin/env python
"""
===============================================================
customNXTMovement.py - LEGO Mindstorms NXT Custom Movement Spec
===============================================================

Definitions of movement for current configuration of NXT
"""

from time import sleep

from nxt.brick import Brick
from nxt.motor import Motor, PORT_A, PORT_B, PORT_C

FORTH = 100
BACK = -100

class customNXTMovement:
    def __init__(self):
        """
        Custom configuration file for any given LEGO Mindstorms NXT robot
        
        In here, there should be definitions for:
        turning left: turnLeft()
        turning right: turnRight()
        going forward: goStraight()
        
        There are three motor ports on the NXT: PORT_A, PORT_B, PORT_C
        These are labeled on the NXT
        
        Direction of forward, left, and right movement should be determined 
        and placed here for the locomotion handler
        
        The default is assumed to be a differential drive and is shown below
        """
        
        #Motor A is the left, Motor B is the right
        self.wheels = [Motor(brick, PORT_A), Motor(brick, PORT_B)]
        left = self.wheels[0]
        right = self.wheels[1]
        
    def turnLeft():
        left.run(BACK)
        right.run(FORTH)
    
    def turnRight():
        left.run(FORTH)
        right.run(BACK)
        
    def goStraight():
        for motor in self.wheels:
            motor.run(FORTH)
        
            