    # -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:34:41 2023

@author: Alexandre
"""

import math
class carObject :
    def __init__(self,spriteNum,pos=[0,0],speed=[0,0],acc=[0,0],frictionPct=0.05,maxSpeed=50):
        self.index = 0
        self.spriteNum = spriteNum
        self.pos = pos
        self.speed = speed
        self.acc = acc
        self.sizeX = 0
        self.sizeY = 0
        self.spriteSize = [0,0]
        self.angle = 0
        self.frictionPct = frictionPct
        self.sprite = []
        self.maxSpeed = maxSpeed
        self.accMulti = 0.5
        self.vehiculeType = "car"
        if spriteNum > 7 and spriteNum <12:
            self.vehiculeType = "boat"
        elif spriteNum > 11:
            self.vehiculeType = "heli"
        

    def move(self) :
        self.pos = [self.pos[0]+self.speed[0],self.pos[1]+self.speed[1]]
    
    def applyAcceleration(self) :
        roof = self.maxSpeed
        frict = self.getFrictionVector()
        self.acc = [self.acc[0]+frict[0],self.acc[1]+frict[1]]
        self.speed = [self.speed[0]+self.acc[0],self.speed[1]+self.acc[1]]
        self.speed = [max(min(self.speed[0],roof),-roof),max(min(self.speed[1],roof),-roof)]
    
    def getFrictionVector(self) :
        return [-self.speed[0]*self.frictionPct,-self.speed[1]*self.frictionPct]
    
    def updateAngle(self,maxAngle=30):
        if self.vehiculeType=="car" :
            radAngle = self.getSpeedAngle()
            if radAngle == None :
                return 0
            else :
                unitAngle = radAngle/(math.pi*2)
                spriteAngle = int(math.ceil(unitAngle*maxAngle))
                if spriteAngle == maxAngle :
                    spriteAngle = 0
                return spriteAngle
        else :
            if self.speed[0]>=0 :
                return 0
            else :
                return 1
    def getSpeedAngle(self):
        speedAbs = (math.sqrt(math.pow(self.speed[0],2)+math.pow(self.speed[1],2)))
        if speedAbs != 0: 
            if self.speed[1]==0:
                sign = 1
            else :
                sign = (-self.speed[1]/abs(self.speed[1]))
            ang = math.acos(self.speed[0]/speedAbs)*(sign)+math.pi-math.pi/2
            if ang<0 :
                ang = ang + 2*math.pi
            return ang
        else :
            return None
    
    def setAcceleration(self,acc):
        self.acc = [acc[0],acc[1]]

    def display(self) :
        print("Sprite num :",self.spriteNum)
        print("Pos :",self.pos," Speed :",self.speed," Acc :",self.acc)
        print("Size :",[self.sizeX,self.sizeY])
        print("Sprite list len :",len(self.sprite))