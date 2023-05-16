    # -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:00:18 2023

@author: Alexandre
"""
import random
import math
class character :
    def __init__(self,spriteNum=0,posMap=[0,0],genderAndNameFromSprite=True,name="",gender="M",template=None):
        self.gender = gender
        self.name = name
        self.template = template
        if genderAndNameFromSprite and template!=None:
            if spriteNum not in femaleNumList :
                self.gender = "M"
            else :
                self.gender = "F"
            self.name = self.getRandomName(self.gender)
        self.spriteNum = spriteNum
        self.posMap = posMap
        self.playerControled = False
        
        self.movingDir = [0,0]
        self.spriteList = []
        self.spriteSize = [0,0]
        self.dead = False
        self.attackCooldown = 0
        self.damageCooldown=0
        self.damageCooldownDef=40
        self.inCar = -1
        self.carInteractionCooldown = 0
        self.merchand = False
        self.lootList = []
        self.lootDistPct = 0.9
        self.talkingText = ""#"我爱老婆   "
        self.emojiProba = 0.2
        self.totalDeltaPos = [0,0]
        self.speed = 15
        self.healthPct = 1
        self.damageMulti = random.random()*0.1
        self.attackRange = 30
        self.movingPattern = 6
        self.defense = 1
        self.aggro = True
        self.lootNumRange = [0,0]
        self.talkProbability = 0.001
        self.probaChangeDir = 0.01
        self.probaStopMoving = 0.01
        self.vision = 150
        self.folowFarRange = [100,300]
        self.setupDefaultTemplate()
    
    def setupDefaultTemplate(self) :
        self.speed = self.template.characterDef["speed"]
        self.healthPct = self.template.characterDef["healthPct"]
        self.damageMulti = self.template.characterDef["damageMulti"]
        self.attackRange = self.template.characterDef["attackRange"]
        self.movingPattern = self.template.characterDef["movingPattern"]
        self.defense = self.template.characterDef["defense"]
        self.aggro = bool(self.template.characterDef["aggro"])
        self.lootNumRange = list(self.template.characterDef["lootNumRange"])
        self.talkProbability = self.template.characterDef["talkProbability"]
        self.probaChangeDir = self.template.characterDef["probaChangeDir"]
        self.probaStopMoving = self.template.characterDef["probaStopMoving"]
        self.vision = self.template.characterDef["vision"]
        self.folowFarRange = list(self.template.characterDef["folowFarRange"])
        
    def applyDamage(self,damage,multi=1) :
        self.damageCooldown = self.damageCooldownDef
        died = False
        self.healthPct = self.healthPct - float((damage*multi)/self.defense)
        if self.healthPct<0 and not self.dead:
            self.dead = True
            self.movingPattern = 0
            died = True
        return died
    
    def dropItems(self) :
        for loot in self.lootList :
            randomMv = randomMove(self.spriteSize[0]*self.lootDistPct)
            loot.pos = [self.posMap[0]+randomMv[0],self.posMap[1]+randomMv[1]]
            loot.doNotDisplayOnMap = False
            loot.canPickup = True
        
    def setSpriteSize(self) :
        self.spriteSize = [self.spriteList[0].width(),self.spriteList[0].height()]
        
    def getPosScreen(self,offset=[0,0]):
        return [self.posMap[0]-offset[0]-int(self.spriteSize[0]/2),self.posMap[1]-offset[1]-int(self.spriteSize[1]/2)]
    
    def getPosMapCenter(self) :
        return [self.posMap[0]-int(self.spriteSize[0]/2),self.posMap[1]-int(self.spriteSize[1]/2)]
    
    
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
        self.totalDeltaPos = [self.totalDeltaPos[0]+ (self.movingDir[0]/self.speed),self.totalDeltaPos[1]+ (self.movingDir[1]/self.speed)]
        #print(self.totalDeltaPos)
        
    def changeDirRand(self,probaChangeDir,probaStopMoving):
        if random.random()<probaChangeDir :
            self.movingDir = randomMove(self.speed)
        elif random.random()<probaStopMoving :
            self.movingDir = [0,0]
    
    def folowPlayer(self,player,inverted=False,vision=False) :
        distX,distY = self.getXYdist(player,inverted)
        dist = math.sqrt(math.pow(distX,2)+math.pow(distY,2))
        if vision :
            if dist<self.vision :
                self.changeDir([distX/dist,distY/dist])
            else :
                self.changeDirRand(self.probaChangeDir,self.probaStopMoving)
        else :
            self.changeDir([distX/dist,distY/dist])
          
    def folowPlayerSoft(self,player) :
        distX,distY = self.getXYdist(player)
        dist = math.sqrt(math.pow(distX,2)+math.pow(distY,2))
        if self.folowFarRange!=[-1,-1] :
            if dist<self.folowFarRange[0] :
                self.folowPlayer(player,True,False)
            elif dist<self.folowFarRange[1] :
                self.changeDirRand(self.probaChangeDir,self.probaStopMoving)
            else :
                self.folowPlayer(player,False,False)
        else :
            self.changeDirRand(self.probaChangeDir,self.probaStopMoving)
            
            
    def changeDir(self,direction) :
        self.movingDir = [direction[0]*self.speed,direction[1]*self.speed]
    
    def getXYdist(self,player,inverted=False) :
        if inverted :
            distX = self.posMap[0]-player.posMap[0]
            distY = self.posMap[1]-player.posMap[1]
        else :
            distX = player.posMap[0]-self.posMap[0]
            distY = player.posMap[1]-self.posMap[1]
        return distX,distY
    
    def getRandomName(self,gender="M") :
        if gender=="M" :
            return self.template.nameListM[int(random.random()*len(self.template.nameListM))]
        else :
            return self.template.nameListF[int(random.random()*len(self.template.nameListF))]
    
    def changeSpeak(self) :
        speakChanged = False
        if random.random()<self.talkProbability :
            speakChanged = True
            if self.talkingText == "" :
                if random.random()>self.emojiProba :
                    self.talkingText = str(self.template.sentenceList[int(random.random()*len(self.template.sentenceList))])
                else :
                    num = str(int(random.random()*9)+1)
                    if len(num)==1 :
                        num = "0"+num
                    self.talkingText = num
            else :
                self.talkingText = ""
                
        return speakChanged
def randomMove(speed=1) :
    angle = random.random()*math.pi*2
    return [speed*math.cos(angle),speed*math.sin(angle)]


femaleNumList = [14,15,18,32,33,45,58,60,62,75,79,80,81,82,83,87,91,97]