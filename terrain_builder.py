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

        image.save(path+mapSetting[1]+"."+self.imageFormat,self.imageFormat.upper())
        imageCol.save(path+mapSetting[1]+"Collision.png","PNG")
        return image,imageCol
        

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
        9: randPointRange(15,6,2,2),
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
        100: [0+addPoint[0],0+addPoint[1]],
        101: [13+addPoint[0],0+addPoint[1]],
        102: [8+addPoint[0],8+addPoint[1]],
        103: [0+addPoint[0],12+addPoint[1]],
        104: [8+addPoint[0],12+addPoint[1]],
        105: [0+addPoint[0],16+addPoint[1]],
        106: [8+addPoint[0],16+addPoint[1]]
    }
    if redVal in mapDict :
        return mapDict[redVal]
    else :
        return [-1,-1]
    
    
def decoMapping(greenVal) :
    mapDict = {
        1: randPointRange(7,0,3,0),
        2: randPointRange(7,1,3,0),
        3: randPointRange(7,2,3,0),
        4: randPointRange(4,3,3,0),
        5: randPointRange(10,3,3,0),
        6: [10,0],
        7: [11,0],
        8: randPointRange(23,10,3,2),
        9: randPointRange(26,10,3,2),
        10: randPointRange(29,10,3,2),
        11: randPointRange(26,12,3,2),
        12: randPointRange(29,12,3,2),
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
