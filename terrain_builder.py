# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:06:32 2023

@author: Alexandre
"""

import math
from PIL import ImageTk,Image,ImageColor
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


    def mapFileToImageNat(self,mapSetting,path) :
        if self.printLog :
            print("TB : generating map image")
        mapTemplate = mapSetting[0]
        treeList = []
        for i in range(9) :
            treeList.append(self.aggSprite([i*2,0,i*2+2,2]))
        blackpix = Image.new("RGB",(1,1),(0,0,0))
        seapix = Image.new("RGB",(1,1),(0,0,255))
        colorMat = numpy.array(list(mapTemplate.getdata())).reshape((mapSetting[2], mapSetting[3], 3))
        tileMat = [[[-1,-1] for x in range(mapSetting[3])] for y in range(mapSetting[2])] 
        image = Image.new("RGB", (mapSetting[2]*self.step_x, mapSetting[3]*self.step_y)) 
        imageCol = Image.new("RGB", (mapSetting[2], mapSetting[3]),color='white') 
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                redVal = colorMat[y][x][0]
                greenVal = colorMat[y][x][1]
                blueVal = colorMat[y][x][2]
                tileMat[x][y] = terrainMapping(redVal,greenVal,blueVal)
                x2,y2 = tileMat[x][y]
                image.paste(self.imageMat2[x2][y2],(int(x*self.step_x),int(y*self.step_y)))
                if colorMat[y][x][0]>=100 :
                    imageCol.paste(blackpix,(x,y))
                if colorMat[y][x][0] in [9,10,11] :
                    imageCol.paste(seapix,(x,y))
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
                #print("x:",x,"y:",y)
                image.paste(self.imageMat2[x][y],(int((x-(point[0]))*self.step_x),int((y-(point[1]))*self.step_y)),self.imageMat2[x][y])
        if flip :
            image = image.transpose(Image.FLIP_LEFT_RIGHT)#FLIP_TOP_BOTTOM)
        return image
                
    
def terrainMapping(redVal,greenVal,blueVal) :
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
