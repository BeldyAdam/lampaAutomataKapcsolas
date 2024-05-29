#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Lampa():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.us = UltrasonicSensor(Port.S4)


    def lampaFel():
        return True

    def lampaLe():
        return False

    def lampaKapcsolasGombbal(self):
        if(self.ts.pressed()):
            lampaFel()
            else:


    def lampaKapcsolasUltraSensor(self):
        alapTavolsag = self.us.distance(silent = False)
        mozgasTavolsag = 0
        while(alapTavolsag > mozgasTavolsag):
            lampaFel()



