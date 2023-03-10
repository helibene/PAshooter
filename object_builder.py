# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:51:09 2023

@author: Alexandre
"""
from PIL import ImageTk,Image
import sys
import math

class object_builder :
    def __init__(self,objSheetSetting):
        self.objSheetSetting = objSheetSetting
        self.imageMat = [[None for x in range(self.objSheetSetting[4]*2)] for y in range(self.objSheetSetting[3]*2)] 
        self.imageMat2 = [[None for x in range(self.objSheetSetting[4])] for y in range(self.objSheetSetting[3])] 
        
        self.step_x = int(self.objSheetSetting[1]/self.objSheetSetting[3])
        self.step_y = int(self.objSheetSetting[2]/self.objSheetSetting[4])
        self.img = self.objSheetSetting[0]
        self.spriteList = [None for x in range(350)]
        self.spriteListFlip = [None for x in range(350)]
        for x in range(self.objSheetSetting[3]) :
            for y in range(self.objSheetSetting[4]) :
                box = ([int(x*self.step_x),int(y*self.step_y),int((x+1)*self.step_x),int((y+1)*self.step_y)])
                self.imgCrop = self.img.crop(box)
                self.imageMat2[x][y] = self.imgCrop
        for x in range(self.objSheetSetting[3]*2) :
            for y in range(self.objSheetSetting[4]*2) :
                box = ([int(x*self.step_x/2),int(y*self.step_y/2),math.ceil((x+1)*self.step_x/2),math.ceil((y+1)*self.step_y/2)])
                self.imgCrop = self.img.crop(box)
                self.imageMat[x][y] = self.imgCrop
    
    def deleteSpriteMatrix(self) :
        del(self.imageMat)
        del(self.imageMat2)
        del(self.objSheetSetting)
        del(self.img)
    
    def getSprite(self,num,rawImage=False) :
        flip = False
        if num <0 :
            num = abs(num)
            flip = True
        if self.spriteList[num]!=None and not rawImage and not flip :
            return self.spriteList[num]
        if self.spriteListFlip[num]!=None and not rawImage and flip:
            return self.spriteListFlip[num]
        mapDict = {
            0: [0,0],
            1: [1,0],#Door h1
            2: [3,0],#v1
            3: [5,0],#h2
            4: [7,0],#v2
            5: [0,2],#Prison Door h
            6: [1,2],#v
            7: [1,1],#Strong door h
            8: [2,1],#v
            9: [2,3],
            10: [0,5],
            11: [0,6],
            12: [5,1],
            13: [6,2],
            14: [0,20],#Chair
            15: [1,20],
            16: [2,20],
            17: [3,20],
            18 : [2,3],#TV
            19 : [3,3],
            20 : [4,3],
            21 : [7,3],#Radio
            22 : [8,3],
            23 : [9,3],
            24 : [0,6],#Books
            25 : [1,6],
            26 : [2,6],
            27 : [6,28],#Bush
            28 : [6,29],
            29 : [5,1],#Phone
            30 : [6,1],
            31 : [7,1],
            32 : [6,2],#Trash
            33 : [7,2],
            34 : [8,2],
            35 : [12,7],#Sofa
            36 : [13,7],
            37 : [14,7],
            38 : [12,5],#Sofa brown
            39 : [13,5],
            40 : [14,5],
            41: [8,20],#Chair red
            42: [9,20],
            43: [10,20],
            44: [11,20],
            45 : [0,5],#Toilet
            46 : [1,5],
            47 : [2,5],
            48 : [4,4],#Shower
            49 : [5,4],
            50 : [6,4],
            51 : [26,6],#Divider
            52 : [27,6],
            53 : [28,6],
            54 : [29,6],
        }
        if num in mapDict :
            coord = mapDict[num]
            image = self.imageMat2[coord[0]][coord[1]]
            if flip :
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if rawImage :
                return image
            else :
                tkimg = ImageTk.PhotoImage(image)
                if not flip :
                    self.spriteList[num] = tkimg
                else :
                    self.spriteListFlip[num] = tkimg
                return tkimg
        
        mapDict2 = {
            100: [0,3,0,4],#Bed
            101: [1,3,1,4],
            102: [2,4,3,4],
            103: [0,28,1,29],#Trees
            104: [2,28,3,29],
            105: [4,28,5,29],
            106: [0,30,1,31],
            107: [2,30,3,31],
            108: [15,7,16,7],#Sofa
            109: [17,7,18,7],
            110: [19,6,19,7],
            111: [5,9.5,8.5,10],#Table
            112: [9.5,7,10,10],
            113: [0,25,0.5,26],#Big bed vBig bed and tables
            114: [1.5,25,1.5,25],#h
            115: [1.5,26,1.5,26],
            116: [2.5,25,2.5,25],#Toilets
            117: [2.5,26,2.5,26],#Mirror
            118: [3.5,25,4.5,26],#Closet
            119: [3.5,27,4.5,27],#Drawers
            120: [5.5,25,5.5,27],#Sofa
            121: [6.5,25,6.5,27],#Cofe table
            122: [7.5,25,7.5,27],#Big TV
            123: [8.5,25,9.5,25.5],#Big table 
            124: [8.5,26.5,8.5,27],#desk
            125: [9.5,26.5,10.5,27],
            126: [16.5,24,17,26],#Big table with plates
            127: [9,28,11,28.5],#Bath
            128: [0,7.5,1,8],#Stove
            129: [2,7.5,3,8],
            130: [4,7,4,8],
            131: [0,9.5,1,10],#Fridge
            132: [2,9.5,3,10],
            133: [4,9,4,10],
            134: [4,4,4,3.5],#Shower
            135: [9,29.5,9,29.5],#Fancy chair
            136: [10,29.5,10,29.5],
            137: [11,29.5,11,29.5],
            138: [12,29.5,12,29.5],
            139: [0,21,1,21],#Office
            140: [2,21,3,21],
            141: [4,20,4,21],
            142: [11.5,24,12.5,24],#Office fancy
            143: [13.5,24,14.5,24],
            144: [15.5,23,15.5,24],
            145: [5,20,5,21],#Office filer
            146: [6,20,6,21],
            147: [7,20,7,21],
            148: [18,25.5,19,26],#Counter
            149: [22,8.5,22,9.5],#Cabinet
            150: [23,9,23,10],
            151: [24,9,24,10],
            152: [22,10.5,22,12],
            153: [23,11,23,12],
            154: [24,11,24,12],
            155: [12,10.5,12,11],#Washing
            156: [13,10.5,13,11],
            157: [14,10.5,14,11],
            158: [15,10.5,15,11],
            159: [11.5,14.5,12.5,15.5],#Med bed
            160: [13.5,14.5,14.5,15.5],
            161: [15.5,14.5,16.5,15.5],
            162: [5,8,7.5,8.5],#Small coffe table
            163: [11,12.5,13.5,13],#Computer
            164: [14.5,12.5,16.5,13],
            165: [17.5,11,18,13],
            166: [0,22,2,24],#Power gen
            167: [5,22,7,24],#Water gen
            168: [20,5.5,20,6],#Soda machine
            169: [21,5.5,21,6],
            170: [22,5.5,22,6],
            171: [20,7,20,7.5],#Game machine
            172: [21,7,21,7.5],
            173: [22,7,22,7.5],
            174: [11.5,18,11.5,19],#Slab
            175: [12.5,18,12.5,19],
            176: [13.5,19,14.5,19],
            177: [11.5,17,11.5,17],#Health mesure
            178: [12.5,17,12.5,17],
            179: [13.5,17,13.5,17],
            180: [19,9,19,9],#Weapon rack
            181: [19,10,19,10],#Stick
            182: [20,10,20,10],
            183: [21,10,21,10],
            184: [19,11,19,11],#Sniper
            185: [20,11,20,11],
            186: [21,11,21,11],
            187: [19,12,19,12],#Shotgun
            188: [20,12,20,12],
            189: [21,12,21,12],
            190: [18.5,18.5,19,19],#Shop shelf
            191: [13.5,27,17.5,27],#church benck
            192: [11.5,26.5,12.5,27],#church piew
            193: [13.5,25.5,13.5,25.5],#jesus
            194: [14.5,25.5,14.5,25.5],#chandelere
            195: [18,22.5,19,24.5],#Small house
            196: [20,22.5,21,24.5],#closed
            197: [13,28.5,13,29.5],#School desk
            198: [14,28.5,14,29.5],
            199: [15,29,16,29.5],
            200: [9,5,9,6],#bench press
            201: [10,5,10,6],
            202: [11,6,12,6],
            203: [20,0,21,0],#Black board
            204: [22,0,22,0],#Boom box
            205: [23,0,23,0],#pilar
            206: [24,0,24,0],#chess
            207: [25,0,25,0],#comode
            208: [26,0,26,0],#crib
            209: [27,0,27,0],#summer chair
            210: [23,1,23,2],#painting
            211: [30,1,30,2],#class board
            212: [22,21,22,21.5],#Weapon locker
            213: [23,21,22.5,22],#Lamp
            214: [24,1,26,2],#Workbench
            215: [27,26,29,26.5],#
            216: [27,27.5,29,28],#
            217: [25,8,25,9],#squeleton
            218: [20,1,22,2],#shop shelf
            219: [23.5,21,25.5,21],#shop table
            220: [28,1,29,2],#Weights rack
            221: [24,25,24,26],#running pad
            222: [29,21,29,22],#punching ball
            223: [22,27,23,29],#ping pong
            224: [25,10,27,10],#red bench
            225: [28,10,30,11],#red table
            226: [28,12,30,12.5],#park bench
            227: [27,23,29,25],#big park bench
            228: [28,0,28,0],#dog food
            229: [29,0,29,0],#mat
            230: [27,1,27,2],#dog crate
            231: [20,3,23,4.5],#bleachers
            232: [24,3,26,3.5],#Computer
            233: [27,3,29,4.5],#Computer 2
            234: [26,8,26,9],#coat hanger
            235: [27,8,27,9],#old computer
            236: [28,8,28,9],#fan
            237: [29,8,29,9],#baril
            238: [31,8,31,8],#heater
            239: [25,11,26,11.5],#small coffe table
            240: [25,13,26,16],#street lamp
            241: [26.5,21,26.5,22],#med cabinet
            242: [23.5,22,23.5,22],#mat child
            243: [25,25,25,26],#tires
            244: [31,0,31,1],#wind meter
            245: [32,0,32,1],#sea meter
            246: [33,0,33,1],#sea boue
            247: [34,0,34,0],#bite amarage
            248: [35,0,35,0],#statue 1
            249: [36,0,36,0],#statue2
            250: [37,0,37,0],#drawer
            251: [38,0,38,0],#barrel
            252: [30,0,30,0],#barb wire
            253: [35,1,35,1],#flamingo
            254: [36,1,36,1],#can machine
            255: [37,1,37,1],#plant 1
            256: [35,2,35,2],#cacti
            257: [36,2,36,2],#grave
            258: [37,2,37,2],#yoga mat
            259: [35,3,36,3],#red sofa
            260: [37,3,37,3],#red sofa chair
            261: [0,11,1,11.5],#small sink
            262: [2,11,3,11.5],
            263: [4,11,4,12],
            264: [0,13,1,13.5],#white table
            265: [3,13,3,14],
            266: [2,13,2,13.5],#small white table
            267: [5,17,5.5,17],#Big TV
            268: [6.5,17,7,17],
            269: [8,16.5,8,17],
            270: [15,5,16,5],#Sofa brown
            271: [17,5,18,5],
            272: [19,4,19,5],
            273: [15,0,17,1],#medium white table
            274: [18,0,19,2],
            275: [13,2,15,3],#big white table
            276: [16,2,17,4],
            277: [41,0,43,1],#medium wood table
            278: [44,0,45,2],
            279: [39,2,41,3],#big wood table
            280: [42,2,43,4],
            281: [26,8,26,9],#coathanger
            282: [28,8,28,9],#fan
            283: [37,6,37,7],#water tower
            #218: [23,21,22.5,22],#
            #219: [23,21,22.5,22],#
            #251: [38,0,38,0],#barrel
        }
        if num in mapDict2 :
            coord = mapDict2[num]
            image = self.aggSprite(coord,flip)
            if rawImage :
                return image
            else :
                tkimg = ImageTk.PhotoImage(image)
                if not flip :
                    self.spriteList[num] = tkimg
                else :
                    self.spriteListFlip[num] = tkimg
                return tkimg
        else :
            return self.spriteList[0]

    
    def addMetadataToObjList(self,objList):
        doorList = [[1,[-1,0]],[2,[0,1]],[3,[1,0]],[4,[0,-1]],[5,[-1,0]],[6,[0,1]],[7,[-1,0]],[8,[0,1]]]
        cabientList = [[149,[True,152]],[150,[True,153]],[151,[True,154]],[152,[False,149]],[153,[False,150]],[154,[False,151]]]
        for j in range(len(objList)) :
            objList[j].append(["none"])
            for i in range(len(doorList)) :
                if objList[j][0] == doorList[i][0]:
                    objList[j][3]=["door",doorList[i][1],0,0,True,objList[j][1],objList[j][2]]#Obj type, direction open, unit open, counter animation, unlocked
            for i in range(len(cabientList)) :
                if objList[j][0] == cabientList[i][0]:
                    objList[j][3]=["cabinet",cabientList[i][1][0],cabientList[i][1][1],True,0]
        return objList
    
       
    def getCarSprite(self,num,angle=0,angleNum=10,flip=False) :
        angleList = []
        for i in range(angleNum+1) :
            angleList.append(int(math.ceil((i/angleNum)*360)))
        mapDict = {
            0: [0,1,2,8],#Cars
            1: [3,0,5,8],
            2: [6,3,8,8],
            3: [9,3,11,8],
            4: [12,3,14,8],
            5: [15,2,17,8],
            6: [18,3,20,8],
            7: [21,2,23,8],
            8: [0,9,8,13],#Boats
            9: [9,9,17,13],
            10: [18,9,26,13],
            11: [0,14,8,18],
            12: [0,19,8,22],#Heli
            13: [9,19,17,22],
            14: [18,19,26,22],
            15: [0,23,8,26],
            16: [9,23,17,26],
            }
        if num in mapDict :
            coord = mapDict[num]
            image = self.aggSprite(coord,flip)
            sizeX, sizeY = image.size
            image2 = self.angleImage(image,angleList[angle],[sizeX,sizeY])#
            image3 = ImageTk.PhotoImage(image2)
            return image3
        return None
    
    def getCarSize(self,carNum) :
        mapDict = {
            0: [0,1,2,8],
            1: [3,0,5,8],
            2: [6,3,8,8],
            3: [9,3,11,8],
            4: [12,3,14,8],
            5: [15,2,17,8],
            6: [18,3,20,8],
            7: [21,2,23,8],
            8: [0,9,8,13],#Boats
            9: [9,9,17,13],
            10: [18,9,26,13],
            11: [0,14,8,18],
            12: [0,19,8,22],#Heli
            13: [9,19,17,22],
            14: [18,19,26,22],
            15: [0,23,8,26],
            16: [9,23,17,26],
            }
        if carNum in mapDict :
            coord = mapDict[carNum]
            image = self.aggSprite(coord,False)
            sizeX, sizeY = image.size
            return sizeX, sizeY
        else :
            return 0,0
        
    def aggSprite(self,point,flip=False):
        size = [(point[2]*2)-(point[0]*2)+2,(point[3]*2)-(point[1]*2)+2]
        image = Image.new("RGBA", (int(size[0]*self.step_x/2), int(size[1]*self.step_y/2))) 
        for x in range(int(point[0]*2),int(point[2]*2)+2) :
            for y in range(int(point[1]*2),int(point[3]*2)+2) :
                image.paste(self.imageMat[x][y],(int((x-(point[0]*2))*self.step_x/2),int((y-(point[1]*2))*self.step_y/2)),self.imageMat[x][y])
        if flip :
            image = image.transpose(Image.FLIP_LEFT_RIGHT)#FLIP_TOP_BOTTOM)
        return image
    
    def angleImage(self,image,angle,size=[300,300],border=20) :
        maxSize = max(size[0],size[1])+border
        imageret = Image.new("RGBA",(maxSize,maxSize)) 
        image2 = image.copy()
        imageret.paste(image2,(int((maxSize/2)-(size[0]/2)),int((maxSize/2)-(size[1]/2))),image2)
        return imageret.rotate(angle,3)