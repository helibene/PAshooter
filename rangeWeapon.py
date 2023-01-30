# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:09:14 2023

@author: Alexandre
"""
from usefullHandObject import usefullHandObject

class rangeWeapon(usefullHandObject) :
    def __init__(self,index,spriteNum,damage,wepRange=500,speed=20,radius=50):
        super().__init__(index, spriteNum)
        self.damage = damage
        self.range = wepRange
        self.speed = speed
        self.radius = radius
        

def getAllList() :
    returnList = []
    for i in range(7) :
        returnList.append(instanceFromStats(selectStats(i)))
    return returnList
    
def init(val) :
    return instanceFromStats(selectStats(val))

def selectStats(index) :
    defaultRange = 1000
    defaultSpeed = 20
    defaultRadius = 30
    mapDict = {
            0: [8,0.05,defaultRange,defaultSpeed,defaultRadius],
            1: [40,0.2,defaultRange,defaultSpeed,defaultRadius],#Door
            2: [41,0.2,defaultRange,defaultSpeed,defaultRadius],
            3: [69,0.2,defaultRange,defaultSpeed,defaultRadius],
            4: [70,0.2,defaultRange,defaultSpeed,defaultRadius],
            5: [79,10,defaultRange,defaultSpeed,defaultRadius],#Prison Door
            6: [51,0.2,defaultRange,defaultSpeed,defaultRadius]
        }
    if index in mapDict :
        stats = mapDict[index]
        return [index,stats[0],stats[1],stats[2],stats[3],stats[4]]

def instanceFromStats(stats) :
    return rangeWeapon(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5])