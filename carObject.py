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
        
    def getMapPixel(self,mapMat) :
        sizeX = int(self.spriteSize[0]/32)
        sizeY = int(self.spriteSize[1]/32)
        posX = int((self.pos[0]/32)-3.5)
        posY = int((self.pos[1]/32)-2.5)
        colSizeY = len(mapMat)-1
        colSizeX = len(mapMat[0])-1
        print("size :",[sizeX,sizeY])
        print("pos :",[posX,posY])
        print("mapMat size :",[colSizeX,colSizeY])
        boolMap = [[0 for x in range(sizeX)] for y in range(sizeY)] 
        for x in range(sizeX) :
            for y in range(sizeY) :
                if mapMat[min(max(posY+y,0),colSizeY)][min(max(posX+x,0),colSizeX)] :
                    boolMap[x][y] = 1
                else :
                    boolMap[x][y] = 0
                #boolMap[x][y] = mapMat[min(max(posY+y,0),colSizeY)][min(max(posX+x,0),colSizeX)]
        cntMat = [0,0,0,0]
        sumMat = [0,0,0,0]
        avgMat = [0,0,0,0]
        for x in range(sizeX) :
            for y in range(sizeY) :
                if x<int(sizeX/2) :
                    if y<int(sizeY/2) :
                        sumMat[0] = sumMat[0] + boolMap[x][y]
                        cntMat[0] = cntMat[0] +1
                    else :
                        sumMat[2] = sumMat[2] + boolMap[x][y]
                        cntMat[2] = cntMat[2] +1
                else :
                    if y<int(sizeY/2) :
                        sumMat[1] = sumMat[1] + boolMap[x][y]
                        cntMat[1] = cntMat[1] +1
                    else :
                        sumMat[3] = sumMat[3] + boolMap[x][y]
                        cntMat[3] = cntMat[3] +1
        for i in range(len(sumMat)) :
            avgMat[i]=sumMat[i]/cntMat[i]
                
        print(avgMat)
        print(sum(avgMat)/4)
        return sum(avgMat)/4,avgMat
    
    def canMove(self,matMap,threold=0.5) :
        validAvg,avgMat = self.getMapPixel(matMap)
        if validAvg<threold :
            defaultval = 10
            self.acc = [0,0]
            self.speed = [0,0]
            minAvg = min(avgMat) 
            if avgMat[0]==minAvg :
                self.speed = [defaultval,defaultval]
            if avgMat[1]==minAvg :
                self.speed = [-defaultval,defaultval]
            if avgMat[2]==minAvg :
                self.speed = [defaultval,-defaultval]
            if avgMat[3]==minAvg :
                self.speed = [-defaultval,-defaultval]

    def display(self) :
        print("Sprite num :",self.spriteNum)
        print("Pos :",self.pos," Speed :",self.speed," Acc :",self.acc)
        print("Size :",[self.sizeX,self.sizeY])
        print("Sprite list len :",len(self.sprite))