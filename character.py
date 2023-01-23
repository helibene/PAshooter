# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:00:18 2023

@author: Alexandre
"""
import random
import math
class character :
    def __init__(self,spriteNum=0,posMap=[0,0],genderAndNameFromSprite=True,name="",gender="M"):
        self.gender = gender
        self.name = name
        if genderAndNameFromSprite :
            if spriteNum not in femaleNumList :
                self.gender = "M"
            else :
                self.gender = "F"
            self.name = getRandomName(self.gender)
        self.spriteNum = spriteNum
        self.posMap = posMap
        self.playerControled = False
        self.speed = 10
        self.movingDir = [0,0]
        self.spriteList = []
        self.spriteSize = [0,0]
        self.healthPct = 1
        self.dead = False
        self.damageMulti = random.random()*0.1
        self.attackRange = 30
        self.movingPattern = 3
        self.attackCooldown = 0
        self.defense = 1
        self.damageCooldown=0
        
    def applyDamage(self,damage,multi=1) :
        self.damageCooldown = 20
        died = False
        self.healthPct = self.healthPct - float((damage*multi)/self.defense)
        if self.healthPct<0 and not self.dead:
            self.dead = True
            self.movingPattern = 0
            died = True
        return died
    
    def setSpriteSize(self) :
        self.spriteSize = [self.spriteList[0].width(),self.spriteList[0].height()]
        
    def getPosScreen(self,offset=[0,0]):
        return [self.posMap[0]-offset[0]-int(self.spriteSize[0]/2),self.posMap[1]-offset[1]-int(self.spriteSize[1]/2)]
    
    def getSpriteFromMotion(self) :
        if self.damageCooldown>0:
            return 4
        if self.movingDir == [0,0] or self.dead:
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
        
    def changeDirRand(self,probaChangeDir,probaStopMoving):
        if random.random()<probaChangeDir :
            self.movingDir = randomMove(self.speed)
        elif random.random()<probaStopMoving :
            self.movingDir = [0,0]
    
    def folowPlayer(self,player,inverted=False,vision=-1,probaChangeDir=0.02,probaStopMoving=0.02) :
        if inverted :
            distX = self.posMap[0]-player.posMap[0]
            distY = self.posMap[1]-player.posMap[1]
        else :
            distX = player.posMap[0]-self.posMap[0]
            distY = player.posMap[1]-self.posMap[1]
        dist = math.sqrt(math.pow(distX,2)+math.pow(distY,2))
        if vision!=-1 :
            if dist<vision :
                self.changeDir([distX/dist,distY/dist])
            else :
                self.changeDirRand(probaChangeDir,probaStopMoving)
        else :
            self.changeDir([distX/dist,distY/dist])
                
    def changeDir(self,direction) :
        self.movingDir = [direction[0]*self.speed,direction[1]*self.speed]
    
    def lootItem(self) :
        item = [30,self.posMap[0],self.posMap[1],-1]    
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