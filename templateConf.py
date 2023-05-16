# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 01:00:19 2023

@author: Alexandre
"""

import rangeWeapon as rw
import handObject as ho
import lootSelection as ls

class templateConf :
    def __init__(self):
        self.setupMasterTemplate()
        self.setupTemplateList()
        self.setupObjRotationMaping()
        
    def setupMasterTemplate(self) :
        self.masterTemplateDict = {
            0 : [[0,[3,3]],[1,[20,3]],[2,[18,24]],[3,[3,27]],[4,[3,41]],[5,[27,54]],[6,[44,36]],[7,[3,56]],[8,[59,36]],[9,[60,53]],[10,[37,55]],[11,[72,38]]],
            #1 : [[0,[119,164]],[1,[119,190]],[2,[149,161]],[3,[103,193]],[4,[87,187]]],
            1 : [[50,[2,2],0],[51,[2,27],1],[52,[2,52],2],[53,[2,77],3]],
            2 : [[50,[2,2],0],[50,[2,27],1],[50,[2,52],2],[50,[2,77],3],
                      [51,[27,2],0],[51,[27,27],1],[51,[27,52],2],[51,[27,77],3],
                      [52,[52,2],0],[52,[52,27],1],[52,[52,52],2],[52,[52,77],3],
                      [53,[76,1],0],[53,[76,26],1],[53,[76,51],2],[53,[76,76],3],[200,[76,76],3]],
            3 : [[0,[161,161]]]
        }
    
    def setupTemplateList(self) :
        self.templateList = {
            0 : {
	            "name": "house1",
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
                    [123,17,8.5],[128,21,8.5],[148,19,8.5],[132,22,12]],#Kitchen
	            "handObjList":[getHandObject(108,[23.5,12.5]),#Cabadge
                         getHandObject(214,[20,8.8]),#Eggs
                         getHandObject(217,[21.5,9]),#bakon
                         getHandObject(6,[19.5,19]),
                         getHandObject(4,[17.5,9]),
                         getHandObject(82,[18.7,16]),
                         getHandObject(0,[23.5,16],True).initRangeWeapon(rw.init(2))]
            },
			1 : {
	            "name": "house2",
	            "objList": [[116,0,0],[127,2.5,1.5],#Bathroom
                [2,5,0],[3,6,-1],[2,7,8],[2,7,5],[3,6,13],#Doors
                [113,8,0],[114,9.5,0],#Bed
                [-118,11,2],[119,11,0],#Closet and drawer
                [108,1.5,4],[162,1,5],[19,2,7],#Sofa, table, TV
                [126,2,9],[138,1.3,10],[137,3.2,10],#dining table and chairs
                [123,8,11.5],[148,10,11.5],[130,12,9],[133,12,7]],#[-141,20,20]],
	            "handObjList":[getHandObject(316,[12.5,9.2]),#Stew
                    getHandObject(107,[8.9,1]),#Cloth
                    getHandObject(213,[12,5])]#Books
            },
			2 : {
	            "name": "office1",
	            "objList": [[1,2,-1],[3,3,-1],[2,6,2],[2,5,15],[2,5,22],[2,8,22],[2,13,20],#Doors
                [149,8,-0.5],[149,9.5,-0.5],[149,11,-0.5],[145,12.5,-0.5],[145,14,-0.5],#filer and cabinet
                [140,2,3],[15,2.5,4],
                [139,1.5,8],[14,2,7],[139,1.5+3.5*1,8],[14,2+3.5*1,7],[139,1.5+3.5*2,8],[14,2+3.5*2,7],[139,1.5+3.5*3,8],[14,2+3.5*3,7],[139,1.5+3.5*4,8],[14,2+3.5*4,7],[139,1.5+3.5*5,8],[14,2+3.5*5,7],
                [139,1.5,11],[14,2,10],[139,1.5+3.5*1,11],[14,2+3.5*1,10],[139,1.5+3.5*2,11],[14,2+3.5*2,10],[139,1.5+3.5*3,11],[14,2+3.5*3,10],[139,1.5+3.5*4,11],[14,2+3.5*4,10],[139,1.5+3.5*5,11],[14,2+3.5*5,10],             
                [123,9,18.5],[128,11,18.5],[148,9,23.5],[132,11,24],#Kitchen
                [144,1,15],[17,0,15.5],[144,1,21],[17,0,21.5],#2 offices
                [151,4,13],[147,4,16],[151,4,18],[147,4,19],#Cabinets
                [164,8,14],[135,9,13],[164,12,14],[135,13,13],[164,16,14],[135,17,13],[165,20.5,19],[138,20,20],#Computer
                [166,15,17],[167,15,21],#Machine
                [109,10,17],[170,21,15],[173,21,16.5]],
            },
			3 : {
	            "name": "hospital",
	            "objList": [[1,4,-1],[-161,0,0.5],[-161,0,3],[-161,0,5.5],
                [176,6,1],[176,6,2.5],[176,6,4],[176,6,5.5],
                [179,7,7],[178,4,9],[177,2,0]],
            },
			4 : {
	            "name": "police",
	            "objList": [[7,4,-1],[7,4,1],[5,1,2],#Doors
                [102,0,0],[10,2,0],#Prison cell
                [109,5.5,9],[162,4.5,7],#relax area
                [165,6.5,3],[138,6,4],
                [-151,0,3],[-151,0,5],[-151,0,7],#cabinets
                [180,6,0],[186,6,0],[180,7,0],[189,7,0]],
            },
			5 : {
	            "name": "shop1",
	            "objList": [[1,3,8],#Door
                [190,0.5,0.5],[190,2.5,0.5],[190,4.5,0.5],
                [190,0.5,2.5],[190,2.5,2.5],[190,4.5,2.5],
                [190,0.5,4.5],[190,2.5,4.5],[190,4.5,4.5]],
	            "handObjList":[getHandObject(-1,[1.5,1.5]),getHandObject(-1,[3.5,1.5]),getHandObject(-1,[5.5,1.5]),
                    getHandObject(-1,[1.5,3.5]),getHandObject(-1,[3.5,3.5]),getHandObject(-1,[5.5,3.5]),
                    getHandObject(-1,[1.5,5.5]),getHandObject(-1,[3.5,5.5]),getHandObject(-1,[5.5,5.5])],
	            "shopArea":[[[-1,-1],[7,9]]]
            },
			6 : {
	            "name": "church",
	            "objList": [[191,0.5,9],[191,0.5,7],[191,0.5,5],[191,0.5,3],#benches left
                [191,6.5,9],[191,6.5,7],[191,6.5,5],[191,6.5,3],#benchez right
                [192,4.5,1],#pew
                [115,1,1],[193,1,0.5],[148,8,0.5],[194,8.8,0.3],
                [1,5,11]],
            },
			7 : {
	            "name": "garden",
	            "objList": [[195,0,0]],
	            "handObjList":[getHandObject(330,[3,0]),
                    getHandObject(331,[3,1.5]),
                    getHandObject(45,[0,3.5]),
                    getHandObject(46,[2,3.5])],
            },
			8 : {
	            "name": "classroom",
	            "objList": [[203,3.5,0],[2,-1,2],
                [198,1,3.5],[198,3,3.5],[198,5,3.5],[198,7,3.5],#Tables
                [198,1,5.5],[198,3,5.5],[198,5,5.5],[198,7,5.5],
                [211,7,0],[217,1,0],#Squeleton board
                [206,7,9.8],[17,6.2,9.8],[16,7.8,9.8]]
            },
			9 : {
	            "name": "workshop",
	            "objList": [[215,1,1],[216,4,1],[215,7,1],#Machines
                [216,1,3],[215,4,3],[216,7,3],
                [214,2,5.5],[215,5,5.5],
                [150,7.5,8],[150,9.5,8],#Cabinet
                [1,4,-1]]
            },
			10 : {
	            "name": "shop2",
	            "objList": extendList([[218,0,-0.5],[218,11,-0.5],[219,5,11],[15,6,12],[1,2,13]],getListObj(205,[2,2],[13,10],2,2)),
	            "handObjList" : getHandObjList(-1,[2.5,2],[13,10],2,2),
	            "shopArea":[[[-1,-1],[16,15]]]
            },
			11 : {
	            "name": "gym",
	            "objList": [[1,4,7],[221,0,0],[221,1,0],[221,2,0],[221,3,0],[221,4,0],[221,5,0],[220,8,0],[202,8,2],[202,8,3.5],[202,8,5],[222,5.5,2.5],[222,5.5,5],[223,1,3]]
            },
            50 : {
	            "name": "defa",
	            "objList": [[114,1,12]],
                "size": [8,14],
                "objListRot": [[0,4,0],#Door
                               [0,4,10],#Door
                               [53,7,1,1],#Kitchen
                               [64,7,3,1],
                               [51,1.5,3.5,2],#Tv
                               [5,2,1.5,0],
                               [65,1,6,0],#table
                               [12,2,5.5,0],
                               [12,2,7.5,2],
                               [13,7,13,1],#Shower
                               [14,6,11],
                               [50,1,13,3],#Bed
                               [7,3,11,0],
                               [15,5,11,1],
                               [15,5,13,1]#,
                               #[69,1,1,0]
                               
                               ]
            },
            51 : {
	            "name": "defa",
	            "objList": [[255,9,12]],#[213,1.5,0.5],[255,9,12]],#[281,6.5,0.5],
                "size": [10,19],
                "objListRot": [[0,5,0,0],#Door
                               [0,7,13,2],
                               [0,4,16,1],
                               [53,1,12,2],
                               [54,3,12,2],
                               [64,1,9,3],
                               [68,7,8,1],
                               [3,9,8,1],
                               [3,9,10,1],
                               [3,6,8,3],
                               [3,6,10,3],
                               [16,6.5,0.5,0],
                               [21,1.25,0,0],
                               [70,8,17,2,5],
                               #["big_wood_table",8,17,2],
                               # [16,1.5,0.5,0],
                               # [17,2.5,1,0],
                               # [18,3.5,1,0],
                               # [19,4.5,0.5,0],
                               # [20,5.5,0.5,0],
                               # [21,6.5,0.5,0],
                               # [22,7.5,0.5,0],
                               # [23,8.5,0.5,0],
                               ]
            },
			52 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [16,19],
                "objListRot": [[0,5,0,0]#Door
                         ],
	            "handObjList":[],
	            "shopArea":[]
            },
            53 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [21,19],
                "objListRot": [[0,10,0,0]#Door
                               ],
	            "handObjList":[],
	            "shopArea":[]
            },
            60 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [[0,3,3]],
                "size": [8,14],
                "objListRot": [[8,0,0,0],[8,8,0,1],[8,0,14,2],[8,8,14,3],
                               [4,1,1,0],[4,7,1,1],[4,1,13,2],[4,7,13,3],
                               [5,3,3,0],[5,5,3,1],[5,3,11,2],[5,5,11,3],[50,1,1,0],[53,7,12,1],[51,1,12,3]],#,[2,0,12,1],[1,0,4,1]],#],#[self.obj(3,0,0),self.obj(4,5,11,1)],#[[101,0,11],[130,6,0],[-263,6,1.7],[109,0.5,3],[18,1,0],[-141,6,11],[44,4.7,11.5]],
	            "handObjList":[],#[108,2,2,-1]],#getHandObject(108,[2,2])
	            "shopArea":[]
            },
            61 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [10,19],
                "objListRot": [[8,0,0,0],[8,10,0,1],[8,0,19,2],[8,10,19,3],
                               [4,1,1,0],[4,9,1,1],[4,1,18,2],[4,9,18,3],
                               [5,3,3,0],[5,7,3,1],[5,3,16,2],[5,7,16,3],[50,1,1,0],[53,9,17,1],[51,1,17,3],[59,8,1,0]],
	            "handObjList":[],
	            "shopArea":[]
            },
			62 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [16,19],
                "objListRot": [[8,0,0,0],[8,16,0,1],[8,0,19,2],[8,16,19,3],
                               [4,1,1,0],[4,15,1,1],[4,1,18,2],[4,15,18,3],
                               [5,3,3,0],[5,13,3,1],[5,3,16,2],[5,13,16,3],[50,1,1,0],[53,15,17,1],[51,1,17,3]],#[[50,1,1,0],[51,15,17,3],[0,5,0,0]],
	            "handObjList":[],
	            "shopArea":[]
            },
            63 : {
	            "name": "defa",
	            "defOffset": [0,0],
	            "objList": [],
                "size": [21,19],
                "objListRot": [[8,0,0,0],[8,21,0,1],[8,0,19,2],[8,21,19,3],[0,10,0,0]],#,[50,1,17,2],[50,20,17,2]],
	            "handObjList":[],
	            "shopArea":[]
            }
        }
             
    def setupObjRotationMaping(self) :
        self.objRotMapping = {
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
				"idList":[18,20,19,-20],
				"size":[1,1]
                },
            6: {"name":"radio",
				"idList":[21,23,22,-23],
				"size":[1,1]
                },
            7: {"name":"books",
				"idList":[24,26,25,-26],
				"size":[1,1]
                },
            8: {"name":"phone",
				"idList":[29,31,30,-31],
				"size":[1,1]
                },
            9: {"name":"trash",
				"idList":[32,34,33,-34],
				"size":[1,1]
                },
            10: {"name":"sofa_small",
				"idList":[35,37,36,-37],
				"size":[1,1]
                },
            11: {"name":"sofa_brown_small",
				"idList":[38,40,39,-40],
				"size":[1,1]
                },
            12: {"name":"fancy_chair",
				"idList":[135,137,136,138],
				"size":[1,1]
                },
            13: {"name":"toilet",
				"idList":[45,47,46,-47],
				"size":[1,1]
                },
            14: {"name":"shower",
				"idList":[48,50,49,-50],
				"size":[1,1]
                },            
            15: {"name":"divider",
				"idList":[51,52,53,54],
				"size":[1,1]
                },
            16: {"name":"coat_hanger",
				"idList":[281,281,281,281],
				"size":[1,2.5],
                "offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            17: {"name":"boombox",
				"idList":[204,204,204,204],
				"size":[1,1],
                #"offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            18: {"name":"chess",
				"idList":[206,206,206,206],
				"size":[1,1],
                #"offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            19: {"name":"painting",
				"idList":[210,210,210,210],
				"size":[1,2.5],
                "offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            20: {"name":"fan",
				"idList":[282,282,282,282],
				"size":[1,2.5],
                "offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            21: {"name":"lamp",
				"idList":[213,213,213,213],
				"size":[0.5,2],
                "offset":[None,[-1,0],[-0.5,1],[0.5,1]],
                "noRot":False
                },
            22: {"name":"punchingball",
				"idList":[222,222,222,222],
				"size":[1,2.5],
                "offset":[None,None,None,[1,0.5]],
                "noRot":False
                },
            23: {"name":"watertower",
				"idList":[283,283,283,283],
				"size":[1,2.5],
                "offset":[None,None,None,[1,0.5]],
                "noRot":False
                },


			50: {"name":"bed",
				"idList":[100,102,101,-102],
				"size":[1,2]
                },
            51: {"name":"sofa",
				"idList":[108,110,109,-110],
				"size":[2,1]
                },
            52: {"name":"big_table",
				"idList":[111,112,111,-112],
				"size":[4,1.5]
                },
            53: {"name":"stove",
				"idList":[128,130,129,-130],
				"size":[2,1]
                },
            54: {"name":"fridge",
				"idList":[131,133,132,-133],
				"size":[2,1]
                },            
            55: {"name":"office",
				"idList":[140,141,139,-141],
				"size":[2,1]
                },            
            56: {"name":"office_fancy",
				"idList":[143,144,142,-144],
				"size":[2,1]
                },            
            57: {"name":"filler",
				"idList":[145,-147,146,147],
				"size":[1,1.5]
                },            
            58: {"name":"cabinet",
				"idList":[149,151,150,-151],
				"size":[1,2]
                },               
            59: {"name":"med_bed",
				"idList":[159,161,160,-161],
				"size":[2,2]
                },
            60: {"name":"soda_machine",
				"idList":[168,170,169,-170],
				"size":[1,2]
                },              
            61: {"name":"game_machine",
				"idList":[171,173,172,-173],
				"size":[2,2]
                },              
            62: {"name":"slab",
				"idList":[174,176,175,-176],
				"size":[2,2]
                },              
            63: {"name":"health_mesure",
				"idList":[177,179,178,-179],
				"size":[2,2]
                },            
            64: {"name":"small_sink",
				"idList":[261,263,262,-263],
				"size":[2,1]
                },
            65: {"name":"white_table",
				"idList":[273,274,273,274],
				"size":[3,2]
                },
            66: {"name":"big_white_table",
				"idList":[275,276,275,276],
				"size":[3,2]
                },
            67: {"name":"wood_table",
				"idList":[277,278,277,278],
				"size":[3,2]
                },
            68: {"name":"big_wood_table",
				"idList":[279,280,279,280],
				"size":[3,2]
                },
            69: {"name":"electrict",
				"idList":[166,166,166,166],
				"size":[3,3]
                },
            70: {"name":"big_bed",
				"idList":[284,286,285,-286],
                "difColorOffset":3,
				"size":[2,2]
                }
            }


def getHandObject(spriteNum=0,pos=[0,0],invisible=False,scale=32) :
    pos = [pos[0]*scale,pos[1]*scale]
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