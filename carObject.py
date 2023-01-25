# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:34:41 2023

@author: Alexandre
"""
class carObject :
    def __init__(self,spriteNum,pos=[0,0],speed=[0,0],acc=[0,0]):
        self.index = 0
        self.spriteNum = spriteNum
        self.pos = pos
        self.speed = speed
        self.acc = acc
        self.sizeX = 0
        self.sizeY = 0
        self.angle = 0
        self.frictionPct = 0.01
        self.sprite = []

    def move(self) :
        self.pos = [self.pos[0]+self.speed[0],self.pos[1]+self.speed[1]]
    
    def applyAcceleration(self) :
        roof = 15
        self.speed = [self.speed[0]+self.acc[0],self.speed[1]+self.acc[1]]
        self.speed = [max(min(self.speed[0],roof),-roof),max(min(self.speed[1],roof),-roof)]
        self.acc = [self.acc[0]-(self.acc[0]*self.frictionPct),self.acc[1]-(self.acc[1]*self.frictionPct)]
    
    def getFrictionVector(self) :
        return [-self.speed[0]*self.frictionPct,-self.speed[1]*self.frictionPct]
    
    def setAcceleration(self,acc):
        frict = self.getFrictionVector()
        self.acc = [acc[0]+frict[0],acc[1]+frict[1]]
    def display(self) :
        print("Sprite num :",self.spriteNum)
        print("Pos :",self.pos," Speed :",self.speed," Acc :",self.acc)
        print("Size :",[self.sizeX,self.sizeY])
        print("Sprite list len :",len(self.sprite))