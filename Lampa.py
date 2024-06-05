#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Lampa:

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # szenzorok
        #self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.us = UltrasonicSensor(Port.S4)

    def lampaFel(self):
        self.ev3.light.on(Color.YELLOW)

    def lampaLe(self):
        self.ev3.light.off()



    def lampaKapcsolasUltraSensor(self):
        alapTavolsag = self.us.distance(silent=False)
        while True:
            if self.ts.pressed():
                self.lampaFel()
                wait(2)
            elif(self.ts.pressed()):
                self.lampaLe()
                wait(2)
            else:
                if self.us.distance(silent=False) < alapTavolsag:
                    self.lampaFel()
                else:
                    #wait(500)
                    self.lampaLe()


    def lampaKapcsolasUltraSensor2(self):
        alapTavolsag = self.us.distance()
        szamlalo = 0
        while True:
            print(szamlalo, self.ts.pressed())

            if self.us.distance() < alapTavolsag:
                self.lampaFel()
                if(szamlalo%2==0) and self.ts.pressed():
                    print("gombb")
                    self.lampaFel()
                if(self.ts.pressed()):
                    szamlalo+=1
                    print("szamlalo: " + str(szamlalo))
                print("lampa Fel")
            else:
                self.lampaLe()
                print("lampa Le")
                if(szamlalo%2==0) and self.ts.pressed():
                    print("gombb")
                    self.lampaFel()
                if(self.ts.pressed()):
                    szamlalo+=1
                    print("szamlalo: " + str(szamlalo))
            wait(200)