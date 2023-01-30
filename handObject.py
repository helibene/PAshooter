# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:45:40 2023

@author: Alexandre
"""

class handObject() :
    def __init__(self,spriteNum=0,pos=[0,0],itemInInventory=False,posInventory=-1,itemType="default",moneyValue=0,usefullItemInstance=None,distanceTraveled=0,moveVector=[0,0],bulletShot=False,doNotDisplayOnMap=False):
        self.spriteNum = spriteNum
        self.pos = pos
        self.itemInInventory = itemInInventory
        self.posInventory = posInventory
        self.itemType = itemType #"default" "bullet" "rangeWeapon" "meleWeapon" "medicine" "mobDrop" "money" "discarded"
        self.moneyValue = moneyValue
        self.usefullItemInstance = usefullItemInstance
        self.distanceTraveled = distanceTraveled
        self.moveVector = moveVector
        self.bulletShot = bulletShot
        self.doNotDisplayOnMap = doNotDisplayOnMap
        self.spriteList = []
        self.bulletRangeWeaponInstance = None
        
    def initBullet(self):
        self.spriteNum = 1
        self.itemType = "bullet"
        self.doNotDisplayOnMap = True
        return self
        
    def initRangeWeapon(self,weapon) :
        self.initUsefullObj(weapon,"rangeWeapon")
        return self
    
    def initMeleWeapon(self,weapon) :
        self.initUsefullObj(weapon,"meleWeapon")
        return self
        
    def initMedicine(self,medicine) :
        self.initUsefullObj(medicine,"medicine")
        return self
        
    def initUsefullObj(self,item,itemType) :
        self.itemType = itemType
        self.usefullItemInstance = item
        self.spriteNum = item.spriteNum
        
    def initMoneyBag(self,moneyVal=1):
        self.moneyValue = moneyVal
        self.spriteNum = 31
        self.itemType = "money"
        return self
        
    def putInInventory(self,posInv=0) :
        self.itemInInventory = True
        self.posInventory = posInv
        self.doNotDisplayOnMap = True
        self.pos = [0,0]
        
    def dropFromInventory(self,mapPos=[0,0]) :
        self.itemInInventory = False
        self.posInventory = -1
        self.doNotDisplayOnMap = False
        self.pos = mapPos
        
    def discard(self) :
        self.itemType = "discarded"
        self.doNotDisplayOnMap = True
        self.pos = [0,0]
        self.itemInInventory = False
        self.posInventory = -1
        self.usefullItemInstance = None
        self.deleteSprites()
        
    def deleteSprites(self) :
        del(self.spriteList)
        
    def display(self,num=-1,alinea=False) :
        spaceList = 0
        if alinea :
            spaceList = 4
        if num!=-1 :
            print("Displaying hand object #"+str(num))
        print(" "*spaceList,"Sprite number :",self.spriteNum)
        print(" "*spaceList,"Position on map :",self.pos)
        print(" "*spaceList,"Item type :",self.itemType)
        
def getBasicInstance(settingsList) :
    if settingsList[3]==-1 :
        return handObject(settingsList[0],[settingsList[1],settingsList[2]])
    else :
        return handObject().initBullet()
    return handObject()

def getBasicInstanceList(settingsMat) :
    returnMat = []
    handObjType = type(handObject())
    for setList in settingsMat :
        if type(setList)!=handObjType :
            returnMat.append(getBasicInstance(setList))
        else :
            returnMat.append(setList)
    return returnMat

def displayItemList(itemList,alinea=False) :
    for i in range(len(itemList)) :
        if itemList[i]!=None :
            itemList[i].display(i,alinea)
        else :
            print("Instance is None")