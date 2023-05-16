# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:08:10 2023

@author: Alexandre
"""

import rangeWeapon as rw
import handObject as ho
import lootSelection as ls
import templateConf as tc    

class objectTemplate :
    
    def __init__(self,index,offset=[0,0]):
        self.tempConf = tc.templateConf()
        self.index = index
        self.offset = offset
            
    def applyOffsetToTemplate(self,objList,handObjList,shopAreaList,offset,scale=32) :
        objListCopy = objList.copy()
        handObjListCopy = handObjList.copy()
        shopAreaListCopy = shopAreaList.copy()
        for i in range(len(objListCopy)) :  
            objListCopy[i][1] = objListCopy[i][1] + offset[0]
            objListCopy[i][2] = objListCopy[i][2] + offset[1]
        for i in range(len(shopAreaListCopy)) :
            shopAreaListCopy[i][0][0] = (shopAreaListCopy[i][0][0] + offset[0])*scale
            shopAreaListCopy[i][1][0] = (shopAreaListCopy[i][1][0] + offset[0])*scale
            shopAreaListCopy[i][0][1] = (shopAreaListCopy[i][0][1] + offset[1])*scale
            shopAreaListCopy[i][1][1] = (shopAreaListCopy[i][1][1] + offset[1])*scale
        for i in range(len(handObjList)) :
            if type(handObjListCopy[i]) != type(ho.handObject()):
                handObjListCopy[i][1] = handObjListCopy[i][1] + offset[0]*scale
                handObjListCopy[i][2] = handObjListCopy[i][2] + offset[1]*scale
            else :
                handObjListCopy[i].pos[0] = handObjListCopy[i].pos[0] + offset[0]*scale
                handObjListCopy[i].pos[1] = handObjListCopy[i].pos[1] + offset[1]*scale
        return objListCopy,handObjListCopy,shopAreaListCopy
    

    def deleteAllData(self) :
        del(self.objMat)
        del(self.handObjMat)
        del(self)

    def templateListToObjList(self,masterTemplateNum) :
        objListBuff = []
        handObjListBuff = []
        shopAreaListBuff = []
        tempList = safeGetFromDict(masterTemplateNum,self.tempConf.masterTemplateDict,[])
        for temp in tempList :
            currentTemplate = safeGetFromDict(temp[0],self.tempConf.templateList,None)
            if currentTemplate!=None :
                defOffset = safeGetFromDict("defOffset",currentTemplate,[0,0])
                objList = safeGetFromDict("objList",currentTemplate,[])
                objListRot = safeGetFromDict("objListRot",currentTemplate,[])
                size = safeGetFromDict("size",currentTemplate,[0,0])
                shopAreaList = safeGetFromDict("shopArea",currentTemplate,[])
                handObjList = safeGetFromDict("handObjList",currentTemplate,[])
                offset = [self.offset[0] + defOffset[0]+temp[1][0],self.offset[1] + defOffset[1]+temp[1][1]]
                if objListRot != [] :
                    objList = extend([],objList)
                    objListDef = self.fromRotToStandardList(objListRot,temp[2])
                    objList = extend(objList,objListDef)
                    objList = self.objListRot(objList,temp[2],size)
                    
                objList,handObjList,shopAreaList = self.applyOffsetToTemplate(objList,handObjList,shopAreaList,offset)
                objListBuff = extend(objListBuff,objList)
                handObjListBuff.extend(handObjList)
                shopAreaListBuff.extend(shopAreaList)
        return objListBuff,handObjListBuff,shopAreaListBuff

    def objListRot(self,objList,angle=0,size=[0,0]) :
        for obj in objList :
            if angle == 2 or angle == 3:
                obj = self.mirrorStraigtAxis(obj,size,angle)
            if angle == 1 or angle == 3:
                obj = self.mirrorObjY(obj,size,angle)
                obj = self.mirrorObjXY(obj,size)
        return objList
    
    def mirrorStraigtAxis(self,obj,size,angle):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        x = -(obj[1]-(size[0]/2))+(size[0]/2)
        y = -(obj[2]-(size[1]/2))+(size[1]/2)
        if angle!=3 :
            if sizeobj[0]>1 :
                x = x - (sizeobj[0]-1)
            if sizeobj[1]>1 :
                y = y - (sizeobj[1]-1)
        obj[1] = x
        obj[2] = y
        return obj
    
    
    def mirrorObjY(self,obj,size,angle):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        y = -(obj[2]-size[1]/2)+(size[1]/2)
        x = obj[1]
        if angle!=3 :
            if sizeobj[0]>1:
                y = y - (sizeobj[0]-1)
        else :
            if sizeobj[1]>1:
                x = x - (sizeobj[1]-1)
        obj[2] = y
        obj[1] = x
        return obj
    
    def mirrorObjXY(self,obj,size):
        x = obj[1]
        y = obj[2]
        obj[1] = y
        obj[2] = x
        return obj
    
    def getObjSettingFromID(self,key=None) :
        if type(key)==type(10) :
            idnum=key
            if idnum in self.tempConf.objRotMapping :
                return self.tempConf.objRotMapping[idnum]
            else :
                return None
        elif type(key)==type("10") :
            sel = 0
            for val in self.tempConf.objRotMapping :
                if self.tempConf.objRotMapping[val]["name"] == key :
                    sel = val
                
            return self.tempConf.objRotMapping[sel]
        else :
            return None
    
    def angleAdd(self,baseAngle,delta) :
        return (baseAngle+delta)%4
    
    def fromRotToStandardList(self,rotList,angle=0) :
        objList = []
        for item in rotList :
            objOff = [None]*4
            noRot = False
            difColorOffset=0
            angleFromItem = 0
            itemId = item[0]
            colorNum = 0
            if len(item)>3 :
                angleFromItem = item[3]
            if len(item)>4 :
                colorNum = item[4]
            angleNum = self.angleAdd(angleFromItem,angle)
            objSize = self.getObjSettingFromID(itemId)["size"]
            if "offset" in self.getObjSettingFromID(itemId) :
                objOff = self.getObjSettingFromID(itemId)["offset"]
            if "noRot" in self.getObjSettingFromID(itemId) :
                noRot = self.getObjSettingFromID(itemId)["noRot"]
            if "difColorOffset" in self.getObjSettingFromID(item[0]) :
                difColorOffset = self.getObjSettingFromID(item[0])["difColorOffset"]
            posX = item[1]
            posY = item[2]
            if objOff != None :
                if objOff[angleNum] != None :
                    posX = posX + objOff[angleNum][0]
                    posY = posY + objOff[angleNum][1]
            if noRot :
                angleNum = 0
            else :
                if angleNum==1 or angleNum==3 :
                    objSize = [objSize[1],objSize[0]]
            spriteNum = self.getObjSettingFromID(item[0])["idList"][angleNum]
            if colorNum!=0 and difColorOffset!=0 :
                if spriteNum>0 :
                    spriteNum = spriteNum + difColorOffset*colorNum
                else :
                    spriteNum = spriteNum - difColorOffset*colorNum
            objList.append(list([spriteNum,posX,posY,objSize]))
        return objList
    
def extend(list1,list2) :
    for ele in list2 :
        list1.append(list(ele))
    return list1

def safeGetFromDict(key,dictonary,defReturn=None) :
    if key in dictonary :
        return dictonary[key]
    else :
        return defReturn

