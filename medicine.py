# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:14:41 2023

@author: Alexandre
"""
from usefullHandObject import usefullHandObject

class medicine(usefullHandObject) :
    def __init__(self,index,spriteNum,healValue):
        super().__init__(index, spriteNum)
        self.healValue = healValue

def getAllList() :
    returnList = []
    for i in range(18) :
        returnList.append(instanceFromStats(selectStats(i)))
    return returnList

def init(val) :
    return instanceFromStats(selectStats(val))

def selectStats(index) :
    medVal = 0.3
    foodVal = 0.1
    mapDict = {
        0: [2,medVal],
        1: [3,medVal],
        2: [25,medVal],
        3: [26,medVal],
        4: [39,medVal],
        5: [57,medVal],
        6: [59,medVal],
        7: [84,medVal],
        8: [108,foodVal],
        9: [110,foodVal],
        10: [112,foodVal],
        11: [114,foodVal],
        12: [115,foodVal],
        13: [116,foodVal],
        14: [117,foodVal],
        15: [118,foodVal],
        16: [128,foodVal],
        17: [129,foodVal],
        }

    if index in mapDict :
        stats = mapDict[index]
        return [index,stats[0],stats[1]]
    
def instanceFromStats(stats) :
    return medicine(stats[0],stats[1],stats[2])