# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 14:30:25 2023

@author: Alexandre
"""
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image,ImageOps
import PIL
import random
import math
import time
import sys
import numpy as np
import character as ch
import terrain_builder as tb
from pynput import keyboard,mouse
import object_builder as ob
import configLoader as cf
import ListenerBundle as lb
import usefullHandObject as uho
import rangeWeapon as rw
import meleWeapon as mw
import medicine as med
import objectTemplate as ot
class window :
    def __init__(self,conf=None):

        self.conf = conf
        self.useConf = False
        if conf!=None :
            self.useConf = True
        self.handObjUsefullList = self.getAllUsefullList()
        #self.useConf = False
        #Constants
        self.exitFlag = False
        self.backgroundColor = "white"
        self.resampleType = 1
        self.pressedKeys = []
        self.inventoryCount = 0
        fpsList = []
        self.keyMovePlayer = True
        self.pctScreenScroll = 0.3  
        displayCharaTest = False
        displayFPS = True
        self.zoom = 1
        self.offset = [1000,1000]
        self.displayName = True
        self.menuSize = [655,55]
        self.menuImageList = []
        self.inventoryList = []
        self.dropCooldown = 0
        self.mouseVal = [-1,-1,0]
        self.menuBarSel = 0
        self.activeBullet = 0
        self.weponUsedCooldown = 0
        self.backgroundId = -1
        self.objIdList = []
        self.animationListPos = []
        self.animationList = []
        self.totalCharacterSprite = 101
        self.changeDirectionFrequency = 0.03
        self.stopMovingFrequency = 0.03
        self.shootWeaponsObj = [8,40,41,69,70,79,51]
        self.meleWeponsObj = [5,7,19,16,22,27,35,33,43,44,45,46,48,63,50,54,66,68,76,74]
        self.medicineObj = [2,3,25,26,39,59]
        self.rwList = rw.getAllList()
        self.mwList = mw.getAllList()
        self.medList = med.getAllList()
        self.characterVision = 500
        
        self.rootPath = self.pasteConf(self.conf.spritePath,"C:/Users/Alexandre/Desktop/PAshooter/sprites/")
        self.textureFolder = self.pasteConf(self.conf.textureFolder,"texture/")
        self.zoomHandObj = self.pasteConf(self.conf.itemSize,0.7)
        self.generate_new_map = self.pasteConf(self.conf.generateNewMap,False)
        self.maxInventory = self.pasteConf(self.conf.maxInventorySize,12)
        self.distancePickup = self.pasteConf(self.conf.distancePickupPixel,30)
        self.healthPct = self.pasteConf(self.conf.startHealth,1)
        self.bulletNum = self.pasteConf(self.conf.maxBulletOnScreen,10)
        self.sprintFactor = self.pasteConf(self.conf.sprintMultiplier,2)
        self.weponUsedCooldownReset = self.pasteConf(self.conf.weponFrameCooldown,10)
        width = self.pasteConf(self.conf.screenWidth,1366)
        height = self.pasteConf(self.conf.screenHeight,768)
        fullscreen = self.pasteConf(self.conf.fullscreen,True) 
        windowOnTop = self.pasteConf(self.conf.windowOnTop,False) 
        waitBetweenFrames = self.pasteConf(self.conf.sleepPerFrame,0) 
        peopleSpawnNum = self.pasteConf(self.conf.peopleSpawnNum,30)
        peopleSpawnRangeX = self.pasteConf(self.conf.peopleSpawnRangeX,[1500,1700])
        peopleSpawnRangeY = self.pasteConf(self.conf.peopleSpawnRangeY,[1500,1700])
        peopleSpeedRange = self.pasteConf(self.conf.peopleSpeedRange,[5,5])
        peopleAttackRange = self.pasteConf(self.conf.peopleAttackRange,[30,30])
        peopleDamageMultiRange = self.pasteConf(self.conf.peopleDamageMultiRange,[1,1])
        objInitInstance = self.pasteConf(self.conf.objInitInstance,0)
        print(objInitInstance)
        myName = self.pasteConf(self.conf.myName,"")
        mySprite = self.pasteConf(self.conf.mySprite,0)
        myGender = self.pasteConf(self.conf.myGender,"M")
        myRandomName = self.pasteConf(self.conf.myRandomName,"True")
        mySpeed = self.pasteConf(self.conf.mySpeed,1)
        myPosition = self.pasteConf(self.conf.myPosition,[0,0])
        myHealth = self.pasteConf(self.conf.myHealth,1)
        myDamageMulti = self.pasteConf(self.conf.myDamageMulti,1)
        myAttackRange = self.pasteConf(self.conf.myAttackRange,30)

        #Sprites conf
        
        self.sheetList = [["objects2.png",800,1024,25,32],["terrain2.png",1024,992,32,31],["caracteres2.png",1200,1200,32,32],["black.png",1,1,1,1]]
        #self.mapList = [["template11.png","mapTemplate1",100,100]]
        #self.mapList = [["template12.png","mapTemplate2",31,31]]
        self.mapList = [["templateMaster.png","mapTemplate3",300,300]]
        #self.mapList = [["StructureTemplate.png","mapTemplate4",75,75]]
        #self.backList = [["mapTemplate1.jpeg",3200,3200,100,100,"mapTemplate1Collision.png"]]
        #self.backList = [["mapTemplate2.jpeg",992,992,31,31,"mapTemplate2Collision.png"]]
        self.backList = [["mapTemplate3.jpeg",9600,9600,300,300,"mapTemplate3Collision.png"]]
        #self.backList = [["mapTemplate4.jpeg",2400,2400,75,75,"mapTemplate4Collision.png"]]
        self.menuList = [["menu.png",[0,0,655,55],[0,55,655,110],[0,110,65,175],[0,175,505,190],[0,190,505,200]]]
        self.root,self.width,self.height = self.setRoot(width,height,0,0,windowOnTop,fullscreen,True,True)       
        self.canvas = self.getCanvasFullScreen(self.root,self.width,self.height,self.backgroundColor)

        self.carList = []
        self.openImageFiles()
        self.chara_list = self.getRandChList(peopleSpawnNum,[peopleSpawnRangeX,peopleSpawnRangeY],self.backList[0][5],peopleSpeedRange,peopleAttackRange,peopleDamageMultiRange)
        self.createMeFull(myName,mySprite,myGender,myRandomName,mySpeed,myPosition,myHealth,myAttackRange,myDamageMulti)
        self.objInit(objInitInstance)
        self.loadSpritesFromSheets()




        self.listener = lb.ListenerBundle()
        self.printRessources()
        self.drawObjList(self.objList,self.sheetList[0],self.offset,True)
        self.drawCarObjList(self.carList,self.offset,True)
        self.object.deleteSpriteMatrix()
        self.objectCar.deleteSpriteMatrix()
        self.printRessources()
        self.frameCount = 0
        while True :
            self.frameCount = self.frameCount + 1
            start = time.time()
            self.drawBundle()
            self.canvas.pack()
            self.root.update()
            time.sleep(waitBetweenFrames)
            self.moveCharacterList(self.chara_list,self.backList[0][5])
            self.scrollCursor()
            self.keyMouseAction()
            end = time.time()
            #self.printRessources()
            fpsList.append(1/max((end-start),0.0001))
            if self.listener.exitFlag :
                print("AVG FPS : "+str(round(sum(fpsList)/len(fpsList),3)))
                self.listener.killListener()
                self.root.destroy()
                sys.exit(0)
                pass
            if displayFPS :
                printFPS(start,end)
            self.resetMemAndCanvas()
        self.root.mainloop() 

    def openImageFiles(self) :
        self.openSheetList()
        self.openMapList()
        self.generateNewMap(self.generate_new_map)           
        self.object = ob.object_builder(self.sheetList[0])
        self.objectCar = ob.object_builder(self.sheetList[2])
        self.openBackgroundList()
        
    def loadSpritesFromSheets(self):
        self.loadImageCharacterList(self.sheetList[2])
        self.loadImageHandObjList(self.sheetList[2])
        self.loadImageMenuList(self.menuList)
        self.loadImageAnimationList(self.sheetList[2])
        
    def drawBundle(self) :
        self.drawBackgroundSheet(self.backList[0],-self.offset[0],-self.offset[1])
        self.drawObjList(self.objList,self.sheetList[0],self.offset)  
        self.drawCarObjList(self.carList,self.offset,False,int(self.frameCount/100)%20) 
        self.drawHandObjList(self.handObjList,self.offset)
        self.drawCharacterClassList(self.sheetList[2],self.chara_list,self.offset)
        self.drawAnimationList()
        self.drawMenu(True)
        self.drawHandObjList(self.handObjList,self.offset,True)
        self.drawMenu()
        
    def getAllUsefullList(self):
        returnList = rw.getAllList()
        returnList.extend(mw.getAllList())
        returnList.extend(med.getAllList())
        return returnList
    
    def getUOfromSpriteNum(self,spriteNum,objList):
        for obj in objList :
            if obj.spriteNum == spriteNum : 
                return obj
        return None
    
    def keyMouseAction(self) :
        keyDir,interact,drop,sprint = self.listener.keyAction()
        me = self.getMe()
        if sprint :
            keyDir = [keyDir[0]*self.sprintFactor,keyDir[1]*self.sprintFactor]
            
        if not self.keyMovePlayer :
            self.moveCamera(keyDir)
            
        self.changeDirCharacterList(0.05,self.chara_list,keyDir,me)
        
        self.healthPct = me.healthPct
        meleWepon = self.weponUseAtempt(me)
        self.damageCalculation(me,meleWepon)
        self.healUseAtempt(me)
        self.listener.resetClick()
        self.dropAction(drop,me)
        self.interactAction(interact,me)
        
    def healUseAtempt(self,me) :
        if self.listener.mouseVal[0]!=-1 :
            obj = self.getHandObjFromInventory(self.menuBarSel)
            if obj != None :
                healItem = self.getUOfromSpriteNum(obj[0],self.medList)
                if healItem != None :
                    me.healthPct = min(me.healthPct + healItem.healValue,1)
                    self.dropItem(obj,me,True)
        
    def dropAction(self,dropBool,me) :
        if dropBool and self.dropCooldown==0:
            obj = self.getHandObjFromInventory(self.menuBarSel)
            self.dropItem(obj,me)
        elif self.dropCooldown>0 :
            self.dropCooldown = self.dropCooldown - 1
    
    def dropItem(self,item,me,delete=False) :
        if item!=None :
            if delete :
                item[3] = -4
            else :
                item[3] = -1
            item[1] = me.posMap[0]
            item[2] = me.posMap[1]
            dropIndex = self.inventoryList.index(self.handObjList.index(item))
            self.inventoryList[dropIndex] = -1
            self.inventoryCount = self.inventoryCount - 1
            self.dropCooldown = 10
    def interactAction(self,interBool,me) :
        if interBool :
            takenFlag = False
            if self.inventoryCount<self.maxInventory+1 : 
                for obj in self.handObjList :
                    if not takenFlag and obj[0]!=1 and obj[3]!=-4 and obj[3]!=-5:
                        dist = math.sqrt(math.pow(obj[1]-me.posMap[0],2)+math.pow(obj[2]-me.posMap[1],2))
                        if dist < self.distancePickup :
                            #print("Picked up obj #",obj[0])
                            obj[1] = -100
                            obj[2] = -100
                            avaSpot = self.inventoryAvailableSpot()
                            obj[3] = avaSpot
                            if avaSpot==len(self.inventoryList):
                                self.inventoryList.append(self.handObjList.index(obj))
                            else :
                                self.inventoryList[avaSpot] = self.handObjList.index(obj)
                            self.inventoryCount = self.inventoryCount + 1
                            takenFlag = True
                            
    def damageCalculation(self,me,meleWepon):
        self.moveBullets(me)
        self.meleDamageCalculation(me,meleWepon)

    def meleDamageCalculation(self,me,meleWepon) :
        if self.weponUsedCooldown == self.weponUsedCooldownReset and meleWepon!=None:
            for cha in self.chara_list :
                dist = math.sqrt(math.pow(cha.posMap[0]-me.posMap[0],2)+math.pow(cha.posMap[1]-me.posMap[1],2))
                if not cha.playerControled and dist<(me.attackRange*meleWepon.rangeMulti) :
                    dead = cha.applyDamage(meleWepon.damage,me.damageMulti)
                    if dead :
                        self.killCharacter(cha)
        for cha in self.chara_list :
            if not cha.dead and not cha.playerControled and cha.attackCooldown==0 :
                dist = math.sqrt(math.pow(cha.posMap[0]-me.posMap[0],2)+math.pow(cha.posMap[1]-me.posMap[1],2))
                if dist<cha.attackRange :
                    cha.attackCooldown = 10
                    #print(cha.damageMulti)
                    dead = me.applyDamage(1,cha.damageMulti)
                    if dead :
                        self.killCharacter(me)
            elif not cha.dead and not cha.playerControled and cha.attackCooldown!=0 :
                cha.attackCooldown = cha.attackCooldown -1
            if cha.damageCooldown>0 :
                cha.damageCooldown = cha.damageCooldown -1
    def killCharacter(self,cha) :
        cha.dead = True
        self.animationListPos.append([0,cha.posMap[0],cha.posMap[1],cha.spriteSize[0],cha.spriteSize[1]])
                    
    def moveBullets(self,me) :
        damage = 0.6
        if self.bulletNum>0 :
            for i in range(self.bulletNum) :
                if self.handObjList[i][3] == -2 :
                    self.handObjList[i][1] = me.posMap[0] 
                    self.handObjList[i][2] = me.posMap[1]
    
                if self.handObjList[i][3] == -3 :
                    self.handObjList[i][1] = self.handObjList[i][1]+self.handObjList[i][5][0]
                    self.handObjList[i][2] = self.handObjList[i][2]+self.handObjList[i][5][1]
                    self.handObjList[i][7] = self.handObjList[i][7] + self.handObjList[i][6].speed 
                    if self.objOutOfScreen(self.handObjList[i]) or self.handObjList[i][7]>self.handObjList[i][6].range:
                        self.handObjList[i][3]=-2
                        self.handObjList[i][7] = 0
                    else :  
                        for cha in self.chara_list :
                            dist = math.sqrt(math.pow(cha.posMap[0]-self.handObjList[i][1],2)+math.pow(cha.posMap[1]-self.handObjList[i][2],2))
                            if not cha.playerControled and dist<self.handObjList[i][6].radius :
                                self.handObjList[i][3]=-2
                                dead = cha.applyDamage(self.handObjList[i][6].damage,me.damageMulti)
                                if dead :
                                    self.killCharacter(cha)

                                    

    def weponUseAtempt(self,me):
        weponUsedFlag = False
        meleWeponReturn=None
        if self.listener.mouseVal[0]!=-1 :
            obj = self.getHandObjFromInventory(self.menuBarSel)
            if obj != None :
                rangeWeapon = self.getUOfromSpriteNum(obj[0],self.rwList)
                if rangeWeapon!=None :
                    speed = rangeWeapon.speed

                    bulletDir = [0,0]
                    bulletDir[0] = self.listener.mouseVal[0]-(me.getPosScreen(self.offset)[0])
                    bulletDir[1] = self.listener.mouseVal[1]-(me.getPosScreen(self.offset)[1])
                    distance = math.sqrt(math.pow(bulletDir[0],2)+math.pow(bulletDir[1],2))

                    self.handObjList[self.activeBullet][3] = -3
                    dir2 = [speed*bulletDir[0]/distance,speed*bulletDir[1]/distance]
                    self.handObjList[self.activeBullet][5] = dir2
                    self.handObjList[self.activeBullet][6] = rangeWeapon
                    self.activeBullet = self.activeBullet + 1
                    if self.activeBullet==self.bulletNum :
                        self.activeBullet = 0
                    weponUsedFlag = True
                else :
                    meleWeapon = self.getUOfromSpriteNum(obj[0],self.mwList)
                    if meleWeapon!=None :
                        weponUsedFlag = True
                        meleWeponReturn = meleWeapon
                    
        if weponUsedFlag :
            self.weponUsedCooldown = self.weponUsedCooldownReset
        else :
            if self.weponUsedCooldown>0 :
                #print(self.weponUsedCooldown)
                self.weponUsedCooldown = self.weponUsedCooldown -1
        
        return meleWeponReturn
    
    def objOutOfScreen(self,obj) :
        if obj[1]-self.offset[0] < 0 :
            return True
        if obj[1]-self.offset[0] > self.width :
            return True
        if obj[2]-self.offset[1] < 0 :
            return True
        if obj[2]-self.offset[1] > self.height :
            return True
    
    def inventoryAvailableSpot(self) :
        for i in range(len(self.inventoryList)) :
            if self.inventoryList[i]==-1 :
                return i
        return len(self.inventoryList)
    def scrollCursor(self):
        if self.listener.mouseVal[2] != 0:
            self.menuBarSel = min(max(self.menuBarSel-self.listener.mouseVal[2],0),self.maxInventory)
            self.listener.mouseVal[2] = 0
            
    def objInit(self,val) :
        handObjList = []
        objList = []
        templateList = [[0,[3,3]],[1,[20,3]],[2,[18,24]],[3,[3,27]],[4,[3,41]]]
        if val == 0 :
            self.handObjListBuff = []
            self.objListBuff = []
        if val == 1 :
            self.objListBuff = generateObjList()#[[113,11,9],[114,13,9],[103,25,25],[103,15,30],[104,27,23],[104,32,32]]
            self.handObjListBuff = generateHandObjList()#self.generateTrees()#
        if val == 2 :
            otinst = ot.objectTemplate(0,[3,3])#
            self.objListBuff,self.handObjListBuff = otinst.getTemplateList()
        if val == 3 :
            #handObjList = [[8,1000,1000,-1],[40,1100,1000,-1],[41,1200,1000,-1],[5,1250,1000,-1]]
            self.handObjListBuff = []
            for i in range(len(self.shootWeaponsObj)) :
                self.handObjListBuff.append([self.shootWeaponsObj[i],1000+i*50,1000,-1])
            for i in range(len(self.meleWeponsObj)) :
                self.handObjListBuff.append([self.meleWeponsObj[i],1000+i*50,1100,-1])
            for i in range(len(self.medicineObj)) :
                self.handObjListBuff.append([self.medicineObj[i],1000+i*50,1200,-1])
            self.objListBuff = []
        if val == 4 :
            self.handObjListBuff = []
            self.objListBuff = []
            for i in range(6) :
                self.carList.append([i,i*100+200,1000+i*100])
        if val == 5 :
            otinst = ot.objectTemplate(3,[3,27])#
            self.objListBuff,self.handObjListBuff = otinst.getTemplateList()
            #self.handObjListBuff = []
            #self.objListBuff = [[-161,4,29],[-161,4,31],[-161,4,33]]
        if val == 6 :
            otinst = ot.objectTemplate(1,[20,3])#
            self.objListBuff,self.handObjListBuff = otinst.getTemplateList()
        if val == 7 :
            otinst = ot.objectTemplate(2,[18,24])#
            self.objListBuff,self.handObjListBuff = otinst.getTemplateList()
        if val == 8 :
            otinst = ot.objectTemplate(4,[3,41])#
            self.objListBuff,self.handObjListBuff = otinst.getTemplateList()
        if val == 9 :    
            self.objListBuff,self.handObjListBuff = self.templateListToObjList(templateList)
        self.handObjList = self.generateBullets()
        lootList = self.generateLoot(10)
        self.handObjList.extend(lootList)
        self.handObjList.extend(self.handObjListBuff)
        
        self.objList = self.objListBuff
        print("len obj list",len(self.objList))
    
    def templateListToObjList(self,tempList) :
        self.objListBuff = []
        self.handObjListBuff = []
        for temp in tempList :
            otinst = ot.objectTemplate(temp[0],temp[1])#
            objList,handObjList = otinst.getTemplateList()
            self.objListBuff.extend(objList)
            self.handObjListBuff.extend(handObjList)
            del(otinst)
        return self.objListBuff,self.handObjListBuff
    def generateBullets(self) :
        bulletList = []
        for i in range(self.bulletNum) :
            bulletList.append([1,0,0,-2])
            
        return bulletList
    def generateLoot(self,num) :
        lootList = []
        for i in range(num) :
            lootList.append([30,0,0,-5])
            
        return lootList
    def generateTrees(self,treeList=[103,104],area=[20,20,40,40],frequency=0.1) :
        objList = []
        for x in range(area[0],area[2]) :
            for y in range(area[1],area[3]) :
                if random.random()<frequency :
                    objList.append([treeList[int(random.random()*len(treeList))],x,y])
        return objList

    
    def resetMemAndCanvas(self):
        #pass
        self.canvas.delete("all")
        #del(self.canvas)
        #del(self.spriteListMem)
        #self.spriteListMem = []
        #self.canvas = self.getCanvasFullScreen(self.root,self.width,self.height,self.backgroundColor)
        #self.canvas = self.drawBackground(self.canvas,self.width,self.height,self.backgroundColor)
        

    def drawObjList(self,objMat,objSheet,offset=[0,0],dontDisplay=False):
        step_x = (objSheet[1]/objSheet[3])
        step_y = (objSheet[2]/objSheet[4])
        objIdList = []
        for obj in objMat :
            img = self.object.getSprite(obj[0])
            if not dontDisplay :
                objIdList.append(self.canvas.create_image(obj[1]*step_x-offset[0],obj[2]*step_y-offset[1], image=img, anchor="nw"))
        self.objIdList = objIdList
    
    def drawCarObjList(self,objMat,offset=[0,0],dontDisplay=False,forceAngle=0):
        for obj in objMat :
            print(obj[0])
            img = self.objectCar.getCarSprite(obj[0],forceAngle)
            if not dontDisplay :
                self.canvas.create_image(obj[1]-offset[0],obj[2]-offset[1], image=img, anchor="nw")

        
    def drawHandObjList(self,objHandMat,offset=[0,0],inventory=False):
        for obj in objHandMat :
            if obj[3]==-1 or obj[3]==-3:
                if not inventory :
                    img = obj[4][0]
                    self.canvas.create_image(obj[1]-offset[0]-(int(img.width()/2)),obj[2]-offset[1]-int(img.height()/2), image=img, anchor="nw")
            else :
                if inventory and obj[3]>-1:
                    img = obj[4][1]
                    self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2))+5+4+50*obj[3],self.height-self.menuSize[1]+5+4, image=img, anchor="nw")
                    if (obj[0] in self.shootWeaponsObj or obj[0] in self.meleWeponsObj) and self.menuBarSel==obj[3]:
                        if self.weponUsedCooldown>0 :
                            img = obj[4][2]
                        else :
                            img = obj[4][0]
                        me = self.getMe()
                        self.canvas.create_image(me.getPosScreen(self.offset)[0]+15,me.getPosScreen(self.offset)[1]+15, image=img, anchor="nw")
    def drawMenu(self,background=False) :
        if background :
            self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2)),self.height-self.menuSize[1], image=self.menuImageList[1], anchor="nw")
            
        else :
            hbar = self.menuImageList[4]
            width, height = hbar.size
            box = ([0,0,int(width*self.healthPct),10])
            hbar=hbar.crop(box)
            self.imgHealthBar = ImageTk.PhotoImage(hbar)
            self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2)),self.height-self.menuSize[1], image=self.menuImageList[0], anchor="nw")
            self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2))+80,self.height-self.menuSize[1]-15, image=self.menuImageList[3], anchor="nw")
            self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2))+80,self.height-self.menuSize[1]-10, image=self.imgHealthBar, anchor="nw")
            self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2))-5+self.menuBarSel*50,self.height-60, image=self.menuImageList[2], anchor="nw")
            
        return None
    def drawCharacter(self,characterSheetSettings,img,dispX,dispY,name="",pc=False) :
        step_x = (characterSheetSettings[1]/characterSheetSettings[3])
        step_y = (characterSheetSettings[2]/characterSheetSettings[4])
        self.canvas.create_image(dispX,dispY, image=img, anchor="nw")
        if name!="" and self.displayName :
            bold = ""
            fontSize = int(8)
            if pc :
                fontSize = int(10)
                bold = "bold"
            self.drawText(name,dispX+int(step_x*self.zoom/2),dispY-int(fontSize/2+step_y*self.zoom/15),fontSize,bold,False)
            #self.canvas.create_text(dispX+int(step_x*self.zoom/2),dispY-int(fontSize/2+step_y*self.zoom/15), text=name, fill="black", font=('Helvetica '+str(fontSize)+" bold"))

    def drawText(self,text,posX,posY,fontSize,bold,background) :
        if background :
            self.canvas.create_rectangle(posX-(len(text)*(fontSize/2)),posY-int(fontSize/2)-1,posX+(len(text)*(fontSize/2)),posY+int(fontSize/2)+3,outline="",fill="lightgray")
        self.canvas.create_text(posX,posY, text=text, fill="black", font=('Helvetica '+str(fontSize)+" "+bold))

    def drawCharacterClass(self,characterSheetSettings,character,offset=[0,0]) :
        self.drawCharacter(characterSheetSettings,character.returnSpriteFromMotion(),character.getPosScreen(offset)[0],character.getPosScreen(offset)[1],character.name,character.playerControled)
    
    def drawCharacterClassList(self,characterSheetSettings,characterList,offset=[0,0]) :
        for character in characterList :
            self.drawCharacterClass(characterSheetSettings,character,offset)
    
    def drawBackgroundSheet(self,backSettings,posX,posY) :
        return self.canvas.create_image(posX,posY, image=self.backList[0][0], anchor="nw")    
    
    def drawAnimationList(self) :
        for i in self.animationListPos :
            img = self.animationList[i[0]]
            self.canvas.create_image(i[1]-int(i[3]/2)-self.offset[0],i[2]-int(i[4]/2)-self.offset[1], image=img, anchor="nw")
   
    def moveCamera(self,keyDir,speed=15) :
        self.offset = [self.offset[0]+speed*keyDir[0],self.offset[1]+speed*keyDir[1]]
    
    #Load texture
    def generateNewMap(self,generate=False) :
        if generate :
            self.terrain = tb.terrain_builder(self.sheetList[1],self.sheetList[3],True)
            self.terrain.mapFileToImage(self.mapList[0],self.rootPath)
            del(self.terrain)
            del(self.mapList)
    def openSheetList(self) :
        for sheetNum in range(len(self.sheetList)) :
            img = Image.open(self.rootPath+self.textureFolder+self.sheetList[sheetNum][0]).convert("RGBA")
            self.sheetList[sheetNum][0] = img
            
    def openMapList(self) :
        for mapNum in range(len(self.mapList)) :
            img = Image.open(self.rootPath+self.mapList[mapNum][0]).convert("RGB")
            self.mapList[mapNum][0] = img
    
    def openBackgroundList(self) :
        for backNum in range(len(self.backList)) :
            img = Image.open(self.rootPath+self.backList[backNum][0]).convert("RGBA")
            
            self.backList[backNum][0] = ImageTk.PhotoImage(img)
            if len(self.backList[backNum])>5:
                img = Image.open(self.rootPath+self.backList[backNum][5]).convert("RGB")
                boolMat = [[False for x in range(self.backList[backNum][4])] for y in range(self.backList[backNum][3])] 
        
                colorMat = np.array(list(img.getdata())).reshape((self.backList[backNum][3], self.backList[backNum][4], 3))
                for x in range(self.backList[backNum][3]-1) :
                    for y in range(self.backList[backNum][4]-1) :
                        if colorMat[x][y][0]==0:
                            boolMat[x][y] = True
                self.backList[backNum][5] = boolMat
            else :
                self.backList[backNum].append(None)
    
    def imageToMask(self,img,transparentCol=(0,0,0,0),fillCol=(255, 0, 0, 100)) :

        data = img.getdata()
        newData = []
        for item in data:
            if item[0] > 0 or item[1] > 0 or item[2] > 0:
                newData.append(fillCol)
            else:
                newData.append(transparentCol)
        img.putdata(newData)
        return img
    def loadImageCharacterList(self,characterSheetSettings) :
        for j in range(len(self.chara_list)) :
            for i in [0,1,2,-2,3] :
                x,y = self.caracterSelection(self.chara_list[j].spriteNum,abs(i))
                img = characterSheetSettings[0]

                step_x = (characterSheetSettings[1]/characterSheetSettings[3])
                step_y = (characterSheetSettings[2]/characterSheetSettings[4])
                box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
                img = img.crop(box)

                if i == 3 :
                    imgcop = img.copy()
                    mask = self.imageToMask(imgcop)
                    img = Image.alpha_composite(img,mask)
                if i<0:
                    img = img.transpose(Image.FLIP_LEFT_RIGHT)
                img2 = ImageTk.PhotoImage(img.resize((int(step_x*self.zoom),int(step_y*self.zoom)), resample=self.resampleType))#
                
                self.chara_list[j].spriteList.append(img2)
            self.chara_list[j].setSpriteSize()
    
    def loadImageHandObjList(self,characterSheetSettings,mirror=False) :
        for j in range(len(self.handObjList)) :
            x,y = self.handObjSelection(self.handObjList[j][0])
            img = characterSheetSettings[0]
            step_x = (characterSheetSettings[1]/characterSheetSettings[3])
            step_y = (characterSheetSettings[2]/characterSheetSettings[4])
            box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
            img = img.crop(box)
            if mirror:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            imageSmall = img.resize((int(step_x*self.zoomHandObj),int(step_y*self.zoomHandObj)), resample=self.resampleType)
            img2 = ImageTk.PhotoImage(imageSmall)
            img3 = ImageTk.PhotoImage(img)
            img4 = ImageTk.PhotoImage(imageSmall.rotate(-90))
            self.handObjList[j].append([])
            self.handObjList[j][4].append(img2)
            self.handObjList[j][4].append(img3)
            self.handObjList[j][4].append(img4)
            self.handObjList[j].append([0,0])
            self.handObjList[j].append(0)
            self.handObjList[j].append(0)

    def loadImageMenuList(self,menuSheetSettings,mirror=False) :
        for coord in range(1,6) :
            img = Image.open(self.rootPath+self.textureFolder+menuSheetSettings[0][0]).convert("RGBA")
            box = (menuSheetSettings[0][coord])
            img = img.crop(box)
            if coord==5 :
                self.menuImageList.append(img)
            else :
                img2 = ImageTk.PhotoImage(img)
                self.menuImageList.append(img2)
                
    def loadImageAnimationList(self,characterSheetSettings):
        for i in range(1) : 
            x,y = self.animationSelection(i)
            img = characterSheetSettings[0]
            step_x = (characterSheetSettings[1]/characterSheetSettings[3])
            step_y = (characterSheetSettings[2]/characterSheetSettings[4])
            box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
            img = img.crop(box)
            img2 = ImageTk.PhotoImage(img)#
            self.animationList.append(img2)
            

    #Create characters
    def getRandCh(self,spawnRange=[[0,500],[0,500]],collisionMat=None,speedRange=[2,10],peopleAttackRange=[30,30],peopleDamageMultiRange=[1,1]) :
        canMove = False
        while not canMove :
            randPos = [int(float(random.random()*float(spawnRange[0][1]-spawnRange[0][0]))+float(spawnRange[0][0])),int(float(random.random()*float(spawnRange[1][1]-spawnRange[1][0]))+float(spawnRange[1][0]))]
            cha = ch.character(int((random.random()*self.totalCharacterSprite)),randPos)
            if collisionMat!=None :
                if self.characterCanMove(cha,collisionMat) :
                    canMove = True  
            else :
                canMove = True 
        cha.speed = randomFloatRange(speedRange)
        cha.attackRange = randomFloatRange(peopleAttackRange)
        cha.damageMulti = randomFloatRange(peopleDamageMultiRange)
        return cha
    
    def getRandChList(self,n,spawnRange=[[0,500],[0,500]],collisionMat=None,speedRange=[2,10],peopleAttackRange=[30,30],peopleDamageMultiRange=[1,1]) :
        ch_list = []
        for i in range(n) :
            ch_list.append(self.getRandCh(spawnRange,collisionMat,speedRange,peopleAttackRange,peopleDamageMultiRange))
        return ch_list
    
    def getMe(self) :
        for c in self.chara_list :
            if c.playerControled :
                return c
        return None
    
    def createMe(self,spriteNum,pos=[0,0]) :
        character_me = ch.character(spriteNum,pos)
        character_me.playerControled = True
        character_me.name = "Alex" 
        self.chara_list.append(character_me)
        self.offset = [pos[0]-int(self.width/2),pos[1]-int(self.height/2)]
    
    def createMeFull(self,myName,mySprite,myGender,myRandomName,mySpeed,myPosition,myHealth,myAttackRange,myDamageMulti) :
        character_me = ch.character(mySprite,myPosition,myRandomName,myName,myGender)
        character_me.playerControled = True
        character_me.speed = mySpeed
        character_me.posMap = myPosition
        character_me.healthPct = myHealth
        character_me.attackRange = myAttackRange
        character_me.damageMulti = myDamageMulti
        self.chara_list.append(character_me)
        self.offset = [character_me.posMap[0]-int(self.width/2),character_me.posMap[1]-int(self.height/2)]
        
    def getAllChList(self) :
        ch_list = []
        for i in range(100) :
            chara = ch.character(i,[i*30,50])
            chara.name = str(i)
            ch_list.append(chara)
        return ch_list
    

    def moveCharacterList(self,chList,collisionMat=None) :
        for c in chList :
            if self.characterCanMove(c,collisionMat,True) and not c.dead:
                c.move()
                if c.playerControled :
                    screenPos = [c.posMap[0]-self.offset[0],c.posMap[1]-self.offset[1]]
                    if screenPos[0]<self.width*self.pctScreenScroll :
                        self.offset[0] = self.offset[0]+c.movingDir[0]
                    if screenPos[0]>self.width-self.width*self.pctScreenScroll :
                        self.offset[0] = self.offset[0]+c.movingDir[0]
                    if screenPos[1]<self.height*self.pctScreenScroll :
                        self.offset[1] = self.offset[1]+c.movingDir[1]
                    if screenPos[1]>self.height-self.height*self.pctScreenScroll :
                        self.offset[1] = self.offset[1]+c.movingDir[1]

    def characterCanMove(self,c,collisionMat=None,future=False) :
        if collisionMat==None :
            return True
        else :
            colSizeY = len(collisionMat)-1
            colSizeX = len(collisionMat[0])-1
            if future :
                newcoo = [int((c.posMap[0] + c.movingDir[0]*2)/32),int((c.posMap[1] + c.movingDir[1]*2)/32)]
            else :
                newcoo = [int(c.posMap[0]/32),int(c.posMap[1]/32)]
            if not collisionMat[min(max(newcoo[1],0),colSizeY)][min(max(newcoo[0],0),colSizeX)] :# and not collisionMat[newcoo[1]+1][newcoo[0]+1] and not collisionMat[newcoo[1]+1][newcoo[0]] and not collisionMat[newcoo[1]][newcoo[0]+1] :
                return True
            else :
                return False
            
    def changeDirCharacterList(self,p,chList,direction=[0,0],player=None) :
        for c in chList :
            if c.playerControled and self.keyMovePlayer :
                c.changeDir(direction)
            else :
                if c.movingPattern == 0 :
                    c.movingDir = [0,0]
                elif c.movingPattern == 1 :
                    c.changeDirRand(self.changeDirectionFrequency,self.stopMovingFrequency)
                elif c.movingPattern == 2 :
                    c.folowPlayer(player,player.dead)
                elif c.movingPattern == 3 :
                    c.folowPlayer(player,player.dead,self.characterVision,self.changeDirectionFrequency,self.stopMovingFrequency)

            
    def getHandObjFromInventory(self,i) :
        for obj in self.handObjList :
            if obj[3] == i :
                return obj
        return None
    
    #Dev display            
    def displayTerrain(self) :
        for i in range(32) :
            for l in range(31) :
                self.canvas.create_image(35*i,35*l, image=self.terrain.imageMat[i][l], anchor="nw")#int(sheetList[0][1]/2),int(sheetList[0][2]/2)
                self.canvas.create_text(35*i+10,35*l+5, text=str(i)+","+str(l), fill="black", font=('Helvetica 10'))
    
    def displayCharacter(self) :
        for i in range(99) :
            for l in range(2) :
                self.canvas.create_image(35*i,35*l, image=self.chara_list[i].spriteList[l], anchor="nw")#int(sheetList[0][1]/2),int(sheetList[0][2]/2)
                self.canvas.create_text(35*i+10,35*l+5, text=str(i), fill="black", font=('Helvetica 10'))
    
    #Selections
    def caracterSelection(self,cara_num,sprite_num) :
        startPoint = [10,17]
        x = 10
        y = 17
        if cara_num > 100 :
            cara_num = 100
        if cara_num >86  :
            cara_num = cara_num+3
        if cara_num >50  :
            cara_num = cara_num+7
        if cara_num > 14     :
            cara_num = cara_num-15
            x = x + 6
            if cara_num>31 :
                cara_num = cara_num - 32
                x = x + 4
                if cara_num>31 :
                    cara_num = cara_num - 32
                    x = x + 4
                    if cara_num>31 :
                        cara_num = cara_num - 32
                        x = x + 4
            y = cara_num
        else :
            y = y + cara_num
            if cara_num>6 and cara_num<15 :
                x = x - 1
        x = x + sprite_num
        return x,y
    
    def handObjSelection(self,objNum) :
        if objNum<100 :
            x = 14
            y = 0
            if objNum >31 :
                objNum = objNum - 32
                x = x + 1
                if objNum >31 :
                    x = 12
                    objNum = objNum - 32
                    if objNum > 9 :
                        x = x + 1
                        objNum = objNum - 10
                        if objNum > 12 :
                            objNum = 12
            y = objNum
        else :
            x = 5
            y = 0
            xoff = int(objNum/100)
            objNum = objNum - xoff*100
            xoff = xoff - 1
            if xoff==0 and objNum in [15,16,17,18,20,22,28,29] :
               xoff = 1 
            y = objNum
            x = x + xoff
        return x,y
  
    def animationSelection(self,animNum) :
        return 10,16
    #Window
    def setRoot(self,width,height,offx=0,offy=0,top=True,fullscreen=False,resizable=True,zoom=True):
        root = tk.Tk()
        if type(width)!=type(None) :
            width_return = width
        else :
            width_return = root.winfo_screenwidth()
        if type(height)!=type(None) :
            height_return = height
        else :
            height_return = root.winfo_screenheight()
        root.geometry(str(width_return)+"x"+str(height_return)+"+"+str(offx)+"+"+str(offy))
        if top :
            root.attributes('-topmost',1)   
        root.resizable(resizable, resizable)
        if zoom :
            root.state('zoomed')
        root.attributes("-fullscreen",fullscreen)
        root.attributes('-alpha', 1)
        return root,width_return,height_return
        
    def getCanvasFullScreen(self,root,width,height,color,borderwidth=-2):
        canvas = Canvas(root, width = width, height = height, bg=color,borderwidth=borderwidth)
        canvas = self.drawBackground(canvas,width,height,color)
        return canvas
        
    def drawBackground(self,canvas,width,height,color):
        canvas.create_rectangle(-10, -10, width+10, height+10, fill=color)
        return canvas
    def pasteConf(self,confVal,defaultVal) :
        if self.useConf :
            return confVal
        else :
            return defaultVal
    
    def printRessources(self) :
        chList = get_size(self.chara_list)
        handObj = get_size(self.handObjList)
        objList = get_size(self.objList)
        sheetList = get_size(self.sheetList)
        bgList = get_size(self.backList)
        obBuilder = get_size(self.object)
        total = obBuilder + bgList + sheetList + objList + handObj + chList
        print("Character list size :",chList,"(len :",len(self.chara_list),")")
        print("Hand obj list size :",handObj,"(len :",len(self.handObjList),")")
        print("Obj list size :",objList,"(len :",len(self.objList),")")
        print("Sheet list size :",sheetList,"(len :",len(self.sheetList),")")
        print("Background list size :",bgList,"(len :",len(self.backList),")")
        print("Objet builder class :",obBuilder)
        print("Total window :",total)

def randomFloatRangeFromTo(fromVal,toVal):
    return (float(random.random()*float(toVal-fromVal))+float(fromVal))

def randomFloatRange(valRange):
    return randomFloatRangeFromTo(valRange[0],valRange[1])
    
def printFPS(start=0,end=0) :
    print("Generated in "+str(round(end-start,6))+"s  ("+str(round(1/max((end-start),0.0001),3))+" FPS)")
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size
    

def generateHandObjList() :
    x = 1000
    y = 500
    objList = []
    for i in range(87) :
        objList.append([i,int(x+((i%10)*50)),int(y+(int(i/10)*50)),-1])
    x = 1000
    y = 1000
    for i in range(32) :
        for j in range(4) :
            objList.append([((j+1)*100)+i,int(x+i*50),int(y+j*50),-1])
    return objList

def generateObjList() :
    x = 50
    y = 50
    objList = []
    for i in range(27) :
        objList.append([i,int(x+i),int(y)])
    x = 50
    y = 55
    for i in range(30,57) :
        objList.append([i+100,int(x+(i%5)*4),int(y+int(i/5)*3)])
    return objList
sl = window(cf.configLoader())