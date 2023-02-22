# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 00:08:10 2023

@author: Alexandre
"""

import rangeWeapon as rw
import handObject as ho
import lootSelection as ls


def getHandObject(spriteNum=0,pos=[0,0],invisible=False) :
    if spriteNum == -1 :
        lootSelect = ls.lootSelection()
        item = lootSelect.getRandomUseless()
        item.pos = pos
    else :
        item = ho.handObject(spriteNum,pos)
    if invisible :
        item.doNotDisplayOnMap = True
    return item

def extendList(list1,list2) :
    list1.extend(list2)
    return list1

def getListObj(spriteNum=0,pos=[0,0],posEnd=[2,2],stepX=1,stepY=1) :
    posX = pos[0]
    posY = pos[1]
    return_list = []
    while posY<posEnd[1] :
        while posX<posEnd[0] :
            return_list.append([spriteNum,posX,posY])
            posX = posX + stepX
        posX = pos[0]
        posY = posY + stepY
    return return_list

def getHandObjList(spriteNum=0,pos=[0,0],posEnd=[2,2],stepX=1,stepY=1) :
    posX = pos[0]
    posY = pos[1]
    return_list = []
    while posY<posEnd[1] :
        while posX<posEnd[0] :
            return_list.append(getHandObject(spriteNum,[posX,posY]))
            posX = posX + stepX
        posX = pos[0]
        posY = posY + stepY
    return return_list
    

class objectTemplate :
    
    masterTemplate1 = [[0,[3,3]],[1,[20,3]],[2,[18,24]],[3,[3,27]],[4,[3,41]],[5,[27,54]],[6,[44,36]],[7,[3,56]],[8,[59,36]],[9,[60,53]],[10,[37,55]],[11,[72,38]]]
    masterTemplate2 = [[0,[119,164]],[1,[119,190]],[2,[149,161]],[3,[103,193]],[4,[87,187]]]
    masterTemplate3 = [[50,[2,2],0],[50,[2,27],1],[50,[2,52],2],[50,[2,77],3],
                       [51,[27,2],0],[51,[27,27],1],[51,[27,52],2],[51,[27,77],3],
                       [52,[52,2],0],[52,[52,27],1],[52,[52,52],2],[52,[52,77],3],
                       [53,[76,1],0],[53,[76,26],1],[53,[76,51],2],[53,[76,76],3]]#,[12,[3,28]]
    
    def __init__(self,index,offset=[0,0]):

        self.templateList = {
            0 : {
	            "name": "defa",
	            "defOffset": [-11,-9],
	            "objList": [[113,11,9],[114,13,9],#Bed and bed table
                    [120,19,18],[121,21,18],[122,23,18],[126,18,14],[141,15,13],[118,11,13.5],#Closet
                    [117,15,9],
                    [125,11,16.5],[138,17.3,15],[137,19.2,15],#dining table and chairs
                    [17,14,14],
                    [2,24,14],[2,16,17],[1,13,18],#Doors
                    [25,17,20],
                    [155,23,8.5],[158,23,8.5],[156,23,8.5],#Washing
                    [151,23,15],[22,18,20],   
                    [127,13.5,19.5],[116,11,18.5],#Bathroom
                    [123,17,8.5],[128,21,8],[148,19,8.5],[132,22,11]],#Kitchen],
	            "handObjList":[getHandObject(108,[22.5*32,12*32]),#Cabadge
                        getHandObject(214,[20*32,8.8*32]),#Eggs
                        getHandObject(217,[21.5*32,9*32]),#bakon
                        getHandObject(6,[19.5*32,19*32]),
                        getHandObject(4,[17.5*32,9*32]),
                        getHandObject(82,[18.7*32,16*32]),
                        getHandObject(0,[23.5*32,16*32],True).initRangeWeapon(rw.init(2))],
	            "shopArea":[]
            },
			1 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[116,0,0],[127,2.5,1.5],#Bathroom
                [2,5,0],[3,6,-1],[2,7,8],[2,7,5],[3,6,13],#Doors
                [113,8,0],[114,9.5,0],#Bed
                [-118,11,2],[119,11,0],#Closet and drawer
                [108,1.5,4],[162,1,5],[19,2,7],#Sofa, table, TV
                [126,2,9],[138,1.3,10],[137,3.2,10],#dining table and chairs
                [123,8,11.5],[148,10,11.5],[130,12,9],[133,12,7],[-141,20,20]],
	            "handObjList":[getHandObject(316,[12.5*32,9*32]),#Stew
                    getHandObject(107,[8.9*32,1*32]),#Cloth
                    getHandObject(213,[12*32,5*32])],
	            "shopArea":[]
            },
			2 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[1,2,-1],[3,3,-1],[2,6,2],[2,5,15],[2,5,22],[2,8,22],[2,13,20],#Doors
                [149,8,-0.5],[149,9.5,-0.5],[149,11,-0.5],[145,12.5,-0.5],[145,14,-0.5],#filer and cabinet
                [140,2,3],[15,2.5,4],
                [139,1.5,8],[14,2,7],[139,1.5+3.5*1,8],[14,2+3.5*1,7],[139,1.5+3.5*2,8],[14,2+3.5*2,7],[139,1.5+3.5*3,8],[14,2+3.5*3,7],[139,1.5+3.5*4,8],[14,2+3.5*4,7],[139,1.5+3.5*5,8],[14,2+3.5*5,7],
                [139,1.5,11],[14,2,10],[139,1.5+3.5*1,11],[14,2+3.5*1,10],[139,1.5+3.5*2,11],[14,2+3.5*2,10],[139,1.5+3.5*3,11],[14,2+3.5*3,10],[139,1.5+3.5*4,11],[14,2+3.5*4,10],[139,1.5+3.5*5,11],[14,2+3.5*5,10],             
                [123,9,18.5],[128,11,18],[148,9,23.5],[132,11,23],#Kitchen
                [144,1,15],[17,0,15.5],[144,1,21],[17,0,21.5],#2 offices
                [151,4,13],[147,4,16],[151,4,18],[147,4,19],#Cabinets
                [164,8,14],[135,9,13],[164,12,14],[135,13,13],[164,16,14],[135,17,13],[165,20.5,19],[138,20,20],#Computer
                [166,15,17],[167,15,21],#Machine
                [109,10,17],[170,21,15],[173,21,16.5]],
	            "handObjList":[],
	            "shopArea":[]
            },
			3 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[1,4,-1],[-161,0,0.5],[-161,0,3],[-161,0,5.5],
                [176,6,1],[176,6,2.5],[176,6,4],[176,6,5.5],
                [179,7,7],[178,4,9],[177,2,0]],
	            "handObjList":[],
	            "shopArea":[]
            },
			4 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[7,4,-1],[7,4,1],[5,1,2],#Doors
                [102,0,0],[10,2,0],#Prison cell
                [109,5.5,9],[162,4.5,7],#relax area
                [165,6.5,3],[138,6,4],
                [-151,0,3],[-151,0,5],[-151,0,7],#cabinets
                [180,6,0],[186,6,0],[180,7,0],[189,7,0]],
	            "handObjList":[],
	            "shopArea":[]
            },
			5 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[1,3,8],#Door
                [190,0.5,0.5],[190,2.5,0.5],[190,4.5,0.5],
                [190,0.5,2.5],[190,2.5,2.5],[190,4.5,2.5],
                [190,0.5,4.5],[190,2.5,4.5],[190,4.5,4.5]],
	            "handObjList":[getHandObject(-1,[1.5*32,1.5*32]),getHandObject(-1,[3.5*32,1.5*32]),getHandObject(-1,[5.5*32,1.5*32]),
                    getHandObject(-1,[1.5*32,3.5*32]),getHandObject(-1,[3.5*32,3.5*32]),getHandObject(-1,[5.5*32,3.5*32]),
                    getHandObject(-1,[1.5*32,5.5*32]),getHandObject(-1,[3.5*32,5.5*32]),getHandObject(-1,[5.5*32,5.5*32])],
	            "shopArea":[[[-1,-1],[7,9]]]
            },
			6 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[191,0.5,9],[191,0.5,7],[191,0.5,5],[191,0.5,3],#benches left
                [191,6.5,9],[191,6.5,7],[191,6.5,5],[191,6.5,3],#benchez right
                [192,4.5,1],#pew
                [115,1,1],[193,1,0.5],[148,8,0.5],[194,8.8,0.3],
                [1,5,11]],
	            "handObjList":[],
	            "shopArea":[]
            },
			7 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[195,0,0]],
	            "handObjList":[getHandObject(330,[3*32,0*32]),
                    getHandObject(331,[3*32,1.5*32]),
                    getHandObject(45,[0*32,3.5*32]),
                    getHandObject(46,[2*32,3.5*32])],
	            "shopArea":[]
            },
			8 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[203,3.5,0],[2,-1,2],
                [198,1,3.5],[198,3,3.5],[198,5,3.5],[198,7,3.5],#Tables
                [198,1,5.5],[198,3,5.5],[198,5,5.5],[198,7,5.5],
                [211,7,0],[217,1,0],#Squeleton board
                [206,7,9.8],[17,6.2,9.8],[16,7.8,9.8]],
	            "handObjList":[],
	            "shopArea":[]
            },
			9 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[215,1,1],[216,4,1],[215,7,1],#Machines
                [216,1,3],[215,4,3],[216,7,3],
                [214,2,5.5],[215,5,5.5],
                [150,7.5,8],[150,9.5,8],#Cabinet
                [1,4,-1]],
	            "handObjList":[],
	            "shopArea":[]
            },
			10 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": extendList([[218,0,-0.5],[218,11,-0.5],[219,5,11],[15,6,12],[1,2,13]],getListObj(205,[2,2],[13,10],2,2)),
	            "handObjList" : getHandObjList(-1,[2.5*32,2*32],[13*32,10*32],2*32,2*32),
	            "shopArea":[[[-1,-1],[16,15]]]
            },
			11 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[226,0,-5],[227,5,-5],[1,4,7],[221,0,0],[221,1,0],[221,2,0],[221,3,0],[221,4,0],[221,5,0],[220,8,0],[202,8,2],[202,8,3.5],[202,8,5],[222,5.5,2.5],[222,5.5,5],[223,1,3]],
	            "handObjList":[],
	            "shopArea":[]
            },
# 			12 : {
# 	            "name": "defa",
# 	            "defOffset": [0,0],
# 	            "objList": [],
#                 "size": [9,15],
#                 "objListRot": [[50,1,1,0],[51,7,12,3],[0,4,0,0],[3,2,2,0],[4,3,3,0],[5,4,4,0],[52,5,5,0]],#,[2,0,12,1],[1,0,4,1]],#],#[self.obj(3,0,0),self.obj(4,5,11,1)],#[[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]],
# 	            "handObjList":[getHandObject(108,[2*32,2*32])],
# 	            "shopArea":[]
#             },
            50 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [8,14],
                "objListRot": [[8,0,0,0],[8,8,0,1],[8,0,14,2],[8,8,14,3],
                               [4,1,1,0],[4,7,1,1],[4,1,13,2],[4,7,13,3],
                               [5,3,3,0],[5,5,3,1],[5,3,11,2],[5,5,11,3],[50,1,1,0],[52,7,12,1],[51,1,12,3]],#,[2,0,12,1],[1,0,4,1]],#],#[self.obj(3,0,0),self.obj(4,5,11,1)],#[[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]],
	            "handObjList":[getHandObject(108,[2*32,2*32])],
	            "shopArea":[]
            },
            51 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [10,19],
                "objListRot": [[8,0,0,0],[8,10,0,1],[8,0,19,2],[8,10,19,3],
                               [4,1,1,0],[4,9,1,1],[4,1,18,2],[4,9,18,3],
                               [5,3,3,0],[5,7,3,1],[5,3,16,2],[5,7,16,3],[50,1,1,0],[52,9,17,1],[51,1,17,3]],
	            "handObjList":[],
	            "shopArea":[]
            },
			52 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [16,19],
                "objListRot": [[8,0,0,0],[8,16,0,1],[8,0,19,2],[8,16,19,3],
                               [4,1,1,0],[4,15,1,1],[4,1,18,2],[4,15,18,3],
                               [5,3,3,0],[5,13,3,1],[5,3,16,2],[5,13,16,3],[50,1,1,0],[52,15,17,1],[51,1,17,3]],#[[50,1,1,0],[51,15,17,3],[0,5,0,0]],
	            "handObjList":[],
	            "shopArea":[]
            },
            53 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [21,19],
                "objListRot": [[8,0,0,0],[8,21,0,1],[8,0,19,2],[8,21,19,3],[0,10,0,0]],
	            "handObjList":[],
	            "shopArea":[]
            },

        }
        self.index = index
        self.offset = offset
        self.masterTemplateList = [objectTemplate.masterTemplate1,objectTemplate.masterTemplate2,objectTemplate.masterTemplate3]
    
    def applyOffsetToTemplate(self,objList,handObjList,shopAreaList,offset,scale=32) :
        #print(offset)
        objListCopy = objList
        handObjListCopy = handObjList.copy()
        shopAreaListCopy = shopAreaList.copy()
        for i in range(len(objListCopy)) :  
            objListCopy[i][1] = objList[i][1] + offset[0]
            objListCopy[i][2] = objList[i][2] + offset[1]
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
        tempList = self.masterTemplateList[masterTemplateNum]
        
        objListBuff = []
        handObjListBuff = []
        shopAreaListBuff = []
        for temp in tempList :
            currentTemplate = self.templateList[temp[0]]
            
            if temp[0] in self.templateList.keys() :
                
                offset = [self.offset[0] + currentTemplate["defOffset"][0]+temp[1][0],self.offset[1] + currentTemplate["defOffset"][1]+temp[1][1]]
                
                #print(offset)
                objListt = []
                for i in currentTemplate["objList"]:
                    objListt.append(i)
                #print(objListt)
                #objListt = list(currentTemplate["objList"]).copy()
                if "objListRot" in currentTemplate.keys() :
                    objListRot = currentTemplate["objListRot"]
                    size = currentTemplate["size"]
                    objListDef = self.fromRotToStandardList(objListRot,temp[2])
                    extend2(objListt,objListDef)
                    objListt = self.objListRotaa(objListt,temp[2],size)
                    
                handObjList = currentTemplate["handObjList"]
                shopAreaList  = currentTemplate["shopArea"]
                
                objList2,handObjList,shopAreaList = self.applyOffsetToTemplate(objListt,handObjList,shopAreaList,offset)
                extend2(objListBuff,objList2)
                handObjListBuff.extend(handObjList)
                shopAreaListBuff.extend(shopAreaList)
                del(objListt)
                objListt = []
        return objListBuff,handObjListBuff,shopAreaListBuff

    def objListRotaa(self,objList,angle=0,size=[0,0]) :
        for obj in objList :
            # if len(obj)>3 :
            #     sizeobj = [obj[3][0],obj[3][1]]
            #     obj[1] = obj[1] - sizeobj[0]/2
            #     obj[2] = obj[2] - sizeobj[1]/2
            if angle == 2 or angle == 3:
                obj = self.mirrorObj(obj,size,angle)
                obj[1] = obj[1]#+0.5
            #if angle == 1 or angle == 3:
            #     obj = self.mirrorObjX(obj,size)
            #     obj = self.mirrorObj2(obj,size)

                #obj = self.mirrorObjX(obj,size)
                #obj = self.mirrorObjY(obj,size)
            if angle == 1 or angle == 3:
                obj = self.mirrorObjY(obj,size,angle)
                obj = self.mirrorObj2(obj,size)
                obj[1] = obj[1]#+0.5#int(obj[2])#+0.5
            #obj[1] = int(obj[1])
            #obj[2] = int(obj[2])
            # if len(obj)>3 :
            #     sizeobj = [obj[3][0],obj[3][1]]
            #     obj[1] = obj[1] + sizeobj[0]/2
            #     obj[2] = obj[2] + sizeobj[1]/2
            #obj[1] = int(obj[1])
            #obj[2] = int(obj[2])
                #x = -(obj[1]-int(size[0]/2))+int(size[0]/2)
                #y = -(obj[2]-int(size[1]/2))+int(size[1]/2)
                # sizeobj = [1,1]
                # if len(obj)>3 :
                #     sizeobj = [obj[3][0],obj[3][1]]
                # x = round(-(obj[1]-size[0]/2)+(size[0]/2)-(sizeobj[0]/2))#)#
                # y = round(-(obj[2]-size[1]/2)+(size[1]/2)-(sizeobj[1]/2))#)#
                # obj[1] = x
                # obj[2] = y
        # if angle == 1 or angle == 3:
        #     for obj in objList :
        #         sizeobj = [1,1]
        #         if len(obj)>3 :
        #             sizeobj = [obj[3][0],obj[3][1]]
        #         x = obj[1]
        #         y = obj[2]
        #         obj[1] = round(-(obj[2]-size[0]/2)+(size[0]/2)-(sizeobj[0]/2))
        #         obj[2] = round(-(obj[1]-size[1]/2)+(size[1]/2)-(sizeobj[1]/2))
        #         #obj[1] = x-sizeobj[0]
        #         #obj[2] = y-sizeobj[1]
        return objList
    
    def mirrorObj(self,obj,size,angle):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        x = -(obj[1]-(size[0]/2))+(size[0]/2)#-(sizeobj[0]/2)#)#
        y = -(obj[2]-(size[1]/2))+(size[1]/2)#-(sizeobj[1]/2)#)#
        if angle!=3 :
            if sizeobj[1]==2 :
                y = y-1
            if sizeobj[0]==2 :
                #x = x+1
                y = y-1
        obj[1] = x
        obj[2] = y
        return obj
    
    def mirrorObjX(self,obj,size):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        x = -(obj[1]-size[0]/2)+(size[0]/2)-(sizeobj[0]/2)
        obj[1] = x
        return obj
    
    def mirrorObjY(self,obj,size,angle):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        y = -(obj[2]-size[1]/2)+(size[1]/2)#-(sizeobj[1]-1)#)#
        x = obj[1]
        if angle!=3 :
            if sizeobj[0]==2 or sizeobj[1]==2:
        #if obj[0] == 128 or obj[0] == 129 or obj[0] == 130 :
            #print("cacaca",obj[0],"  ",sizeobj[0])
                y = y - 1
                #print("loool",sizeobj[0],"   ",obj[0])
        #if sizeobj[1]==2 :
            #x = x -10
        obj[2] = y
        obj[1] = x
        return obj
    
    def mirrorObj2(self,obj,size):
        x = obj[1]
        y = obj[2]
        obj[1] = y
        obj[2] = x
        return obj
    
    def mirrorObj3(self,obj,size):
        sizeobj = [1,1]
        if len(obj)>3 :
            sizeobj = [obj[3][0],obj[3][1]]
        x = round(-(obj[1]-size[0]/2)+(size[0]/2)-(sizeobj[0]/2))#)#
        y = round(-(obj[2]-size[1]/2)+(size[1]/2)-(sizeobj[1]/2))#)#
        obj[1] = x
        obj[2] = y
        return obj
    def getObjSettingFromID(self,idnum=0,name=None) :
        
        mapDict = {
            0: {"name":"door",
				"idList":[1,2,3,4],
				"size":[1,1]
                },
            1: {"name":"prison_door",
				"idList":[5,6,5,6],
				"size":[1,1]
                },
            2: {"name":"strong_door",
				"idList":[7,8,7,8],
				"size":[1,1]
                },
            3: {"name":"chair",
				"idList":[14,16,15,17],
				"size":[1,1]
                },
            4: {"name":"red_chair",
				"idList":[41,43,42,44],
				"size":[1,1]
                },
            5: {"name":"tv",
				"idList":[18,-20,19,20],
				"size":[1,1]
                },
            6: {"name":"radio",
				"idList":[21,23,22,-23],
				"size":[1,1]
                },
            7: {"name":"books",
				"idList":[24,25,26,-25],
				"size":[1,1]
                },
            8: {"name":"phone",
				"idList":[29,30,31,-31],
				"size":[1,1]
                },
			50: {"name":"bed",
				"idList":[100,102,101,-102],
				"size":[1,2]
                },
            51: {"name":"stove",
				"idList":[128,130,129,-130],
				"size":[1,2]
                },
            52: {"name":"sofa",
				"idList":[108,110,109,-110],
				"size":[2,1]
                },
            53: {"name":"big_table",
				"idList":[111,112,111,-112],
				"size":[2,1]
                },
				}
        if idnum in mapDict :
            return mapDict[idnum]
        else :
            return None
        
    def obj(self,objid,posx=0,posy=0,angle=0) :
        ret = [self.getObjSettingFromID(objid)["idList"][self.angleAdd(angle,1)],posx,posy]
        return ret
    
    def angleAdd(self,baseAngle,delta) :
        return (baseAngle+delta)%4
    
    def fromRotToStandardList(self,rotList,angle=0) :
        objList = []
        for item in rotList :
            angleNum = self.angleAdd(item[3],angle)
            objSize = self.getObjSettingFromID(item[0])["size"]
            if angleNum==1 or angleNum==3 :
                objSize = [objSize[1],objSize[0]]
                print(item[0])
            objList.append(list([self.getObjSettingFromID(item[0])["idList"][angleNum],item[1],item[2],objSize]))
        return objList
def extend2(list1,list2) :
    for ele in list2 :
        list1.append(list(ele))
    return list1