# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:29:13 2023

@author: Alexandre
"""

import meleWeapon as mw
import rangeWeapon as rw
import medicine as med
import random
import handObject as ho
class lootSelection :
    
    template1 = {"rangew":0.5,"melew":0.5}

    def __init__(self):
        self.rwList = rw.getAllList()
        self.mwList = mw.getAllList()
        self.medList = med.getAllList()
        self.template1 = {"rangew":0.5,"melew":0.5}
        self.template2 = {"rangew":0.1,"melew":0.1,"money":0.6,"other":0.2}
        self.unusedHandObj = [0,1,32,47,64,65,73,75,31]
        #self.characterIndex
        pass
    
    def getItemFromTemplate(self,template=None) :
        template=self.template2
        randVal = random.random()
        selectValue = 0
        item = None
        for dictKey in template :
            selectValue = selectValue + template[dictKey]
            if randVal<selectValue :
                if dictKey == "rangew" :
                    item = self.getRandomRW()
                    item = ho.handObject().initRangeWeapon(item)
                elif dictKey == "melew" :
                    item = self.getRandomMW()
                    item = ho.handObject().initMeleWeapon(item)
                elif dictKey == "med" :
                    item = self.getRandomMED()
                    item = ho.handObject().initMedicine(item)
                elif dictKey == "money" :
                     item = ho.handObject().initMoneyBag()
                elif dictKey == "other" :
                    item = self.getRandomUseless()#ho.handObject(random.random()*87)
            if item != None :
                #item.itemType = "mobDrop"
                item.canPickup = False
                item.doNotDisplayOnMap = True
                return item
        item = self.getRandomUseless()
        item.doNotDisplayOnMap = True
        return None
    def getRandomRW(self) :
        indexList = int(random.random()*len(self.rwList))
        rangeWeapon = rw.init(indexList)
        return rangeWeapon
    
    def getRandomMW(self) :
        indexList = int(random.random()*len(self.mwList))
        meleWeapon = mw.init(indexList)
        return meleWeapon
    
    def getRandomMED(self) :
        indexList = int(random.random()*len(self.medList))
        medicine = med.init(indexList)
        return medicine
    
    def getUsefullSpriteNum(self):
        usefullItemSprite = []
        for rwep in self.rwList :
            usefullItemSprite.append(rwep.spriteNum)
        for mwep in self.mwList :
            usefullItemSprite.append(mwep.spriteNum)
        for medic in self.medList :
            usefullItemSprite.append(medic.spriteNum)
        return usefullItemSprite
    
    def getUselessItemSprite(self) :
        uselessList = []
        usefullAndUnusedList = self.getUsefullSpriteNum()
        usefullAndUnusedList.extend(self.unusedHandObj)
        for i in range(87) :
            if i not in usefullAndUnusedList :
                uselessList.append(i)
        return uselessList
    
    def getRandomUseless(self) :
        uselessList = self.getUselessItemSprite()
        randVal = int(random.random()*len(uselessList))
        return ho.handObject(uselessList[randVal])
