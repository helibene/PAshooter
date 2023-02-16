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

class objectTemplate :
    
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
        #print("aggobj :",return_list)
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
        #print("aggobj :",return_list)
        return return_list
    
    def extendList(list1,list2) :
        list1.extend(list2)
        #print("list1 :",list1)
        return list1
        
    defaultOffset0=[-11,-9]#House 1
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
    handObjList0 = [getHandObject(108,[22.5*32,12*32]),#Cabadge
                        getHandObject(214,[20*32,8.8*32]),#Eggs
                        getHandObject(217,[21.5*32,9*32]),#bakon
                        getHandObject(6,[19.5*32,19*32]),
                        getHandObject(4,[17.5*32,9*32]),
                        getHandObject(82,[18.7*32,16*32]),
                        getHandObject(0,[23.5*32,16*32],True).initRangeWeapon(rw.init(2))]
    
    defaultOffset1 = [0,0]#House 2
    objList1 = [[116,0,0],[127,2.5,1.5],#Bathroom
                [2,5,0],[3,6,-1],[2,7,8],[2,7,5],[3,6,13],#Doors
                [113,8,0],[114,9.5,0],#Bed
                [-118,11,2],[119,11,0],#Closet and drawer
                [108,1.5,4],[162,1,5],[19,2,7],#Sofa, table, TV
                [126,2,9],[138,1.3,10],[137,3.2,10],#dining table and chairs
                [123,8,11.5],[148,10,11.5],[130,12,9],[133,12,7]#Kitchen
                ]
    handObjList1 = [getHandObject(316,[12.5*32,9*32]),#Stew
                    getHandObject(107,[8.9*32,1*32]),#Cloth
                    getHandObject(213,[12*32,5*32])]#Books
    
    defaultOffset2 = [0,0]#Office
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
    
    defaultOffset3 = [0,0]#Medical
    objList3 = [[1,4,-1],[-161,0,0.5],[-161,0,3],[-161,0,5.5],
                [176,6,1],[176,6,2.5],[176,6,4],[176,6,5.5],
                [179,7,7],[178,4,9],[177,2,0]]
    handObjList3 = []
    
    defaultOffset4 = [0,0]#Police
    objList4 = [[7,4,-1],[7,4,1],[5,1,2],#Doors
                [102,0,0],[10,2,0],#Prison cell
                [109,5.5,9],[162,4.5,7],#relax area
                [165,6.5,3],[138,6,4],
                [-151,0,3],[-151,0,5],[-151,0,7],#cabinets
                [180,6,0],[186,6,0],[180,7,0],[189,7,0]]#[180,0,9],[183,0,9.3],
    handObjList4 = []
    
    defaultOffset5 = [0,0]#Shop
    objList5 = [[1,3,8],#Door
                [190,0.5,0.5],[190,2.5,0.5],[190,4.5,0.5],
                [190,0.5,2.5],[190,2.5,2.5],[190,4.5,2.5],
                [190,0.5,4.5],[190,2.5,4.5],[190,4.5,4.5]]#[180,0,9],[183,0,9.3],
    handObjList5 = [getHandObject(-1,[1.5*32,1.5*32]),getHandObject(-1,[3.5*32,1.5*32]),getHandObject(-1,[5.5*32,1.5*32]),
                    getHandObject(-1,[1.5*32,3.5*32]),getHandObject(-1,[3.5*32,3.5*32]),getHandObject(-1,[5.5*32,3.5*32]),
                    getHandObject(-1,[1.5*32,5.5*32]),getHandObject(-1,[3.5*32,5.5*32]),getHandObject(-1,[5.5*32,5.5*32])]
    
    defaultOffset6 = [0,0]#Church
    objList6 = [[191,0.5,9],[191,0.5,7],[191,0.5,5],[191,0.5,3],#benches left
                [191,6.5,9],[191,6.5,7],[191,6.5,5],[191,6.5,3],#benchez right
                [192,4.5,1],#pew
                [115,1,1],[193,1,0.5],[148,8,0.5],[194,8.8,0.3],
                [1,5,11]]#[180,0,9],[183,0,9.3],
    handObjList6 = []
    
    defaultOffset7 = [0,0]#Garden
    objList7 = [[195,0,0]]#Small house
    handObjList7 = [getHandObject(330,[3*32,0*32]),
                    getHandObject(331,[3*32,1.5*32]),
                    getHandObject(45,[0*32,3.5*32]),
                    getHandObject(46,[2*32,3.5*32]),
                    #getHandObject(197,[6*32,6*32]),
                    #getHandObject(198,[8*32,8*32]),
                    ]
    
    defaultOffset8 = [0,0]#School
    objList8 = [[203,3.5,0],[2,-1,2],
                [198,1,3.5],[198,3,3.5],[198,5,3.5],[198,7,3.5],#Tables
                [198,1,5.5],[198,3,5.5],[198,5,5.5],[198,7,5.5],
                [211,7,0],[217,1,0],#Squeleton board
                [206,7,9.8],[17,6.2,9.8],[16,7.8,9.8]]#chess
    handObjList8 = []
    
    defaultOffset9 = [0,0]#Wood working
    objList9 = [[215,1,1],[216,4,1],[215,7,1],#Machines
                [216,1,3],[215,4,3],[216,7,3],
                [214,2,5.5],[215,5,5.5],
                [150,7.5,8],[150,9.5,8],#Cabinet
                [1,4,-1]
                ]
    handObjList9 = []
    
    defaultOffset10 = [0,0]
    objList10 = extendList([[218,0,-0.5],[218,11,-0.5],[219,5,11],[15,6,12],[1,2,13]],getListObj(205,[2,2],[13,10],2,2))
    handObjList10 = getHandObjList(-1,[2.5*32,2*32],[13*32,10*32],2*32,2*32)
    
    defaultOffset11 = [0,0]
    objList11 = [[226,0,-5],[227,5,-5],[1,4,7],[221,0,0],[221,1,0],[221,2,0],[221,3,0],[221,4,0],[221,5,0],[220,8,0],[202,8,2],[202,8,3.5],[202,8,5],[222,5.5,2.5],[222,5.5,5],[223,1,3]]
    handObjList11 = []
    
    defaultOffset12 = [0,0]
    objList12 = [[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]]
    handObjList12 = [getHandObject(108,[2*32,2*32])]
    
    shopAreaTemplate1 = [[-1,-1],[7,9]]
    shopAreaTemplate2 = [[-1,-1],[16,15]]
    masterTemplate1 = [[0,[3,3]],[1,[20,3]],[2,[18,24]],[3,[3,27]],[4,[3,41]],[5,[27,54]],[6,[44,36]],[7,[3,56]],[8,[59,36]],[9,[60,53]],[10,[37,55]],[11,[72,38]]]#,[-1,[27,54]]]
    masterTemplate2 = [[0,[119,164]],[1,[119,190]],[2,[149,161]],[3,[103,193]],[4,[87,187]]]
    masterTemplate3 = [[0,[3,3]]]#[[12,[3,3]]]
    
    def __init__(self,index,offset=[0,0]):
