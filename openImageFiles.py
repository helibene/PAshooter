# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:03:01 2023

@author: Alexandre
"""

from PIL import ImageTk,Image,ImageOps
import numpy as np
import math
import terrain_builder as tb
import object_builder as ob

class openImageFiles :
     def __init__(self):
         pass

def masterOpen(w) :
    openSheetList(w)
    openMapList(w)    
    generateNewMap(w,w.generate_new_map)       
    objectInst = ob.object_builder(w.sheetList[0])
    objectCarInst = ob.object_builder(w.sheetList[5])
    openBackgroundList(w)
    return objectInst, objectCarInst

def masterLoad(w) :
    loadImageCharacterList(w,w.sheetList[2])
    loadImageHandObjList(w,w.sheetList[2])
    loadImageMenuList(w,w.menuList)
    loadImageAnimationList(w,w.sheetList[2])
    

def masterSaveObjImage(w) :
    saveObjList(w,w.objList,w.mapInstance)
    openObjMap(w,w.mapInstance)
        
def generateNewMap(w,generate=False) :
    splitBool = w.splitMapImage!=[0,0]
    if generate :
        w.terrain = tb.terrain_builder(w.sheetList[4],w.sheetList[3],True,int(w.jpegQuality*95))
        w.terrain.mapFileToImageNat(w.mapList[0],w.rootPath+w.mapFolder+w.mapTextureFolder,w.rootPath+w.mapFolder+w.mapCollisionFolder,splitBool)
        if splitBool :
            mapSetList,backSetList = w.terrain.splitImage(w.rootPath+w.mapFolder+w.mapRawFolder,w.mapList[0][1],"png",w.splitMapImage[0],w.splitMapImage[1],w.mapRawSplitFolder)
            w.backList.extend(backSetList)
            w.mapList2=mapSetList
            print("Gen splited files :",len(w.mapList2))
            openMapList2(w)
            for i in range(len(w.mapList2)):
                w.terrain.mapFileToImageNat(w.mapList2[i],w.rootPath+w.mapFolder+w.mapTextureFolder,w.rootPath+w.mapFolder+w.mapCollisionFolder)
    else :
        if splitBool :
            w.terrain = tb.terrain_builder(w.sheetList[4],w.sheetList[3],True,int(w.jpegQuality*95))
            mapSetList,backSetList = w.terrain.splitImage(w.rootPath+w.mapFolder+w.mapRawFolder,w.mapList[0][1],"png",w.splitMapImage[0],w.splitMapImage[1],w.mapRawSplitFolder,True)
            print("Generating terain texture files :",len(mapSetList))
            w.backList.extend(backSetList)
            
def openSheetList(w) :
    for sheetNum in range(len(w.sheetList)) :
        img = Image.open(w.rootPath+w.textureFolder+w.sheetList[sheetNum][0]).convert("RGBA")
        w.sheetList[sheetNum][0] = img
        
def openObjMap(w,num) :
    w.objMapImageRaw = Image.open(w.rootPath+w.mapFolder+w.mapObjectFolder+"map"+str(num)+"_obj.png").convert("RGBA")
    w.objMapImage = ImageTk.PhotoImage(w.objMapImageRaw)
    
def saveObjList(w,objMat,num=0):
    mapSizeX = w.backList[0][1]
    mapSizeY = w.backList[0][2]
    mapImage = Image.new("RGBA", (mapSizeX, mapSizeY)) 
    for obj in objMat :
        if obj[3][0]=='none':
            img = w.object.getSprite(obj[0],True)
            mapImage.paste(img,(int(obj[1]*32),int(obj[2]*32)),img)
    mapImage.save(w.rootPath+w.mapFolder+w.mapObjectFolder+"map"+str(num)+"_obj.png","PNG")
    
    
def openMapList(w) :
    for mapNum in range(len(w.mapList)) :
        img = Image.open(w.rootPath+w.mapFolder+w.mapRawFolder+w.mapList[mapNum][0]).convert("RGB")
        w.mapList[mapNum][0] = img
        sizeX, sizeY = img.size
        w.mapList[mapNum].append(sizeX)
        w.mapList[mapNum].append(sizeY)

def openMapList2(w) :
    for mapNum in range(len(w.mapList2)) :
        img = Image.open(w.rootPath+w.mapFolder+w.mapRawFolder+w.mapList2[mapNum][0]).convert("RGB")
        w.mapList2[mapNum][0] = img
        sizeX, sizeY = img.size
        w.mapList2[mapNum].append(sizeX)
        w.mapList2[mapNum].append(sizeY)

def openBackgroundList(w) :
    splitBool = w.splitMapImage!=[0,0]
    print("Opening terain texture files :",len(w.backList))
    for backNum in range(len(w.backList)) :
        if not(backNum==0 and splitBool) :
            imgback = Image.open(w.rootPath+w.mapFolder+w.mapTextureFolder+w.backList[backNum][0]).convert("RGB")
            w.backList[backNum][0] = ImageTk.PhotoImage(imgback)
        imgCol = Image.open(w.rootPath+w.mapFolder+w.mapCollisionFolder+w.backList[backNum][5]).convert("RGB")
        sizeX, sizeY = imgCol.size
        w.backList[backNum][1] = sizeX*w.terrainTileSize
        w.backList[backNum][2] = sizeY*w.terrainTileSize
        w.backList[backNum][3] = sizeX
        w.backList[backNum][4] = sizeY
        colliMat = [[False for x in range(w.backList[backNum][4])] for y in range(w.backList[backNum][3])] 
        seaMat = [[False for x in range(w.backList[backNum][4])] for y in range(w.backList[backNum][3])] 
        colorMat = np.array(list(imgCol.getdata())).reshape((w.backList[backNum][3], w.backList[backNum][4], 3))
        for x in range(w.backList[backNum][3]-1) :
            for y in range(w.backList[backNum][4]-1) :
                if colorMat[x][y][0]==0:
                    colliMat[x][y] = True
                    if colorMat[x][y][2]==255:
                        seaMat[x][y] = True
        w.backList[backNum][5] = colliMat
        w.backList[backNum][6] = seaMat

def imageToMask(w,img,transparentCol=(0,0,0,0),fillCol=(255, 0, 0, 100)) :
    data = img.getdata()
    newData = []
    for item in data:
        if item[0] > 0 or item[1] > 0 or item[2] > 0:
            newData.append(fillCol)
        else:
            newData.append(transparentCol)
    img.putdata(newData)
    return img

def fuseTextureAndObj(w) :
    for backNum in range(len(w.backList)) :
        imgback = Image.open(w.rootPath+w.mapFolder+w.mapTextureFolder+w.backList[backNum][0]).convert("RGB")

def loadImageCharacterList(w,characterSheetSettings) :
    for j in range(len(w.chara_list)) :
        for i in [0,1,2,-2,3] :
            x,y = w.caracterSelection(w.chara_list[j].spriteNum,abs(i))
            img = characterSheetSettings[0]
            step_x = (characterSheetSettings[1]/characterSheetSettings[3])
            step_y = (characterSheetSettings[2]/characterSheetSettings[4])
            box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
            img = img.crop(box)
            if i == 3 :
                imgcop = img.copy()
                mask = imageToMask(w,imgcop)
                img = Image.alpha_composite(img,mask)
            if i<0:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img2 = ImageTk.PhotoImage(img.resize((int(step_x*w.zoom),int(step_y*w.zoom)), resample=w.resampleType))#
            
            w.chara_list[j].spriteList.append(img2)
        w.chara_list[j].setSpriteSize()
        
def loadImageHandObjList(w,characterSheetSettings,mirror=False) :
    for j in range(len(w.handObjListClass)) :
        x,y = w.handObjSelection(w.handObjListClass[j].spriteNum)
        img = characterSheetSettings[0]
        step_x = (characterSheetSettings[1]/characterSheetSettings[3])
        step_y = (characterSheetSettings[2]/characterSheetSettings[4])
        box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
        img = img.crop(box)
        if mirror:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        imageSmall = img.resize((int(step_x*w.zoomHandObj),int(step_y*w.zoomHandObj)), resample=w.resampleType)
        img2 = ImageTk.PhotoImage(imageSmall)
        img3 = ImageTk.PhotoImage(img)
        img4 = ImageTk.PhotoImage(imageSmall.rotate(-90))
        w.handObjListClass[j].spriteList.append(img2)
        w.handObjListClass[j].spriteList.append(img3)
        w.handObjListClass[j].spriteList.append(img4)


def loadImageMenuList(w,menuSheetSettings,mirror=False) :
    for coord in range(1,8) :
        img = Image.open(w.rootPath+w.textureFolder+menuSheetSettings[0][0]).convert("RGBA")
        box = (menuSheetSettings[0][coord])
        img = img.crop(box)
        if coord==5 :
            w.menuImageList.append(img)
        else :
            img2 = ImageTk.PhotoImage(img)
            w.menuImageList.append(img2)
            
def loadImageAnimationList(w,characterSheetSettings):
    for i in range(1) : 
        x,y = w.animationSelection(i)
        img = characterSheetSettings[0]
        step_x = (characterSheetSettings[1]/characterSheetSettings[3])
        step_y = (characterSheetSettings[2]/characterSheetSettings[4])
        box = ([math.ceil(x*step_x),math.ceil(y*step_y),int((x+1)*step_x),int((y+1)*step_y)])
        img = img.crop(box)
        img2 = ImageTk.PhotoImage(img)#
        w.animationList.append(img2)