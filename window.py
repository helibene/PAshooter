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
import carObject as co
import characterAction as ca
import openImageFiles as oi
import windowUtil as wu
import lootSelection as ls
import handObject as ho
class window :
    def __init__(self,conf=None):
        print(" ==== PROGRAM START ====")
        startTimeInit = time.time()
        self.conf = conf
        self.useConf = False
        if conf!=None :
            self.useConf = True
        #self.handObjUsefullList = self.getAllUsefullList()

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
        self.zoom = 1
        self.offset = [1000,1000]
        self.displayName = True
        self.menuSize = [655,55]
        self.menuImageList = []
        self.inventoryList = []
        self.dropCooldown = 0
        self.pickupCooldown = 0
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
        self.toggleStatDisplay = False
        self.rwList = rw.getAllList()
        self.mwList = mw.getAllList()
        self.medList = med.getAllList()
        self.characterVision = 300
        self.frameCount = 0
        displayFPS = False
        printResources = False
        self.objMapImage = None
        self.objMapImageRaw = None
        self.carAngleNum = 35
        self.moneyCount = 9
        self.currentFPS = 0
        self.currentFPSavg = 0
        self.toggleStatCooldown = 0
        self.saveObjImage = False
        self.mapRawFolder = "raw/"
        self.mapTextureFolder = "texture/"
        self.mapObjectFolder = "object/"
        self.mapCollisionFolder = "collision/"
        self.mapRawSplitFolder = "split/"
        self.packAllBack = False
        
        self.rootPath = self.pasteConf(self.conf.spritePath,"C:/Users/Alexandre/Desktop/PAshooter/sprites/")
        self.textureFolder = self.pasteConf(self.conf.textureFolder,"texture/")
        self.mapFolder = self.pasteConf(self.conf.mapFolder,"map/")
        self.terrainTileSize = self.pasteConf(self.conf.terrainTileSize,32)
        self.mapInstance = self.pasteConf(self.conf.mapInstance,1)
        self.splitMapImage = self.pasteConf(self.conf.splitMapImage,[0,0])
        self.zoomHandObj = self.pasteConf(self.conf.itemSize,0.7)
        self.generate_new_map = self.pasteConf(self.conf.generateNewMap,False)
        self.maxInventory = self.pasteConf(self.conf.maxInventorySize,12)
        self.distancePickup = self.pasteConf(self.conf.distancePickupPixel,30)
        self.healthPct = self.pasteConf(self.conf.startHealth,1)
        self.bulletNum = self.pasteConf(self.conf.maxBulletOnScreen,10)
        self.sprintFactor = self.pasteConf(self.conf.sprintMultiplier,2)
        self.weponUsedCooldownReset = self.pasteConf(self.conf.weponFrameCooldown,10)
        self.jpegQuality = self.pasteConf(self.conf.jpegQuality,0.5)
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
        myName = self.pasteConf(self.conf.myName,"")
        mySprite = self.pasteConf(self.conf.mySprite,0)
        myGender = self.pasteConf(self.conf.myGender,"M")
        myRandomName = self.pasteConf(self.conf.myRandomName,"True")
        mySpeed = self.pasteConf(self.conf.mySpeed,1)
        myPosition = self.pasteConf(self.conf.myPosition,[0,0])
        myHealth = self.pasteConf(self.conf.myHealth,1)
        myDamageMulti = self.pasteConf(self.conf.myDamageMulti,1)
        myAttackRange = self.pasteConf(self.conf.myAttackRange,30)
        
        #print(self.splitMapImage)
        #Sprites conf
        self.shopAreaList = []#[[0*32,0*32],[0*32,0*32]]#[[27*32,54*32],[37*32,64*32]]
        self.sheetList = [["objects3.png",1504,1024,47,32],["terrain3.png",1024,992,32,31],["caracteres3.png",1200,1200,32,32],["black.png",1,1,1,1],["nature2.png",896,992,28,31],["vehicule.png",864,864,27,27]]#["objects2.png",800,1024,25,32]
        self.menuList = [["menu3.png",[0,0,655,55],[0,55,655,110],[0,110,65,175],[0,175,505,190],[0,190,505,200],[0,206,96,263],[704,0,896,192]]]
        self.mapList,self.backList = self.generateMapConfig(self.mapInstance)
        self.mapList2 = []
        self.root,self.width,self.height = wu.setRoot(self,width,height,0,0,windowOnTop,fullscreen,True,True)       
        self.canvas = wu.getCanvasFullScreen(self,self.root,self.width,self.height,self.backgroundColor)
        self.carList = []
        self.carObjList = []
        self.object,self.objectCar = oi.masterOpen(self)
        self.chara_list = self.getRandChList(peopleSpawnNum,[peopleSpawnRangeX,peopleSpawnRangeY],self.backList[0][5],peopleSpeedRange,peopleAttackRange,peopleDamageMultiRange)
        self.createMeFull(myName,mySprite,myGender,myRandomName,mySpeed,myPosition,myHealth,myAttackRange,myDamageMulti)
        self.objInit(objInitInstance)

        oi.masterLoad(self)
        if self.saveObjImage :
            oi.masterSaveObjImage(self)
        self.listener = lb.ListenerBundle()

        self.drawObjList(self.objList,self.sheetList[0],self.offset,True)
        self.drawCarObjList(self.offset,True)
        self.object.deleteSpriteMatrix()
        self.objectCar.deleteSpriteMatrix()
        
        self.isShoping = False 
        #print(len(self.backList))
        if printResources :
            self.printRessources()
        endTimeInit = time.time()
        print("Init done in ",round(float(endTimeInit)-float(startTimeInit),2),"sec")
        while True :
            self.frameCount = self.frameCount + 1
            start = time.time()
            self.drawBundle()
            self.canvas.pack()
            self.root.update()
            time.sleep(waitBetweenFrames)

            self.scrollCursor()
            ca.master(self)
            self.moveCharacterList(self.chara_list,self.backList[0][5])
            self.moveCarList()
            end = time.time()
            self.fpsHandeling(start,end,displayFPS,fpsList)
            self.resetMemAndCanvas()
        self.root.mainloop() 

        
    def drawBundle(self) :
        self.drawBackgroundSheet(self.backList,-self.offset[0],-self.offset[1])
        self.drawObjList(self.objList,self.sheetList[0],self.offset,False,self.saveObjImage)  
        self.drawCarObjList(self.offset)
        self.drawHandObjList(self.handObjListClass,self.offset)
        self.drawCharacterClassList(self.sheetList[2],self.chara_list,self.offset)
        self.drawAnimationList()
        self.drawMenu(True)
        self.drawHandObjList(self.handObjListClass,self.offset,True)
        self.drawMenu()
        if self.toggleStatDisplay :
            self.drawStats()
    
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
            
    def moveCarList(self) :
        for i in range(len(self.carObjList)) :
            self.carObjList[i].applyAcceleration()
            if self.carObjList[i].vehiculeType=="boat" :
                self.carObjList[i].canMove(self.backList[0][6],True)
            if self.carObjList[i].vehiculeType=="car" :
                self.carObjList[i].canMove(self.backList[0][5],False,0.9)
            self.carObjList[i].move()
    ###############
    #Player Action#
    ###############
    
    def objOutOfScreen(self,obj) :
        if obj.pos[0]-self.offset[0] < 0 :
            return True
        if obj.pos[0]-self.offset[0] > self.width :
            return True
        if obj.pos[1]-self.offset[1] < 0 :
            return True
        if obj.pos[1]-self.offset[1] > self.height :
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
        #print("objInit   val :",val)
        if val == 0 :
            self.handObjListBuff = []
            self.objListBuff = []
        if val == 1 :
            self.objListBuff,self.handObjListBuff,shopAreaList = ot.objectTemplate(0).templateListToObjList(0)
            self.shopAreaList = shopAreaList
        if val == 2 :
            self.objListBuff,self.handObjListBuff,shopAreaList = ot.objectTemplate(0).templateListToObjList(1)
            self.carObjList.append(self.loadCarObj(co.carObject(5,[32*115,32*150])))
        if val == 3 :
            self.objListBuff,self.handObjListBuff,shopAreaList = ot.objectTemplate(0).templateListToObjList(3)
            self.shopAreaList = shopAreaList
        if val == 4 :
            self.handObjListBuff = []
            self.objListBuff = []
            car = self.loadCarObj(co.carObject(10,[500,1500]))
            self.carObjList.append(car)
        if val == 5 :
            self.objListBuff,self.handObjListBuff,shopAreaList = ot.objectTemplate(0).templateListToObjList(4)
            self.shopAreaList = shopAreaList
        if val == -1 :
            self.handObjListBuff = generateHandObjList()
            self.objListBuff = []
        if val == -2 :
            self.handObjListBuff = []
            for i in range(len(self.rwList)) :
                self.handObjListBuff.append(ho.handObject(0,[i*35+20,20]).initRangeWeapon(self.rwList[i]))
            for i in range(len(self.mwList)) :
                self.handObjListBuff.append(ho.handObject(0,[i*35+20,70]).initMeleWeapon(self.mwList[i]))
            for i in range(len(self.medList)) :
                self.handObjListBuff.append(ho.handObject(0,[i*35+20,120]).initMedicine(self.medList[i]))
            self.handObjListBuff.append(ho.handObject(0,[20,170]).initMoneyBag(10))
            self.objListBuff = []
        if val == -3 :    
            self.objListBuff = generateObjList()
            self.handObjListBuff = []
        if val == -4 :
            self.handObjListBuff = []
            self.objListBuff = []
            for i in range(7) :
                if i<8 :
                    car = self.loadCarObj(co.carObject(i,[200+i*200,200]))
                elif i<12 :
                    car = self.loadCarObj(co.carObject(i,[2500,600+(i-8)*400]))
                else :
                    car = self.loadCarObj(co.carObject(i,[200+(i-12)*500,1000]))
                self.carObjList.append(car)
        if val == -5 :
            self.handObjListBuff = []
            self.objListBuff = []
            car = self.loadCarObj(co.carObject(10,[500,50*32]))
            self.carObjList.append(car)
        self.handObjListClass = self.generateBullets()
        lootList = self.generateLoot()
        self.handObjListClass.extend(lootList)
        self.handObjListClass.extend(self.handObjListBuff)
        self.objList = self.object.addMetadataToObjList(self.objListBuff)
        self.handObjListClass = ho.getBasicInstanceList(self.handObjListClass)
        
    #########################
    #Generate class instance#
    #########################
    
    def loadCarObj(self,car) :
        if car.vehiculeType == "car" :
            for i in range(self.carAngleNum) :
                sprite = self.objectCar.getCarSprite(car.spriteNum,i,self.carAngleNum+1)#,spriteSizeX,spriteSizeY
                car.sprite.append(sprite)
        else :
            sprite2 = self.objectCar.getCarSprite(car.spriteNum,0,self.carAngleNum+1)
            sprite3 = self.objectCar.getCarSprite(car.spriteNum,0,self.carAngleNum+1,True)
            car.sprite.append(sprite2)
            car.sprite.append(sprite3)
        w,h = self.objectCar.getCarSize(car.spriteNum)
        car.spriteSize = [max(w,h)+20,max(w,h)+20]
        car.sizeX = w
        car.sizeY = h
        if car.spriteNum==6 :
            car.maxSpeed = 100
            car.accMulti = 2
            car.frictionPct = 0.1
        return car
    
    def generateBullets(self) :
        bulletList = []
        for i in range(self.bulletNum) :
            obj = ho.handObject()
            bullet = obj.initBullet()
            bulletList.append(bullet)
        return bulletList
    
    def generateLoot(self) :
        lootList = []
        lootSel = ls.lootSelection()
        for cha in self.chara_list :
            lootNum = int(float(random.random()*float(cha.lootNumRange[1]-cha.lootNumRange[0]))+float(cha.lootNumRange[0]))
            for i in range(lootNum) :
                loot = lootSel.getItemFromTemplate(None)
                lootList.append(loot)
                cha.lootList.append(loot)
        return lootList
    
    #def generateNature(self)
    def resetMemAndCanvas(self):
        self.canvas.delete("all")

    ################
    #Draw on canvas#
    ################
    
    def drawObjList(self,objMat,objSheet,offset=[0,0],dontDisplay=False,useImageMap=False):
        if useImageMap :
            self.canvas.create_image(-offset[0],-offset[1],image=self.objMapImage, anchor="nw")
        step_x = (objSheet[1]/objSheet[3])
        step_y = (objSheet[2]/objSheet[4])
        for obj in objMat :
            if not useImageMap or (useImageMap and obj[3][0]!='none') :
                img = self.object.getSprite(obj[0])
                if obj[3][0]=='cabinet':
                    img2 = self.object.getSprite(obj[3][2])
                if not dontDisplay :
                    self.canvas.create_image(obj[1]*step_x-offset[0],obj[2]*step_y-offset[1], image=img, anchor="nw")
            
    
    def drawCarObjList(self,offset=[0,0],dontDisplay=False,forceAngle=0):
        for car in self.carObjList :
            if forceAngle==0 and not dontDisplay:
                forceAngle = car.angle
            if not dontDisplay :
                forceAngle = car.updateAngle(self.carAngleNum)
                img = car.sprite[forceAngle]
                self.canvas.create_image(car.pos[0]-offset[0]-int(car.spriteSize[0]/2),car.pos[1]-offset[1]-int(car.spriteSize[1]/2), image=img, anchor="nw")

        
    def drawHandObjList(self,objHandMat,offset=[0,0],inventory=False):
        for obj in objHandMat :
            if not obj.doNotDisplayOnMap :
                if not inventory :
                    img = obj.spriteList[0]
                    self.canvas.create_image(obj.pos[0]-offset[0]-(int(img.width()/2)),obj.pos[1]-offset[1]-int(img.height()/2), image=img, anchor="nw")
            if obj.itemInInventory and obj.posInventory != -1 and inventory :
                me = self.getMe()
                img = obj.spriteList[1]
                self.canvas.create_image(int(self.width/2-(self.menuSize[0]/2))+5+4+50*obj.posInventory,self.height-self.menuSize[1]+5+4, image=img, anchor="nw")
                if (obj.itemType == "rangeWeapon" or obj.itemType == "meleWeapon") and self.menuBarSel==obj.posInventory and me.inCar==-1:
                    if self.weponUsedCooldown>0 :
                        img = obj.spriteList[2]
                    else :
                        img = obj.spriteList[0]
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
            self.canvas.create_image(10,10, image=self.menuImageList[5], anchor="nw")
            #self.canvas.create_image(self.width-(896-704),0, image=self.menuImageList[6], anchor="nw")
            moneyStr = str(self.moneyCount)#[704,0,896,192]
            moneySize = len(moneyStr)
            self.canvas.create_text(94-10*moneySize+10-10,25+10+5, text=moneyStr, fill="black", font=("Helvetica 25 bold"))
            #if self.toggleFPSdisplay : 
            #    self.canvas.create_text(self.width-50,50, text=str(self.currentFPS), fill="black", font=("Helvetica 20 bold"))
            
        return None
    
    def drawStats(self) :
        posX = self.width-100
        posY = 20
        incY = 20
        me = self.getMe()
        self.canvas.create_text(posX,posY+incY*0, text="FPS : "+str(self.currentFPS)+" (avg : "+str(self.currentFPSavg)+")", fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*1, text="Position pixel: ("+str(me.posMap[0])+","+str(me.posMap[1])+")", fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*2, text="Position tile : ("+str(int(me.posMap[0]/self.terrainTileSize))+","+str(int(me.posMap[1]/self.terrainTileSize))+")", fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*3, text="In shopping zone : "+str(self.isShoping), fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*4, text="Hand obj : "+str(len(self.handObjListClass)), fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*5, text="Static obj : "+str(len(self.objList)), fill="black", font=("Helvetica 10 bold"))
        self.canvas.create_text(posX,posY+incY*6, text="Car obj : "+str(len(self.carObjList)), fill="black", font=("Helvetica 10 bold"))
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
            if character.inCar == -1 :
                self.drawCharacterClass(characterSheetSettings,character,offset)
    
    def drawBackgroundSheet(self,backSettings,posX,posY) :
        if self.splitMapImage==[0,0] :
            back = backSettings[0]
            self.canvas.create_image(posX,posY, image=back[0], anchor="nw")    
        else :
            for i in range(1,len(backSettings)) :
                back = backSettings[i]  
                if self.packAllBack:
                    self.canvas.create_image(posX+back[8]*32,posY+back[9]*32, image=back[0], anchor="nw") 
                else :
                    if self.isBackgroundOnScreen(back) :
                        self.canvas.create_image(posX+back[8]*32,posY+back[9]*32, image=back[0], anchor="nw") 
                #print("x",back[8],"y",back[9])
                 
    
    def isBackgroundOnScreen(self,back) :
        minX = -self.offset[0]+back[8]*32
        minY = -self.offset[1]+back[9]*32
        maxX = minX+back[1]
        maxY = minY+back[2]
        border = 200
        if maxX<-border or maxY<-border or minX>self.width+border or minY>self.height+border :
            return False
        else :
            return True
        #self.canvas.create_image(50,50, image=backSettings[0][7], anchor="nw")
        
    def drawAnimationList(self) :
        for i in self.animationListPos :
            img = self.animationList[i[0]]
            self.canvas.create_image(i[1]-int(i[3]/2)-self.offset[0],i[2]-int(i[4]/2)-self.offset[1], image=img, anchor="nw")
   
    def moveCamera(self,keyDir,speed=15) :
        self.offset = [self.offset[0]+speed*keyDir[0],self.offset[1]+speed*keyDir[1]]
    
    ##############
    #Load texture#
    ##############
    
    def generateMapConfig(self,num) :
        return [["map"+str(num)+".png","map"+str(num)]],[["map"+str(num)+"_tex.jpeg",0,0,0,0,"map"+str(num)+"_col.png",0,0,0,0]]
   
    ###################
    #Create characters#
    ###################
    
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
    
    def createMeFull(self,myName,mySprite,myGender,myRandomName,mySpeed,myPosition,myHealth,myAttackRange,myDamageMulti) :
        character_me = ch.character(mySprite,myPosition,myRandomName,myName,myGender)
        character_me.playerControled = True
        character_me.speed = mySpeed
        character_me.posMap = myPosition
        character_me.healthPct = myHealth
        character_me.attackRange = myAttackRange
        character_me.damageMulti = myDamageMulti
        character_me.inCar = -1
        self.chara_list.append(character_me)
        self.centerCameraOn(character_me)
        #self.offset = [character_me.posMap[0]-int(self.width/2),character_me.posMap[1]-int(self.height/2)]
    
    def centerCameraOn(self,me) :
        self.offset = [me.posMap[0]-int(self.width/2),me.posMap[1]-int(self.height/2)]
    
    def getAllChList(self) :
        ch_list = []
        for i in range(100) :
            chara = ch.character(i,[i*30,50])
            chara.name = str(i)
            ch_list.append(chara)
        return ch_list
    

    def moveCharacterList(self,chList,collisionMat=None) :
        for c in chList :
            if c.inCar == -1 :
                if self.characterCanMove(c,collisionMat,True) and not c.dead:
                    c.move()
                if c.playerControled :
                    self.moveCameraPos(c)
            else :
                carPos = self.carObjList[c.inCar].pos
                posDiff = [carPos[0]-c.posMap[0],carPos[1]-c.posMap[1]]
                c.movingDir = posDiff
                c.move()
                self.moveCameraPos(c)
                #c.posMap = self.carObjList[c.inCar].pos
                
    def moveCameraPos(self,c):
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
                newcoo = [int((c.posMap[0] + c.movingDir[0]*2)/self.terrainTileSize),int((c.posMap[1] + c.movingDir[1]*2)/self.terrainTileSize)]
            else :
                newcoo = [int(c.posMap[0]/self.terrainTileSize),int(c.posMap[1]/self.terrainTileSize)]
            if not collisionMat[min(max(newcoo[1],0),colSizeY)][min(max(newcoo[0],0),colSizeX)] :# and not collisionMat[newcoo[1]+1][newcoo[0]+1] and not collisionMat[newcoo[1]+1][newcoo[0]] and not collisionMat[newcoo[1]][newcoo[0]+1] :
                return True
            else :
                return False
            
    def getHandObjFromInventory(self,i) :
        for obj in self.handObjListClass :
            if obj.itemInInventory :
                if obj.posInventory == i :
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
    
    def pasteConf(self,confVal,defaultVal) :
        if self.useConf :
            return confVal
        else :
            return defaultVal
    
    #Print
    def fpsHandeling(self,start,end,displayFPS,fpsList) : 
        fpsNum = 0
        if end!=start :
            fpsNum = float(1/float((float(end)-float(start))))
        else :
            fpsNum = 150
        fpsList.append(fpsNum)
        if self.frameCount%10==0 :
            self.currentFPS = int(fpsNum)
            if len(fpsList)>300 :
                self.currentFPSavg = round(sum(fpsList[-300:])/300,3)
        if self.listener.exitFlag :
            print("FPS => (avg:"+str(round(sum(fpsList)/len(fpsList),3))+") (min:"+str(round(min(fpsList),3))+") (max:"+str(round(max(fpsList),3))+")")
            print(" ==== PROGRAM STOP ====")
            self.listener.killListener()
            self.root.destroy()
            sys.exit(0)
            pass
        if displayFPS :
            printFPS(start,end)    
            
    def printRessources(self) :
        chList = get_size(self.chara_list)
        handObj = get_size(self.handObjListClass)
        objList = get_size(self.objList)
        sheetList = get_size(self.sheetList)
        bgList = get_size(self.backList)
        obBuilder = get_size(self.object)
        total = obBuilder + bgList + sheetList + objList + handObj + chList
        print("Character list size :",chList,"(len :",len(self.chara_list),")")
        print("Hand obj list size :",handObj,"(len :",len(self.handObjListClass),")")
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
    x = 100
    y = 100
    objList = []
    for i in range(87) :
        objList.append([i,int(x+((i%10)*45)),int(y+(int(i/10)*45)),-1])
    x = 100
    y = 700
    for i in range(32) :
        for j in range(4) :
            objList.append([((j+1)*100)+i,int(x+i*45),int(y+j*45),-1])
    return objList

def generateObjList() :
    x = 1
    y = 1
    objList = []
    for i in range(50) :
        objList.append([i,int(x+i),int(y)])
    x = 1
    y = 3
    for i in range(200) :
        objList.append([i+100,int(x+(i%15)*3),int(y+int(i/15)*3)])
    return objList
#sl = window(cf.configLoader())