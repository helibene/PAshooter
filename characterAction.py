# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 01:08:32 2023

@author: Alexandre
"""
import math

class characterAction :
    def __init__(self):
        pass


def master(w) :
    keyMouseAction(w)
    
    
def keyMouseAction(w) :
    keyDir,interact,drop,sprint = w.listener.keyAction()
    me = w.getMe()
    keyDir = applySprint(w,sprint,keyDir)
    changeDirCharacterList(w,keyDir,me)
    changeDirCarList(w,me,keyDir)
    meleWepon = weponUseAtempt(w,me)
    damageCalculation(w,me,meleWepon)
    healUseAtempt(w,me)
    interactAction(w,interact,drop,me)
    w.healthPct = me.healthPct
    w.listener.resetClick()


def changeDirCarList(w,me=None,direction=[0,0],accMulti=0.02) :
    for i in range(len(w.carObjList)) :
        if me!=None  :
            if me.inCar == i and direction != [0,0] :
                w.carObjList[i].setAcceleration([direction[0]*accMulti,direction[1]*accMulti])
            else :
                w.carObjList[i].setAcceleration([0,0])
                
def changeDirCharacterList(w,direction=[0,0],me=None) :
    for c in w.chara_list :
        if c.playerControled :
            if w.keyMovePlayer :
                c.changeDir(direction)
        else :
            if c.movingPattern == 0 :
                c.movingDir = [0,0]
            elif c.movingPattern == 1 :
                c.changeDirRand(w.changeDirectionFrequency,w.stopMovingFrequency)
            elif c.movingPattern == 2 :
                c.folowPlayer(me,me.dead)
            elif c.movingPattern == 3 :
                c.folowPlayer(me,me.dead,w.characterVision,w.changeDirectionFrequency,w.stopMovingFrequency)

########
#Pickup#
########

def pickUpItem(w,me,interBool) :
    takenFlag = False
    if w.pickupCooldown == 0 :
        if w.inventoryCount<w.maxInventory+1 and interBool : 
            for obj in w.handObjList :
                if not takenFlag and obj[0]!=1 and obj[3]!=-4 and obj[3]!=-5:
                    dist = math.sqrt(math.pow(obj[1]-me.posMap[0],2)+math.pow(obj[2]-me.posMap[1],2))
                    if dist < w.distancePickup :
                        print("Picked up obj #",obj[0])
                        obj[1] = -100
                        obj[2] = -100
                        if obj[0]==31 :
                            obj[3] = -5
                            w.moneyCount = w.moneyCount + obj[6]
                        else :
                            avaSpot = w.inventoryAvailableSpot()
                            obj[3] = avaSpot
                            if avaSpot==len(w.inventoryList):
                                w.inventoryList.append(w.handObjList.index(obj))
                            else :
                                w.inventoryList[avaSpot] = w.handObjList.index(obj)
                            w.inventoryCount = w.inventoryCount + 1
                        takenFlag = True
                        w.pickupCooldown = 20
    else :
        w.pickupCooldown = w.pickupCooldown - 1
        
        
def applySprint(w,sprintBool,keyDir) :
    if sprintBool :
        keyDir = [keyDir[0]*w.sprintFactor,keyDir[1]*w.sprintFactor]
    return keyDir

def healUseAtempt(w,me) :
    if w.listener.mouseVal[0]!=-1 :
        obj = w.getHandObjFromInventory(w.menuBarSel)
        if obj != None :
            healItem = w.getUOfromSpriteNum(obj[0],w.medList)
            if healItem != None :
                me.healthPct = min(me.healthPct + healItem.healValue,1)
                dropItem(w,obj,me,True)
    
def dropAction(w,dropBool,me) :
    if dropBool and w.dropCooldown==0:
        obj = w.getHandObjFromInventory(w.menuBarSel)
        dropItem(w,obj,me)
    elif w.dropCooldown>0 :
        w.dropCooldown = w.dropCooldown - 1

def dropItem(w,item,me,delete=False) :
    if item!=None :
        if delete :
            item[3] = -4
        else :
            item[3] = -1
        item[1] = me.posMap[0]
        item[2] = me.posMap[1]
        dropIndex = w.inventoryList.index(w.handObjList.index(item))
        w.inventoryList[dropIndex] = -1
        w.inventoryCount = w.inventoryCount - 1
        w.dropCooldown = 10

def interactAction(w,interBool,dropBool,me) :
    dropAction(w,dropBool,me)
    pickUpItem(w,me,interBool)
    interactCar(w,me,interBool)
    interactWithItem(w,me,interBool)

def interactCar(w,me,interBool) :
    if me.carInteractionCooldown == 0 :
        if interBool :
            for i in range(len(w.carObjList)) :
                dist = math.sqrt(math.pow(w.carObjList[i].pos[0]-me.posMap[0],2)+math.pow(w.carObjList[i].pos[1]-me.posMap[1],2))
                if dist<100 :
                    me.carInteractionCooldown = 50
                    if me.inCar==-1 :
                        me.inCar = i
                    elif me.inCar==i:
                        me.inCar = -1
    else :
        me.carInteractionCooldown = me.carInteractionCooldown -1
                
def interactWithItem(w,me,interBool):
    aniIter = 25
    distance = 60
    for obj in w.objList : 
        if obj[3][0]!='none' :
            if obj[3][0]=='door' :
                if obj[3][3] == 0 :
                    #print(#w.backList[0][5][int(obj[1])][int(obj[2])],"  ",obj[1],"  ",obj[2])
                    w.backList[0][5][int(obj[3][6])][int(obj[3][5])]=True
                else :
                    w.backList[0][5][int(obj[3][6])][int(obj[3][5])]=False
                if obj[3][4] :
                    if interBool:
                        dist = math.sqrt(math.pow(obj[1]*32-me.getPosMapCenter()[0],2)+math.pow(obj[2]*32-me.getPosMapCenter()[1],2))
                        if dist < distance :
                            if obj[3][2] == 0 :
                                #print(#obj[3][3],dist)
                                if obj[3][3] == 0 :
                                    obj[3][2] = 1
                                if obj[3][3] == aniIter:
                                    obj[3][2] = -1
    
                            
                    obj[1] = obj[1]+obj[3][1][0]*obj[3][2]/aniIter
                    obj[2] = obj[2]+obj[3][1][1]*obj[3][2]/aniIter
                    obj[3][3] = obj[3][3] + obj[3][2] 
                    if aniIter<=obj[3][3] and obj[3][2] == 1:
                        obj[3][2] = 0
                        obj[3][3] = aniIter
                    if obj[3][3] <= 0 and obj[3][2] == -1:
                        obj[3][3] = 0
                        obj[3][2] = 0
            if obj[3][0]=='cabinet' :
                if obj[3][3] :
                    if interBool:
                        dist = math.sqrt(math.pow(obj[1]*32-me.getPosMapCenter()[0],2)+math.pow(obj[2]*32-me.getPosMapCenter()[1],2))
                        if dist < distance and obj[3][4]==0:
                            obj[3][4] = aniIter
                            if obj[3][1] :
                                obj[3][1] = False
                            else :
                                obj[3][1] = True
                            spriteNum = obj[0]
                            obj[0] = obj[3][2]
                            obj[3][2] = spriteNum
                if obj[3][4]>0 :
                    obj[3][4] = obj[3][4] -1
                    
        
def damageCalculation(w,me,meleWepon):
    moveBullets(w,me)
    meleDamageCalculation(w,me,meleWepon)

def meleDamageCalculation(w,me,meleWepon) :
    if w.weponUsedCooldown == w.weponUsedCooldownReset and meleWepon!=None:
        for cha in w.chara_list :
            dist = math.sqrt(math.pow(cha.getPosMapCenter()[0]-me.getPosMapCenter()[0],2)+math.pow(cha.getPosMapCenter()[1]-me.getPosMapCenter()[1],2))
            if not cha.playerControled and dist<(me.attackRange*meleWepon.rangeMulti) :
                dead = cha.applyDamage(meleWepon.damage,me.damageMulti)
                if dead :
                    killCharacter(w,cha)
    for cha in w.chara_list :
        if not cha.dead and not cha.playerControled and cha.attackCooldown==0 :
            dist = math.sqrt(math.pow(cha.getPosMapCenter()[0]-me.getPosMapCenter()[0],2)+math.pow(cha.getPosMapCenter()[1]-me.getPosMapCenter()[1],2))
            if dist<cha.attackRange :
                cha.attackCooldown = 10
                dead = me.applyDamage(1,cha.damageMulti)
                if dead :
                    killCharacter(w,me)
        elif not cha.dead and not cha.playerControled and cha.attackCooldown!=0 :
            cha.attackCooldown = cha.attackCooldown -1
        if cha.damageCooldown>0 :
            cha.damageCooldown = cha.damageCooldown -1

def killCharacter(w,cha) :
    cha.dead = True
    w.animationListPos.append([0,cha.posMap[0],cha.posMap[1],cha.spriteSize[0],cha.spriteSize[1]])
    lootList = cha.lootList
    for lootIndex in lootList :
        print(lootIndex)
        w.handObjList[lootIndex][3] = -1
        w.handObjList[lootIndex][1] = cha.posMap[0]
        w.handObjList[lootIndex][2] = cha.posMap[1]
                
def moveBullets(w,me) :
    if w.bulletNum>0 :
        for i in range(w.bulletNum) :
            if w.handObjList[i][3] == -2 :
                w.handObjList[i][1] = me.posMap[0] 
                w.handObjList[i][2] = me.posMap[1]

            if w.handObjList[i][3] == -3 :
                w.handObjList[i][1] = w.handObjList[i][1]+w.handObjList[i][5][0]
                w.handObjList[i][2] = w.handObjList[i][2]+w.handObjList[i][5][1]
                w.handObjList[i][7] = w.handObjList[i][7] + w.handObjList[i][6].speed 
                if w.objOutOfScreen(w.handObjList[i]) or w.handObjList[i][7]>w.handObjList[i][6].range:
                    w.handObjList[i][3]=-2
                    w.handObjList[i][7] = 0
                else :  
                    for cha in w.chara_list :
                        dist = math.sqrt(math.pow(cha.posMap[0]-w.handObjList[i][1],2)+math.pow(cha.posMap[1]-w.handObjList[i][2],2))
                        if not cha.playerControled and dist<w.handObjList[i][6].radius :
                            w.handObjList[i][3]=-2
                            dead = cha.applyDamage(w.handObjList[i][6].damage,me.damageMulti)
                            if dead :
                                killCharacter(w,cha)

def weponUseAtempt(w,me):
    weponUsedFlag = False
    meleWeponReturn=None
    if w.listener.mouseVal[0]!=-1 :
        obj = w.getHandObjFromInventory(w.menuBarSel)
        if obj != None :
            rangeWeapon = w.getUOfromSpriteNum(obj[0],w.rwList)
            if rangeWeapon!=None :
                speed = rangeWeapon.speed

                bulletDir = [0,0]
                bulletDir[0] = w.listener.mouseVal[0]-(me.getPosScreen(w.offset)[0])
                bulletDir[1] = w.listener.mouseVal[1]-(me.getPosScreen(w.offset)[1])
                distance = math.sqrt(math.pow(bulletDir[0],2)+math.pow(bulletDir[1],2))

                w.handObjList[w.activeBullet][3] = -3
                dir2 = [speed*bulletDir[0]/distance,speed*bulletDir[1]/distance]
                w.handObjList[w.activeBullet][5] = dir2
                w.handObjList[w.activeBullet][6] = rangeWeapon
                w.activeBullet = w.activeBullet + 1
                if w.activeBullet==w.bulletNum :
                    w.activeBullet = 0
                weponUsedFlag = True
            else :
                meleWeapon = w.getUOfromSpriteNum(obj[0],w.mwList)
                if meleWeapon!=None :
                    weponUsedFlag = True
                    meleWeponReturn = meleWeapon
                
    if weponUsedFlag :
        w.weponUsedCooldown = w.weponUsedCooldownReset
    else :
        if w.weponUsedCooldown>0 :
            w.weponUsedCooldown = w.weponUsedCooldown -1
    
    return meleWeponReturn
