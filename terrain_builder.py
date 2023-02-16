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
        self.jpegQuality = 20
        self.step_x = int(self.terrainSheetSetting[1]/self.terrainSheetSetting[3])
        self.step_y = int(self.terrainSheetSetting[2]/self.terrainSheetSetting[4])
        self.img = self.terrainSheetSetting[0]
        self.waterColor = 9
        if self.printLog :
            print("TB : spliting sprite sheet")
        for x in range(self.terrainSheetSetting[3]) :
            for y in range(self.terrainSheetSetting[4]) :
                box = ([int(x*self.step_x),int(y*self.step_y),int((x+1)*self.step_x),int((y+1)*self.step_y)])
                self.imgCrop = self.img.crop(box)
                self.imageMat[x][y] = ImageTk.PhotoImage(self.imgCrop)
                self.imageMat2[x][y] = self.imgCrop


    def mapFileToImageNat(self,mapSetting,path,onlyCol=False) :
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
        if not onlyCol :
            image = Image.new("RGB", (mapSetting[2]*self.step_x, mapSetting[3]*self.step_y)) 
        imageCol = Image.new("RGB", (mapSetting[2], mapSetting[3]),color='white') 
        for x in range(mapSetting[2]) :
            for y in range(mapSetting[3]) :
                if not onlyCol :
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
        if not onlyCol :
            for x in range(1,mapSetting[2]-1) :
                for y in range(1,mapSetting[3]-1) :
                    if colorMat[y][x][0] not in [9,10,11] :
                        tileX = 0
                        tileY = 0
                        colorMatSmall = [[colorMat[y+y2][x+x2][0] for x2 in range(-1,2)] for y2 in range(-1,2)]
                        if self.seaAngle(colorMatSmall,[[2,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,0,0)
                        if self.seaAngle(colorMatSmall,[[0,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,0,1)
                        if self.seaAngle(colorMatSmall,[[0,0]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,0,2)
                        if self.seaAngle(colorMatSmall,[[2,0]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,0,3)
                        if self.seaAngle(colorMatSmall,[[1,2]],[[0,2],[2,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,1,0)
                        if self.seaAngle(colorMatSmall,[[0,1]],[[0,0],[0,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,1,1)
                        if self.seaAngle(colorMatSmall,[[1,0]],[[0,0],[2,0]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,1,2)
                        if self.seaAngle(colorMatSmall,[[2,1]],[[2,0],[2,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,1,3)
                        if self.seaAngle(colorMatSmall,[[1,2],[2,1]],[[2,2],[0,2],[2,0]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,2,0)
                        if self.seaAngle(colorMatSmall,[[0,1],[1,2]],[[0,2],[0,0],[2,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,2,1)
                        if self.seaAngle(colorMatSmall,[[1,0],[0,1]],[[0,0],[0,2],[2,0]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,2,2)
                        if self.seaAngle(colorMatSmall,[[1,0],[2,1]],[[2,0],[0,0],[2,2]]) :
                            tileX,tileY=seaMapping(self.waterColor-9,2,3)
                            
                        if tileX!=0 and tileY!=0 :
                            image.paste(self.imageMat2[tileX][tileY],(int(x*self.step_x),int(y*self.step_y)),self.imageMat2[tileX][tileY])

                    
        
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
            for x in range(2,int(mapSetting[2]/div)) :
                for y in range(2,int(mapSetting[3]/div)) :
                    redVal = colorMat[y*div][x*div][0]
                    greenVal = colorMat[y*div][x*div][1]
                    freq = float(greenVal/50)  
                    if random.random()<(freq/10) and redVal<9:
                        img = treeList[redVal]
                        randVal = random.random()
                        maxSizeChangePct = 0.25
                        img = img.resize((int(self.step_x*2+(self.step_x*2*maxSizeChangePct)*randVal),int(self.step_y*2+(self.step_y*2*maxSizeChangePct)*randVal)))
                        image.paste(img,(int(x*div*self.step_x-self.step_x/2),int(y*div*self.step_y-self.step_y)),img)
        if not onlyCol :
            image.save(path+mapSetting[1]+"_tex."+self.imageFormat,self.imageFormat.upper(), dpi=(10, 10),quality=self.jpegQuality)
        imageCol.save(path+mapSetting[1]+"_col.png","PNG")
    
    
    def splitImage(self,imageRoot,imageFilename,fileFormat,splitNumX,splitNumY,justBackSetList=False) :
        img = Image.open(imageRoot+imageFilename+"."+fileFormat).convert("RGB")
        sizeX,sizeY = img.size
        stepX = int(sizeX/splitNumX)
        stepY = int(sizeY/splitNumY)
        mapSetList = []
        backSetList = []
        for x in range(splitNumX) :
            for y in range(splitNumY) :
                if not justBackSetList :
                    box = (int(x*stepX),int(y*stepY),int((x+1)*stepX),int((y+1)*stepY))
                    imgLoop = img.copy()
                    imgLoop = imgLoop.crop(box)
                if x<10 :
                    strx="0"+str(x)
                else :
                    strx=str(x)
                if y<10 :
                    stry="0"+str(y)
                else :
                    stry=str(y)
                if not justBackSetList :
                    imgLoop.save(imageRoot+imageFilename+"_"+strx+"_"+stry+"."+fileFormat)
                    mapSetList.append([imageFilename+"_"+strx+"_"+stry+".png",imageFilename+"_"+strx+"_"+stry])
                backSetList.append([imageFilename+"_"+strx+"_"+stry+"_tex.jpeg",0,0,0,0,imageFilename+"_"+strx+"_"+stry+"_col.png",0,0,x*stepX,y*stepY])
        return mapSetList,backSetList
    
    def aggSprite(self,point,flip=False):
        size = [point[2]-point[0],point[3]-point[1]]
        image = Image.new("RGBA", (int(size[0]*self.step_x), int(size[1]*self.step_y))) 
        for x in range(int(point[0]),int(point[2])) :
            for y in range(int(point[1]),int(point[3])) :
                image.paste(self.imageMat2[x][y],(int((x-(point[0]))*self.step_x),int((y-(point[1]))*self.step_y)),self.imageMat2[x][y])
        if flip :
            image = image.transpose(Image.FLIP_LEFT_RIGHT)#FLIP_TOP_BOTTOM)
        return image

    def seaAngle(self,tileMat,onlyList,ignoreList=[]) :
        return_count = 0
        waterColor = 9
        for x in range(3) :
            for y in range(3) :
                if not(x==1 and y==1) :
                    if [x,y] in ignoreList :
                        return_count = return_count + 1
                    else :
                        if [x,y] in onlyList :
                            if tileMat[y][x] in [9,10,11] :
                                waterColor = tileMat[y][x]
                                return_count = return_count + 1
                        else :
                            if tileMat[y][x] not in [9,10,11] :
                                return_count = return_count + 1
        
        if return_count == 8 :
            self.waterColor = waterColor
            return True
        else :
            return False
    
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
        elif redVal>54 :
            return [8+int((redVal-55)/2),17+(redVal-55)%2]
        else :
            return [5,5]
        
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

def seaMapping(waterColor,angleType,val) :
    colorDict = {
        0: [21,19],
        1: [21,23],
        2: [21,27]
    }
    angleDict = {
            0: [[0,0],[2,0],[2,2],[0,2]],
            1: [[1,0],[2,3],[1,2],[1,3]],
            2: [[2,1],[0,3],[1,1],[0,1]]
            }
    posX = 0
    posY = 0
    if waterColor in colorDict :
        coord = colorDict[waterColor]
        posX = coord[0]
        posY = coord[1]
        if angleType in angleDict :
            coordList = angleDict[angleType]
            if val<len(coordList) :
                coord = coordList[val]
                posX = posX + coord[0]
                posY = posY + coord[1]
    return [posX,posY]
    

            
def randPointRange(xstart,ystart,xrange,yrange):
    return [xstart+int(random.random()*xrange),ystart+int(random.random()*yrange)]
