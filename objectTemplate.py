# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:08:10 2023

@author: Alexandre
"""

class objectTemplate :

    objList0 = [[113,11,9],[114,13,9],#Bed and table
                    [120,19,18],[121,21,18],[122,23,18],[126,18,14],[141,15,13],[118,11,13.5],[117,15,9],[125,11,16.5],[138,17.3,15],[137,19.2,15],[17,14,14],
                    [2,24,14],[2,16,17],[1,13,18],#Doors
                    [25,17,20],[155,23,8.5],[158,23,8.5],[156,23,8.5],[151,23,15],[22,18,20],   
                    [127,13.5,19.5],[116,11,18.5],#Bathroom
                    [123,17,8.5],[128,21,8],[148,19,8.5],[132,22,11]]#Kitchen   #,[103,25,25],[103,15,30],[104,27,23],[104,32,32]]
    handObjList0 = [[108,22.5*32,12*32,-1],#Cabadge
                        [214,20*32,8.8*32,-1],#Eggs
                        [217,21.5*32,9*32,-1],#bakon
                        [6,19.5*32,19*32,-1],
                        [4,17.5*32,9*32,-1],
                        [82,18.7*32,16*32,-1]]
    def __init__(self,index,offset=[0,0]):
        self.index = index
        self.offset = offset
        self.objMat = [objectTemplate.objList0]
        self.handObjMat = [objectTemplate.handObjList0]
        
    def getTemplateList(self) :
        if self.index>len(self.objMat)-1 or self.index>len(self.handObjMat)-1 :
            return None
        else :
            objList = self.objMat[self.index]
            handObjList = self.handObjMat[self.index]
            objList,handObjList = self.applyOffsetToTemplate(objList,handObjList)
            return objList,handObjList

    def applyOffsetToTemplate(self,objList,handObjList,scale=32) :
        for i in range(len(objList)) :
            objList[i][0] = objList[i][0] + self.offset[0]
            objList[i][1] = objList[i][1] + self.offset[1]
        for i in range(len(handObjList)) :
            handObjList[i][0] = handObjList[i][0] + self.offset[0]*scale
            handObjList[i][1] = handObjList[i][1] + self.offset[1]*scale
        return objList,handObjList
        
    def deleteAllData(self) :
        del(self.objMat)
        del(self.handObjMat)
        del(self)
    