# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:08:10 2023

@author: Alexandre
"""

class objectTemplate :
    
    defaultOffset0=[-11,-9]
    objList0 = [[113,11,9],[114,13,9],#Bed and bed table
                    [120,19,18],[121,21,18],[122,23,18],[126,18,14],[141,15,13],[118,11,13.5],#Closet
                    [117,15,9],
                    [125,11,16.5],[138,17.3,15],[137,19.2,15],#dining table and chairs
                    [17,14,14],
                    [2,24,14],[2,16,17],[1,13,18],#Doors
                    [25,17,20],
                    [155,23,8.5],[158,23,8.5],[156,23,8.5],#Washing
                    [151,23,15],[22,18,20],   
                    [127,13.5,19.5],[116,11,18.5],#Bathroom
                    [123,17,8.5],[128,21,8],[148,19,8.5],[132,22,11]]#Kitchen   #,[103,25,25],[103,15,30],[104,27,23],[104,32,32]]
    handObjList0 = [[108,22.5*32,12*32,-1],#Cabadge
                        [214,20*32,8.8*32,-1],#Eggs
                        [217,21.5*32,9*32,-1],#bakon
                        [6,19.5*32,19*32,-1],
                        [4,17.5*32,9*32,-1],
                        [82,18.7*32,16*32,-1]]
    defaultOffset1 = [0,0]
    objList1 = [[116,0,0],[127,2.5,1.5],#Bathroom
                [2,5,0],[3,6,-1],[2,7,8],[2,7,5],[3,6,13],#Doors
                [113,8,0],[114,9.5,0],#Bed
                [-118,11,2],[119,11,0],#Closet and drawer
                [108,1.5,4],[162,1,5],[19,2,7],#Sofa, table, TV
                #[126,18,0],
                [126,2,9],[138,1.3,10],[137,3.2,10],#dining table and chairs
                [123,8,11.5],[148,10,11.5],[130,12,9],[133,12,7]#Kitchen
                ]
    handObjList1 = []
    objList2 = [[1,2,-1],[3,3,-1],[2,6,2],[2,5,15],[2,5,22],[2,8,22],[2,13,20],#Doors
                [149,8,-0.5],[149,9.5,-0.5],[149,11,-0.5],[145,12.5,-0.5],[145,14,-0.5],#filer and cabinet
                [140,2,3],[15,2.5,4],
                [139,1.5,8],[14,2,7],[139,1.5+3.5*1,8],[14,2+3.5*1,7],[139,1.5+3.5*2,8],[14,2+3.5*2,7],[139,1.5+3.5*3,8],[14,2+3.5*3,7],[139,1.5+3.5*4,8],[14,2+3.5*4,7],[139,1.5+3.5*5,8],[14,2+3.5*5,7],
                [139,1.5,11],[14,2,10],[139,1.5+3.5*1,11],[14,2+3.5*1,10],[139,1.5+3.5*2,11],[14,2+3.5*2,10],[139,1.5+3.5*3,11],[14,2+3.5*3,10],[139,1.5+3.5*4,11],[14,2+3.5*4,10],[139,1.5+3.5*5,11],[14,2+3.5*5,10],             
                [123,9,18.5],[128,11,18],[148,9,23.5],[132,11,23],#Kitchen
                [144,1,15],[17,0,15.5],[144,1,21],[17,0,21.5],#2 offices
                [151,4,13],[147,4,16],[151,4,18],[147,4,19],#Cabinets
                [164,8,14],[135,9,13],[164,12,14],[135,13,13],[164,16,14],[135,17,13],[165,20.5,19],[138,20,20],#Computer
                [166,15,17],[167,15,21],#Machine
                [109,10,17],[170,21,15],[173,21,16.5]
                ]
    handObjList2 = []
    defaultOffset2 = [0,0]
    objList3 = [[1,4,-1],[-161,0,0.5],[-161,0,3],[-161,0,5.5],
                [176,6,1],[176,6,2.5],[176,6,4],[176,6,5.5],
                [179,7,7],[178,4,9],[177,2,0]]
    handObjList3 = []
    defaultOffset3 = [0,0]
    objList4 = [[7,4,-1],[7,4,1],[5,1,2],#Doors
                [102,0,0],[10,2,0],#Prison cell
                [109,5.5,9],[162,4.5,7],#relax area
                [165,6.5,3],[138,6,4],
                [-151,0,3],[-151,0,5],[-151,0,7],#cabinets
                [180,6,0],[186,6,0],[180,7,0],[189,7,0]]#[180,0,9],[183,0,9.3],
    handObjList4 = []
    defaultOffset4 = [0,0]
    def __init__(self,index,offset=[0,0]):
        self.index = index
        self.offset = offset
        self.objMat = [objectTemplate.objList0,objectTemplate.objList1,objectTemplate.objList2,objectTemplate.objList3,objectTemplate.objList4,objectTemplate.objList4]
        self.handObjMat = [objectTemplate.handObjList0,objectTemplate.handObjList1,objectTemplate.handObjList2,objectTemplate.handObjList3,objectTemplate.handObjList4,objectTemplate.handObjList4]
        self.defaultOffsetList = [objectTemplate.defaultOffset0,objectTemplate.defaultOffset1,objectTemplate.defaultOffset2,objectTemplate.defaultOffset3,objectTemplate.defaultOffset4]
        
    def getTemplateList(self) :
        if self.index>len(self.objMat)-1 or self.index>len(self.handObjMat)-1 :
            return None
        else :
            objList = self.objMat[self.index]
            handObjList = self.handObjMat[self.index]
            offset = [self.offset[0] + self.defaultOffsetList[self.index][0],self.offset[1] + self.defaultOffsetList[self.index][1]]
            objList,handObjList = self.applyOffsetToTemplate(objList,handObjList,offset)
            return objList,handObjList

    def applyOffsetToTemplate(self,objList,handObjList,offset,scale=32) :
        objListCopy = objList.copy()
        handObjListCopy = handObjList.copy()
        for i in range(len(objList)) :
            objListCopy[i][1] = objListCopy[i][1] + offset[0]
            objListCopy[i][2] = objListCopy[i][2] + offset[1]
        for i in range(len(handObjList)) :
            handObjListCopy[i][1] = handObjListCopy[i][1] + offset[0]*scale
            handObjListCopy[i][2] = handObjListCopy[i][2] + offset[1]*scale
        return objListCopy,handObjListCopy
        
    def deleteAllData(self) :
        del(self.objMat)
        del(self.handObjMat)
        del(self)
    