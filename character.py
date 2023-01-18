# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:00:18 2023

@author: Alexandre
"""
import random
import math
class character :
    def __init__(self,spriteNum=0,posMap=[0,0]):
        if spriteNum not in femaleNumList :
            self.gender = "M"
        else :
            self.gender = "F"
        self.name = getRandomName(self.gender)
        self.spriteNum = spriteNum
        self.posMap = posMap
        self.playerControled = False
        self.speed = 2
        self.movingDir = [0,0]#randomMove(self.speed)#[(random.random()*6)-3,(random.random()*6)-3]#(random.random()*10)-5
        self.spriteList = []
        self.spriteSize = [0,0]
        self.healthPct = 1
        self.dead = False
    
    def setSpriteSize(self) :
        self.spriteSize = [self.spriteList[0].width(),self.spriteList[0].height()]
    def getPosScreen(self,offset=[0,0]):
        return [self.posMap[0]-offset[0]-int(self.spriteSize[0]/2),self.posMap[1]-offset[1]-int(self.spriteSize[1]/2)]
    
    def getSpriteFromMotion(self) :
        if self.movingDir == [0,0] :
            return 0
        if self.movingDir[0]>=0 and self.movingDir[0]>=abs(self.movingDir[1]) :
            return -2
        if self.movingDir[0]<=0 and abs(self.movingDir[0])>=abs(self.movingDir[1]) :
            return 2
        if self.movingDir[1]>0 and self.movingDir[1]>abs(self.movingDir[0]) :
            return 0
        if self.movingDir[1]<0 and abs(self.movingDir[1])>abs(self.movingDir[0]) :
            return 1
        return 0
    
    def returnSpriteFromMotion(self) :
        num = self.getSpriteFromMotion()
        if num==-2:
            num=3
        return self.spriteList[num]
    
    def move(self) :
        self.posMap = [self.posMap[0] + self.movingDir[0],self.posMap[1] + self.movingDir[1]]
        
    def changeDirRand(self,proba):
        if random.random()<proba :
            self.movingDir = randomMove(self.speed)
        elif random.random()<proba :
            self.movingDir = [0,0]
    
    def changeDir(self,direction) :
        self.movingDir = [direction[0]*self.speed,direction[1]*self.speed]
    
def randomMove(speed=1) :
    angle = random.random()*math.pi*2
    return [speed*math.cos(angle),speed*math.sin(angle)]

def getRandomName(gender="M") :
    if gender=="M" :
        return nameListM[int(random.random()*len(nameListM))]
    else :
        return nameListF[int(random.random()*len(nameListF))]

nameListM = [
    "Alex",
    "Michael",
    "Christopher",
    "Matthew",
    "Jennifer",
    "Joshua",
    "Amanda",
    "Daniel",
    "David",
    "James",
    "Robert",
    "John",
    "Joseph",
    "Andrew",
    "Ryan",
    "Brandon",
    "Jason",
    "Justin",
    "William",
    "Jonathan",
    "Brian",
    "Nicholas",
    "Anthony",
    "Eric",
    "Adam",
    "Kevin",
    "Steven",
    "Thomas",
    "Timothy",
    "Kyle",
    "Richard",
    "Jeffrey",
    "Jeremy"    
    ]
nameListF = [
    "Hongyi",
    "Jessica",
    "Ashley",
	"Sarah",
	"Stephanie",
	"Nicole",
	"Heather",
	"Elizabeth",
	"Megan",
    "Melissa",
	"Christina",
    "Rachel",
    "Laura",
    "Lauren",
	"Amber",
    "Brittany",
    "Danielle",
	"Kimberly",
	"Amy",
    "Crystal",
    "Michelle",
    "Tiffany"
]

femaleNumList = [14,15,18,32,33,45,58,60,62,75,79,80,87,91,97]