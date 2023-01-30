# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:14:20 2023

@author: Alexandre
"""
from usefullHandObject import usefullHandObject

class meleWeapon(usefullHandObject) :
    def __init__(self,index,spriteNum,damage,rangeMulti):
        super().__init__(index, spriteNum)
        self.damage = damage
        self.rangeMulti = rangeMulti
        
def getAllList() :
    returnList = []
    for i in range(18) :
        returnList.append(instanceFromStats(selectStats(i)))
    return returnList

def init(val) :
    return instanceFromStats(selectStats(val))

def selectStats(index) :
    defaultDamage = 0.1
    defaultRange = 0.1
    mapDict = {#[5,7,19,16,22,27,35,33,43,44,45,46,48,63,50,54,66,68,76,74]
            0: [5,0.2,1],
            1: [7,0.05,10],#Door
            2: [19,0.5,1],
            3: [16,defaultDamage,defaultRange],
            4: [22,defaultDamage,defaultRange],
            5: [27,defaultDamage,defaultRange],
            6: [35,defaultDamage,defaultRange],
            7: [33,defaultDamage,defaultRange],
            8: [43,defaultDamage,defaultRange],
            9: [46,defaultDamage,defaultRange],
            10: [48,defaultDamage,defaultRange],
            11: [63,defaultDamage,defaultRange],
            12: [50,defaultDamage,defaultRange],
            13: [54,defaultDamage,defaultRange],
            14: [66,defaultDamage,defaultRange],
            15: [76,defaultDamage,defaultRange],
            16: [74,defaultDamage,defaultRange],
            17: [68,defaultDamage,defaultRange],
        }
    if index in mapDict :
        stats = mapDict[index]
        return [index,stats[0],stats[1],stats[2]]
    
def instanceFromStats(stats) :
    return meleWeapon(stats[0],stats[1],stats[2],stats[3])