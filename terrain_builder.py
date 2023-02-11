# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:06:32 2023

@author: Alexandre
"""

import math
from PIL import ImageTk,Image 
import numpy 
import random
from tkinter import Canvas 

class terrain_builder :
    def __init__(self,terrainSheetSetting,black,printLog=False):
        self.terrainSheetSetting = terrainSheetSetting
        self.black = black[0]
        self.imageMat = [[None for x in range(self.terrainSheetSetting[4])] for y in range(self.terrainSheetSetting[3])] 
        self.imageMat2 = [[None for x in range(self.terrainSheetSetting[4])] for y in range(self.terrainSheetSetting[3])] 
        self.printLog = printLog
        self.imageFormat = "jpeg"
        self.step_x = int(self.terrainSheetSetting[1]/self.terrainSheetSetting[3])
        self.step_y = int(self.terrainSheetSetting[2]/self.terrainSheetSetting[4])
        self.img = self.terrainSheetSetting[0]
        if self.printLog :
            print("TB : spliting sprite sheet")
        for x in range(self.terrainSheetSetting[3]) :
            for y in range(self.terrainSheetSetting[4]) :
                box = ([int(x*self.step_x),int(y*self.step_y),int((x+1)*self.step_x),int((y+1)*self.step_y)])
                self.imgCrop = self.img.crop(box)
                self.imageMat[x][y] = ImageTk.PhotoImage(self.imgCrop)
                self.imageMat2[x][y] = self.imgCrop

    def mapFileToImage(self,mapSetting,path) :
        if self.printLog :
            print("TB : generating map image")
        mapTemplate = mapSetting[0]
        colorMat = numpy.array(list(mapTemplate.getdata())).reshape((mapSetting[2], mapSetting[3], 3))
        tileMat = [[[-1,-1] for x in range(mapSetting[3])] for y in range(mapSetting[2])] 
        tileMatDeco = [[[-1,-1] for x in range(mapSetting[3])] for y in range(mapSetting[2])] 
        tileMatColision = [[False for x in range(mapSetting[3])] for y in range(mapSetting[2])] 
        image = Image.new("RGB", (mapSetting[2]*self.step_x, mapSetting[3]*self.step_y)) 
        imageCol = Image.new("RGB", (mapSetting[2], mapSetting[3]),color='white') 
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                redVal = colorMat[y][x][0]
                greenVal = colorMat[y][x][1]
                if redVal>=100 :
                    tileMatColision[x][y] = True
                    tileMat[x][y] = terrainMapping(redVal,wallMapping(greenVal))
                else :
                    tileMat[x][y] = terrainMapping(redVal)
                    if redVal==18 :
                        tileMatColision[x][y] = True
                if redVal<100 and greenVal!=0:
                    tileMatDeco[x][y] = decoMapping(greenVal)
                    
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                x2,y2 = tileMat[x][y]
                x3,y3 = tileMatDeco[x][y]
                bool1 = tileMatColision[x][y]
                image.paste(self.imageMat2[x2][y2],(int(x*self.step_x),int(y*self.step_y)))
                if x3!=-1 and y3!=-1 :
                    image.paste(self.imageMat2[x3][y3],(int(x*self.step_x),int(y*self.step_y)),self.imageMat2[x3][y3])
                if bool1 :
                    imageCol.paste(self.black,(x,y))

        image.save(path+mapSetting[1]+"_tex."+self.imageFormat,self.imageFormat.upper())
        imageCol.save(path+mapSetting[1]+"_col.png","PNG")
        return image,imageCol

    def mapFileToImageNat(self,mapSetting,path) :
        if self.printLog :
            print("TB : generating map image")
        mapTemplate = mapSetting[0]
        treeList = []
        for i in range(9) :
            print("tree num",i)
            treeList.append(self.aggSprite([i*2,0,i*2+2,2]))
            
        colorMat = numpy.array(list(mapTemplate.getdata())).reshape((mapSetting[2], mapSetting[3], 3))
        tileMat = [[[-1,-1] for x in range(mapSetting[3])] for y in range(mapSetting[2])] 
        image = Image.new("RGB", (mapSetting[2]*self.step_x, mapSetting[3]*self.step_y)) 
        imageCol = Image.new("RGB", (mapSetting[2], mapSetting[3]),color='white') 
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                redVal = colorMat[y][x][0]
                greenVal = colorMat[y][x][1]
                blueVal = colorMat[y][x][2]
                tileMat[x][y] = terrainMapping2(redVal,greenVal,blueVal)
                x2,y2 = tileMat[x][y]
                image.paste(self.imageMat2[x2][y2],(int(x*self.step_x),int(y*self.step_y)))
                if colorMat[y][x][0]>=100 :
                    imageCol.paste(self.black,(x,y))
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                redVal = colorMat[y][x][0]
                if redVal<9 :
                    greenVal = colorMat[y][x][1]
                    freq = float(greenVal/25)
                    x3,y3 = randPointRange(redVal*2,2,2,3)
                    if random.random()<(freq/10) :
                        img = self.imageMat2[x3][y3]
                        randVal = (random.random()-0.5)*2
                        maxSizeChangePct = 0.2
                        img = img.resize((int(self.step_x+(self.step_x*maxSizeChangePct)*randVal),int(self.step_y+(self.step_y*maxSizeChangePct)*randVal)))
                        image.paste(img,(int(x*self.step_x),int(y*self.step_y)),img)
        div = 2
        for x in range(int(mapSetting[2]/div)) :
            for y in range(int(mapSetting[3]/div)) :
                redVal = colorMat[y*div][x*div][0]
                greenVal = colorMat[y*div][x*div][1]
                freq = float(greenVal/50)  
                if random.random()<(freq/10) and redVal<9:
                    img = treeList[redVal]
                    randVal = random.random()
                    maxSizeChangePct = 0.25
                    img = img.resize((int(self.step_x*2+(self.step_x*2*maxSizeChangePct)*randVal),int(self.step_y*2+(self.step_y*2*maxSizeChangePct)*randVal)))
                    image.paste(img,(int(x*div*self.step_x-self.step_x/2),int(y*div*self.step_y-self.step_y)),img)
        image.save(path+mapSetting[1]+"_tex."+self.imageFormat,self.imageFormat.upper())
        imageCol.save(path+mapSetting[1]+"_col.png","PNG")
        
    def splitImage(imageRoot,imageFilename,fileFormat,splitNumX,splitNumY) :
        img = Image.open(imageRoot+imageFilename+"."+fileFormat).convert("RGB")
        sizeX,sizeY = img.size
        stepX = int(sizeX/splitNumX)
        stepY = int(sizeY/splitNumY)
        for x in range(splitNumX) :
            for y in range(splitNumY) :
                box = (int(x*stepX),int(y*stepY),int((x+1)*stepX),int((y+1)*stepY))
                imgLoop = img.copy()
                imgLoop.crop(box)
                if x<10 :
                    strx="0"+str(x)
                else :
                    strx=str(x)
                if y<10 :
                    stry="0"+str(y)
                else :
                    stry=str(y)
                imgLoop.save(imageRoot+imageFilename+"_"+strx+"_"+stry+"."+fileFormat)
    
    def aggSprite(self,point,flip=False):
        size = [point[2]-point[0],point[3]-point[1]]
        image = Image.new("RGBA", (int(size[0]*self.step_x), int(size[1]*self.step_y))) 
        for x in range(int(point[0]),int(point[2])) :
            for y in range(int(point[1]),int(point[3])) :
                print("x:",x,"y:",y)
                image.paste(self.imageMat2[x][y],(int((x-(point[0]))*self.step_x),int((y-(point[1]))*self.step_y)),self.imageMat2[x][y])
        if flip :
            image = image.transpose(Image.FLIP_LEFT_RIGHT)#FLIP_TOP_BOTTOM)
        return image
                
    #def newNature()
def terrainMapping(redVal,addPoint=[0,0]) :
    mapDict = {
        0: randPointRange(0,4,5,2),
        1: randPointRange(5,4,5,2),
        2: randPointRange(10,4,5,2),
        3: randPointRange(15,4,5,2),
        4: randPointRange(20,4,5,2),
        5: randPointRange(25,4,5,2),
        6: randPointRange(0,6,5,2),
        7: randPointRange(5,6,5,2),
        8: randPointRange(10,6,2,2),
        9: randPointRange(15,6,2,2),#Road
        10: randPointRange(20,6,5,2),
        11: randPointRange(25,6,5,2),
        12: randPointRange(15,8,5,2),
        13: randPointRange(25,8,5,2),
        14: randPointRange(30,6,2,2),
        15: randPointRange(20,8,2,2),
        16: randPointRange(20,12,2,4),
        17: randPointRange(22,12,2,4),
        18: randPointRange(0,26,6,0),
        19: randPointRange(0,29,6,0),
        20: randPointRange(17,6,1,2),#left
        21: randPointRange(18,6,1,2),#right
        22: randPointRange(19,6,1,2),#middle vert
        23: randPointRange(15,10,2,0),#up
        24: randPointRange(15,11,2,0),#down
        25: randPointRange(17,10,2,0),#middle hor
        26: randPointRange(13,6,1,2),#PAvement left
        27: randPointRange(14,6,1,2),#right
        28: randPointRange(19,10,2,0),#up
        29: randPointRange(19,11,2,0),#down
        30: randPointRange(22,8,0,0),
        31: randPointRange(22,9,0,0),
        100: [0+addPoint[0],0+addPoint[1]],
        101: [13+addPoint[0],0+addPoint[1]],
        102: [8+addPoint[0],8+addPoint[1]],
        103: [0+addPoint[0],12+addPoint[1]],
        104: [8+addPoint[0],12+addPoint[1]],
        105: [0+addPoint[0],16+addPoint[1]],
        106: [8+addPoint[0],16+addPoint[1]],
    }
    if redVal in mapDict :
        return mapDict[redVal]
    else :
        return [-1,-1]
    
def terrainMapping2(redVal,greenVal,blueVal) :
    if redVal<50 :
        return randPointRange(int((redVal%12)*2),5+int(redVal/12)*4,2,4)
    elif redVal<100 :
        if redVal==50 :
            return randPointRange(0,17,2,2)
        elif redVal==51 :
            return randPointRange(2,17,2,2)
        elif redVal==52 :
            return randPointRange(4,17,2,2)
        elif redVal==53 :
            return randPointRange(6,17,1,2)
        elif redVal==54 :
            return randPointRange(7,17,1,2)
        elif redVal==55 :
            return randPointRange(8,17,1,1)
        elif redVal==56 :
            return randPointRange(8,18,1,1)
        elif redVal==57 :
            return randPointRange(9,17,1,1)
        elif redVal==58 :
            return randPointRange(9,18,1,1)
        elif redVal==59 :
            return randPointRange(10,17,1,1)
        elif redVal==60 :
            return randPointRange(10,18,1,1)
        elif redVal==61 :
            return randPointRange(11,17,1,1)
        elif redVal==62 :
            return randPointRange(11,18,1,1)
        else :
            return [22,0]
        
    else :
        return [0+((redVal-100)%3)*7+wallMapping(greenVal)[0],19+int((redVal-100)/3)*4+wallMapping(greenVal)[1]] 
    
def decoMapping(greenVal) :
    mapDict = {
        1: randPointRange(4,3,3,0),#Grass
        2: [11,0],
        3: randPointRange(23,10,3,2),
        4: randPointRange(29,10,3,2),
        
        5: [10,0],#Flower
        6: [12,0],
        
        7: randPointRange(26,10,3,2),#Rocks
        8: randPointRange(26,12,3,2),
        9: randPointRange(29,13,3,0),
        
        10: randPointRange(7,0,3,0),#Dust
        11: randPointRange(7,1,3,0),
        12: randPointRange(10,3,3,0),
        13: randPointRange(7,2,3,0),
        
        14: [9,3]#Hole
    }
    if greenVal in mapDict :
        return mapDict[greenVal]
    else :
        return [-1,-1]
    
def wallMapping(val) :
    posX = 0
    posY = 0
    if val>6 :
        val = val-7
        posY = posY+1
    if val>6 :
        val = val-7
        posY = posY+1
    if val>6 :
        val = val-7
        posY = posY+1
    if val==0 and posY==3:
        posX =2
    elif val==1 and posY==3:
        posX =3
    else :
        posX = val
    return [posX,posY]

def randPointRange(xstart,ystart,xrange,yrange):
    return [xstart+int(random.random()*xrange),ystart+int(random.random()*yrange)]