#         self.templateList = {
#             0 : {
# 	            "name": "defa",
# 	            "defOffset": [0,0],
# 	            "objList": [[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]],
# 	            "handObjList":[getHandObject(108,[2*32,2*32])],
# 	            "shopArea":[[[0,0],[2,2]]]
#             },
#             1 : {
# 	            "name": "defa",
# 	            "defOffset": [0,0],
# 	            "objList": [],
# 	            "handObjList":[],
# 	            "shopArea":[]
#             }
#         }
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
                [123,8,11.5],[148,10,11.5],[130,12,9],[133,12,7]],
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
	            "objList": self.extendList([[218,0,-0.5],[218,11,-0.5],[219,5,11],[15,6,12],[1,2,13]],self.getListObj(205,[2,2],[13,10],2,2)),
	            "handObjList" : self.getHandObjList(-1,[2.5*32,2*32],[13*32,10*32],2*32,2*32),
	            "shopArea":[[[-1,-1],[16,15]]]
            },
			11 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[226,0,-5],[227,5,-5],[1,4,7],[221,0,0],[221,1,0],[221,2,0],[221,3,0],[221,4,0],[221,5,0],[220,8,0],[202,8,2],[202,8,3.5],[202,8,5],[222,5.5,2.5],[222,5.5,5],[223,1,3]],
	            "handObjList":[],
	            "shopArea":[]
            },
			12 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]],
	            "handObjList":[getHandObject(108,[2*32,2*32])],
	            "shopArea":[[[0,0],[2,2]]]
            },
			13 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
	            "handObjList":[],
	            "shopArea":[]
            },
			14 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
	            "handObjList":[],
	            "shopArea":[]
            }
        }
        self.index = index
        self.offset = offset
        self.objMat = [objectTemplate.objList0,objectTemplate.objList1,objectTemplate.objList2,objectTemplate.objList3,objectTemplate.objList4,objectTemplate.objList5,objectTemplate.objList6,objectTemplate.objList7,objectTemplate.objList8,objectTemplate.objList9,objectTemplate.objList10,objectTemplate.objList11,objectTemplate.objList12]
        self.handObjMat = [objectTemplate.handObjList0,objectTemplate.handObjList1,objectTemplate.handObjList2,objectTemplate.handObjList3,objectTemplate.handObjList4,objectTemplate.handObjList5,objectTemplate.handObjList6,objectTemplate.handObjList7,objectTemplate.handObjList8,objectTemplate.handObjList9,objectTemplate.handObjList10,objectTemplate.handObjList11,objectTemplate.handObjList12]
        self.defaultOffsetList = [objectTemplate.defaultOffset0,objectTemplate.defaultOffset1,objectTemplate.defaultOffset2,objectTemplate.defaultOffset3,objectTemplate.defaultOffset4,objectTemplate.defaultOffset5,objectTemplate.defaultOffset6,objectTemplate.defaultOffset7,objectTemplate.defaultOffset8,objectTemplate.defaultOffset9,objectTemplate.defaultOffset10,objectTemplate.defaultOffset11,objectTemplate.defaultOffset12]
        self.shopAreaList = [objectTemplate.shopAreaTemplate1,objectTemplate.shopAreaTemplate2]
        self.masterTemplateList = [objectTemplate.masterTemplate1,objectTemplate.masterTemplate2,objectTemplate.masterTemplate3]
    
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
            if type(handObjListCopy[i]) != type(ho.handObject()):
                handObjListCopy[i][1] = handObjListCopy[i][1] + offset[0]*scale
                handObjListCopy[i][2] = handObjListCopy[i][2] + offset[1]*scale
            else :
                handObjListCopy[i].pos[0] = handObjListCopy[i].pos[0] + offset[0]*scale
                handObjListCopy[i].pos[1] = handObjListCopy[i].pos[1] + offset[1]*scale
        return objListCopy,handObjListCopy
    
    def applyOffsetToTemplate2(self,objList,handObjList,shopAreaList,offset,scale=32) :
        objListCopy = objList.copy()
        handObjListCopy = handObjList.copy()
        shopAreaListCopy = shopAreaList.copy()
        for i in range(len(objList)) :
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
    
    
    def applyOffsetShopArea(self,shopArea,offset,scale=32) :
        return [[(shopArea[0][0]+offset[0])*scale,(shopArea[0][1]+offset[1])*scale],[(shopArea[1][0]+offset[0])*scale,(shopArea[1][1]+offset[1])*scale]]
    
    def deleteAllData(self) :
        del(self.objMat)
        del(self.handObjMat)
        del(self)

    def templateListToObjList(self,masterTemplateNum) :
        objListBuff = []
        handObjListBuff = []
        shopAreaList = []
        tempList = self.masterTemplateList[masterTemplateNum]
        
        for temp in tempList :
            if temp[0]<0 :
                shopAreaList.append(self.applyOffsetShopArea(self.shopAreaList[abs(temp[0])-1],temp[1]))
            else :
                otinst = objectTemplate(temp[0],temp[1])#
                objList,handObjList = otinst.getTemplateList()
                objListBuff.extend(objList)
                handObjListBuff.extend(handObjList)
                del(otinst)
        return objListBuff,handObjListBuff,shopAreaList

    def templateListToObjList2(self,masterTemplateNum) :
        tempList = self.masterTemplateList[masterTemplateNum]
        objListBuff = []
        handObjListBuff = []
        shopAreaListBuff = []
        for temp in tempList :
            if temp[0] in self.templateList.keys() :
                offset = [self.offset[0] + self.templateList[temp[0]]["defOffset"][0]+temp[1][0],self.offset[1] + self.templateList[temp[0]]["defOffset"][1]+temp[1][1]]
                objList = self.templateList[temp[0]]["objList"]
                handObjList = self.templateList[temp[0]]["handObjList"]
                shopAreaList  = self.templateList[temp[0]]["shopArea"]
                print(shopAreaList)
                objList,handObjList,shopAreaList = self.applyOffsetToTemplate2(objList,handObjList,shopAreaList,offset)
                objListBuff.extend(objList)
                handObjListBuff.extend(handObjList)
                shopAreaListBuff.extend(shopAreaList)               
        return objListBuff,handObjListBuff,shopAreaListBuff

    def getHandObjList(self,spriteNum=0,pos=[0,0],posEnd=[2,2],stepX=1,stepY=1) :
        posX = pos[0]
        posY = pos[1]
        return_list = []
        while posY<posEnd[1] :
            while posX<posEnd[0] :
                return_list.append(getHandObject(spriteNum,[posX,posY]))
                posX = posX + stepX
            posX = pos[0]
            posY = posY + stepY
        #print("aggobj :",return_list)
        return return_list
    
    def extendList(self,list1,list2) :
        list1.extend(list2)
        #print("list1 :",list1)
        return list1
    
    def getListObj(self,spriteNum=0,pos=[0,0],posEnd=[2,2],stepX=1,stepY=1) :
        posX = pos[0]
        posY = pos[1]
        return_list = []
        while posY<posEnd[1] :
            while posX<posEnd[0] :
                return_list.append([spriteNum,posX,posY])
                posX = posX + stepX
            posX = pos[0]
            posY = posY + stepY
        #print("aggobj :",return_list)
        return return_list