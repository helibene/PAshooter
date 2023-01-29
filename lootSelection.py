# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:29:13 2023

@author: Alexandre
"""

import meleWeapon as mw
import rangeWeapon as rw
import medicine as med
import random
class lootSelection :
    
    template1 = {"rangew":0.5,"melew":0.5}

    def __init__(self):
        self.rwList = rw.getAllList()
        self.mwList = mw.getAllList()
        self.medList = med.getAllList()
        self.template1 = {"rangew":0.5,"melew":0.5}
        pass
    
    def getItemFromTemplate(self,template) :
        template=self.template1
        randVal = random.random()
        selectValue = 0
        for dictKey in template :
            selectValue = selectValue + template[dictKey]
            if randVal<selectValue :
                if dictKey == "rangew" :
                    return self.getRandomRW()
                elif dictKey == "melew" :
                    return self.getRandomMW()
                elif dictKey == "med" :
                    return self.getRandomMED()
                else :
                    return int(random.random()*87)
    def getRandomRW(self) :
        indexList = int(random.random()*len(self.rwList))
        rangeWeapon = rw.selectStats(indexList)
        return rangeWeapon[1]
    
    def getRandomMW(self) :
        indexList = int(random.random()*len(self.mwList))
        meleWeapon = mw.selectStats(indexList)
        return meleWeapon[1]
    
    def getRandomMED(self) :
        indexList = int(random.random()*len(self.medList))
        medicine = med.selectStats(indexList)
        return medicine[1]
    
    
