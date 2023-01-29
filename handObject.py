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
        
    def initBullet(self):
        self.spriteNum = 1
        self.itemType = "bullet"
        
    def initRangeWeapon(self,weapon) :
        self.initUsefullObj(weapon,"rangeWeapon")
    
    def initMeleWeapon(self,weapon) :
        self.initUsefullObj(weapon,"meleWeapon")
        
    def initMedicine(self,medicine) :
        self.initUsefullObj(medicine,"medicine")
        
    def initUsefullObj(self,item,itemType) :
        self.itemType = itemType
        self.usefullItemInstance = item
        
    def initMoneyBag(self,moneyVal):
        self.moneyValue = moneyVal
        self.spriteNum = 31
        self.itemType = "money"
        
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