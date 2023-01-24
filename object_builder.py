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
        self.spriteList = [None for x in range(500)]
        for x in range(self.objSheetSetting[3]) :
            for y in range(self.objSheetSetting[4]) :
                box = ([int(x*self.step_x),int(y*self.step_y),int((x+1)*self.step_x),int((y+1)*self.step_y)])
                self.imgCrop = self.img.crop(box)
                self.imageMat2[x][y] = ImageTk.PhotoImage(self.imgCrop)
        for x in range(self.objSheetSetting[3]*2) :
            for y in range(self.objSheetSetting[4]*2) :
                box = ([int(x*self.step_x/2),int(y*self.step_y/2),math.ceil((x+1)*self.step_x/2),math.ceil((y+1)*self.step_y/2)])
                self.imgCrop = self.img.crop(box)
                self.imageMat[x][y] = self.imgCrop
       
        ##print("obj image mat :",sys.getsizeof(self.imageMat))
    
    def deleteSpriteMatrix(self) :
        del(self.imageMat)
        del(self.imageMat2)
        del(self.objSheetSetting)
        del(self.img)
        
    def getSprite(self,num) :
        num2 = num
        flip = False
        if num <0 :
            num = abs(num)
            num2 = num + 100
            flip = True
        if self.spriteList[num2]!=None :
            return self.spriteList[num2]
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
        }
        if num in mapDict :
            coord = mapDict[num]
            self.spriteList[num] = self.imageMat2[coord[0]][coord[1]]#.transpose(Image.FLIP_LEFT_RIGHT)
            return self.spriteList[num]
        
        mapDict2 = {
            100: [0,3,0,4],#Bed
            101: [1,3,1,4],
            102: [2,4,3,4],
            103: [0,28,1,29],#Trees
            104: [2,28,3,29],
            105: [4,28,5,29],
            106: [0,30,1,31],
            107: [2,30,3,31],
            108: [15,7.5,16,7.5],#Sofa
            109: [17,7.5,18,7.5],
            110: [19,6.5,19,7.5],
            111: [5,9,8.5,10],#Table
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
            123: [8.5,25,9.5,25.5],#Big table with plates
            124: [8.5,26.5,8.5,27],#desk
            125: [9.5,26.5,10.5,27],
            126: [16.5,24,17,26],
            127: [9,28,11,28.5],#Bath
            128: [0,7,1,8],#Stove
            129: [2,7,3,8],
            130: [4,7,4,8],
            131: [0,9,1,10],#Fridge
            132: [2,9,3,10],
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
            188: [20,10,20,12],
            189: [21,12,21,12],
        }
        if num in mapDict2 :
            coord = mapDict2[num]
            image = self.aggSprite(coord,flip)
            self.spriteList[num2] = ImageTk.PhotoImage(image)
            return self.spriteList[num2]
        return None
    
    def getCarSprite(self,num,angle=0) :
        flip=False
        num2 = num+300+angle*10
        angleList = []#[0,45,90,135,180,225,270,315]
        angleNum = 20
        for i in range(angleNum) :
            angleList.append(int((i/angleNum)*360))
        if self.spriteList[num2]!=None :
            return self.spriteList[num2]
        mapDict = {
            0: [1,0,2,7],
            1: [3,0,4,7],#Door
            2: [1,8,2,12],
            3: [3,8,4,12],
            4: [1,13.5,2,17],
            5: [3,13.5,4,17.5],
            }
        if num in mapDict :
            coord = mapDict[num]
            image = self.aggSprite(coord,flip)
            for i in range(len(angleList)) :
                image2 = self.angleImage(image,angleList[i])
                self.spriteList[num2+10*i] = ImageTk.PhotoImage(image2)
            #self.spriteList[num2] = ImageTk.PhotoImage(image)
            return self.spriteList[num2]
        return None
            
    def aggSprite(self,point,flip=False):
        size = [(point[2]*2)-(point[0]*2)+2,(point[3]*2)-(point[1]*2)+2]
        image = Image.new("RGBA", (int(size[0]*self.step_x/2), int(size[1]*self.step_y/2))) 
        for x in range(int(point[0]*2),int(point[2]*2)+2) :
            for y in range(int(point[1]*2),int(point[3]*2)+2) :
                image.paste(self.imageMat[x][y],(int((x-(point[0]*2))*self.step_x/2),int((y-(point[1]*2))*self.step_y/2)),self.imageMat[x][y])
        if flip :
            image = image.transpose(Image.FLIP_LEFT_RIGHT)#FLIP_TOP_BOTTOM)
        return image
    
    def angleImage(self,image,angle) :
        imageret = Image.new("RGBA",(300,300)) 
        image2 = image.copy()
        imageret.paste(image2,(150-38,0),image2)
        return imageret.rotate(angle)