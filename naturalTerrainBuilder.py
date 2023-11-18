# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:11:08 2023

@author: Alexandre
"""
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np
from scipy.spatial import Voronoi
from skimage.draw import polygon
from PIL import Image
from noise import snoise3
import json 
from PIL import ImageColor,Image
from skimage import exposure
import random
import scipy.ndimage as ndimage
from numpy import savez_compressed
from numpy import load
from numpy import savetxt
from numpy import loadtxt
import math

class naturalTerrainBuilder :
    def __init__(self,instructions):
        self.width = instructions["MapSize"][0]
        self.height = instructions["MapSize"][1]
        #   self.mainFolder = "C:/Users/Alexandre/Desktop/PAshooter/terrain"
        self.mainFolder = "C:/Users/Alexandre/Desktop/terrainBuilder"
        self.inputFolder = "/map_input"
        self.outputFolder = "/map_output"
        self.mapIndex = 0
        self.totalBiomeNumber = 3
        self.mainMap = [[[[0,0] for z in range(self.totalBiomeNumber)] for y in range(self.height)] for x in range(self.width)]
        self.mainMapNp = np.zeros((self.width, self.height,self.totalBiomeNumber,2))
        biomejsonRaw = openJson(self.mainFolder+self.inputFolder,"addResources4","json")
        getAllSpriteNames(biomejsonRaw)
        quit()
        self.biomeStatList = biomejsonRaw["BiomeStats"]
        self.biomeColorMat,self.biomeIndexMat = openBiomeImage(self.mainFolder+self.inputFolder)
        self.stepByStep()
        #self.testModule()
        pass
        
    def testModule(self) :
        size = 150
        height1 = genPerl((size,size),scale=10,octaves=1)
        height2 = genPerl((size,size),scale=5,octaves=1)
        height3 = genPerl((size,size),scale=1,octaves=1)
        ret = superposeDFtoImage(height1,height2,height3)
        dispStatNumpyDf(ret,True,True,False)
        
    def stepByStep(self) :
        size = 1000
        n = 256
        map_seed = 762348
        np.random.seed(map_seed)
        # d1 = baseVornoi(5)
        # d2 = basePerl(5)
        # dispStatNumpyDf(d1)
        # dispStatNumpyDf(d2)
        # colorNumpyRGB(d1,d2,0,[255/5,255/5,255/5],True)
        # vor_map = voronoiSetup((size,size),500,False,10,True)
        # vor_map = bounderyCalculation((size,size),vor_map,False,0,True)
        # vor_map = voronoiSetup((size,size),500,True,3,True)
        # vor_map = bounderyCalculation((size,size),vor_map,True,20,True)
        # vor_map = segmentation((size,size),vor_map,10,True)
        # vor_map = layerSelection((size,size),vor_map,5,True)
        # d1 = baseVornoi(5)
        # dispStatNumpyDf(d1)
        # d2 = convertNumpyFloat((size,size),d1)
        # dispStatNumpyDf(d2)
        # fig = plt.figure(dpi=150, figsize=(10, 10))
        # plt.imshow(d2,cmap = 'rainbow')
        # d2 = d1/3
        # dispStatNumpyDf(d2)
        # vor_map = layerSelection((size,size),d1,1,True)
        # dispStatNumpyDf(vor_map)
        #perl_df = createMaskNumpyFloat((size,size),perl_df,[0,0.3])
        #print(max(vor_map))
        #height_map = noise_map(size, 2, 0, octaves=5, persistence=0.5, lacunarity=2,map_seed=map_seed)
        #height_map = segmentation((size,size),height_map,10,True)
        
        # vn = genVornoi((size,size),display=False)
        # vn2 = genVornoi((size,size),display=False)
        # vn3 = (vn+(1-vn2))/2

        
        # d1 = genPerl((size,size),display=True)
        # vn = genVornoi((size,size),1000,display=True)
        # sea,beach = generateSea((size,size),d1,[0,0.25],[0.25,0.3])
        # plot(sea+beach,"gray")
        # vn = generateTerain((size,size),vn,4,sea,beach)
        # vn2 = genVornoi((size,size),1000,display=True)
        # vn2 = segmentation((size,size),vn2,3)
        
        
        # dispStatNumpyDf(vn2,True)
        # colorBiomeMapStat(vn2,vn,self.biomeMat)
        # colorNumpyBiome(vn2,vn,self.biomeMat)
        
        #vn = genVornoi((size,size),2000,display=True)

        #colorNumpyBiome(vn2,vn,self.biomeMat)
        #dispStatNumpyDf(vn2)
        # sea = createMaskNumpyFloat((size,size),d1,[0,0.2])
        # beach = createMaskNumpyFloat((size,size),d1,[0.2,0.3])
        # terrain = segmentation((size,size),d1,5,[0.3,1],-1)
        # terrainMask = (terrain != -1).astype(int)
        
        # plot(sea)
        # plot(beach)
        # result = (sea+beach).astype(bool)##map(toBool, sea+beach)
        # dispStatNumpyDf(result)
        # plot(result,"gray")
        # dispStatNumpyDf(terrainMask)
        # plot(terrainMask)
        # total = sea*1+beach*2+(terrain+3)*terrainMask
        #dispStatNumpyDf(total)
        #plot(total)
        
        
        # df = genPerl((size,size),5,5,0.5,2,0,True)
        # df2 = genVornoi((size,size),2000,True,10,True,10,True)
        # df3 = mergeMap(df,df2)
        
        
        #df3 = segmentation((size,size),df3,10)
        # listAvg = average_cells(df2,df)
        # df3 = fill_cells(df2,listAvg)
        
        
        #print(listAvg)
        
        # df2 = histeq(df,0.5)
        # df2 = convertNumpyFloat((1000,1000),df2)
        
        # dispStatNumpyDf(df3,True,True,False)
        # id1 = getDataFromImg(openImage("C:/Users/Alexandre/Desktop/test_lua/test5/usefull_txt/biome1.png"),"RGB")
        # id2 = getDataFromImg(openImage("C:/Users/Alexandre/Desktop/test_lua/test5/usefull_txt/biome2.png"),"RGB")
        # id3 = selectColorFromMat(id2,0)
        # print(id3)
        # print(id1[5][5])
        
        #biomeColorMat,biomeIndexMat = openBiomeImage()
        #print(biomeIndexMat)
        #self.basicTerain((size,size),[10,10],self.biomeColorMat)
        
        
        # height1 = genPerl((size,size),scale=10,octaves=1)
        # height2 = genPerl((size,size),scale=5,octaves=1)
        # height3 = genPerl((size,size),scale=1,octaves=1)
        # ret = superposeDFtoImage(height1,height2,height3)
        # plt.imsave(self.mainFolder+self.outputFolder+"/testcacacaca.png", ret)
        
        
        self.generateMap((size,size))
        # for i1 in range(2,9) :
        #     for i2 in range(2,9) :
        #         for i3 in range(2,9) :
        #             for i4 in range(2,9) :
        #                 self.testList = [i1,i2,i3,i4]
        #                 self.basicTerain2((size,size),[10,10],self.biomeColorMat)
                        

    def generateMap(self,size=(100,100)) :
        biomeDfPath = self.mainFolder+self.outputFolder+"/"+str(self.mapIndex)+"_"
        numbeOfBiome = len(self.biomeStatList)
        biomeMapShape = (len(self.biomeIndexMat),len(self.biomeIndexMat[0]))
        seaMapSize = 1
        beachMapSize = 1
        seaLevel = 0.2
        beachFromSeaLevel = 0.1
        edgeBorderTileSize = 4
        edgeBorderSD = 1
        display = False
        
        #Numpy map gen
        height = genPerl(size,histeqAlpha=0.0,scale=8,octaves=2,display=display)
        tile = genPerl(size,histeqAlpha=0.1,scale=20,octaves=10,display=display)
        foliageDencity = genPerl(size,histeqAlpha=0.1,scale=12,octaves=10,display=display)
        humidity = genVornoi(size,200,display=display)
        temperature = genVornoi(size,150,display=display)
        
        sea,beach = generateSea(size,height,[0,seaLevel],[seaLevel,seaLevel+beachFromSeaLevel])
        
        if display :
            plot((sea+beach).astype(bool),"gray")
        
        humidityFit = generateTerainNoSB(size,humidity,biomeMapShape[0],sea,seaMapSize,beach,beachMapSize)
        temperatureFit = generateTerainDef(size,temperature,biomeMapShape[1])
        
        biomeColorDf = colorNumpyBiome(temperatureFit,humidityFit,self.biomeColorMat,display=display)
        biomeIndexDf = indexNumpyBiome(temperatureFit,humidityFit,self.biomeIndexMat,display=display)
        
        plt.imsave(biomeDfPath+'biomeColorDf.png', biomeColorDf)#Biome Color Map
        plt.imsave(biomeDfPath+'biomeIndexDf.png', biomeIndexDf)#Biome Index Map
        #print(biomeColorDf[100][100])
        #savez_compressed('data.npz', biomeColorDf)
        
        #savetxt('data.csv', biomeIndexDf, fmt='%1x')# delimiter=',')
        biomeSegementDf = getEdgeBlur(biomeIndexDf,edgeBorderTileSize,edgeBorderSD)
        foliageDencityNoEdge = biomeSegementDf*foliageDencity
        FrequencyBiomeTree = extractFrequencyBiome(size,biomeIndexDf,self.biomeStatList,"TreeFrequency")
        FrequencyBiomeFoliage = extractFrequencyBiome(size,biomeIndexDf,self.biomeStatList,"FoliageFrequency")
        NumberBiomeTile = extractFrequencyBiome(size,biomeIndexDf,self.biomeStatList,"TileName",True)
        NumberBiomeTree = extractFrequencyBiome(size,biomeIndexDf,self.biomeStatList,"TreeList",True)
        NumberBiomeFoliage = extractFrequencyBiome(size,biomeIndexDf,self.biomeStatList,"FoliageList",True)
        NumberBiomeTileIndex = (NumberBiomeTile*tile).astype(int)
        NumberBiomeTreeIndex = (NumberBiomeTree*tile)
        NumberBiomeFoliageIndex = (NumberBiomeFoliage*tile)
        if display:
            colorBiomeMapStat(temperatureFit,humidityFit,self.biomeColorMat.shape,True)
            dispStatNumpyDf(biomeSegementDf,True,True,False)
            dispStatNumpyDf(foliageDencityNoEdge,True,True,False)
            dispStatNumpyDf(FrequencyBiomeTree,True,True,True)
            dispStatNumpyDf(FrequencyBiomeFoliage,True,True,True)
            dispStatNumpyDf(NumberBiomeTile,True,True,True)
            dispStatNumpyDf(NumberBiomeTree,True,True,True)
            dispStatNumpyDf(NumberBiomeFoliage,True,True,True)

        #quit()
        #plt.imsave(biomeDfPath+'biomeSegementDf.png', biomeSegementDf)
        TreeDencityNoEdge = convertNumpyFloat(size,foliageDencityNoEdge * FrequencyBiomeTree)
        FoliageDencityNoEdge = convertNumpyFloat(size,foliageDencityNoEdge * FrequencyBiomeFoliage)
        if display:
            dispStatNumpyDf(TreeDencityNoEdge,True,True,False)
            dispStatNumpyDf(FoliageDencityNoEdge,True,True,False)
        treeDencityPoint = genPointsInBiome(size,TreeDencityNoEdge,0.05)
        foliageDencityPoint = genPointsInBiome(size,FoliageDencityNoEdge,0.1)
        #plt.scatter(*foliageDencityPoint.T, s=0.2)
        
        newMap = pointsToMap(size,treeDencityPoint,1)
        newMap = minPointDistanceDf(size,newMap,3)
        newMap = dfRoundUp(size,newMap * NumberBiomeTreeIndex)
        newMap2 = pointsToMap(size,foliageDencityPoint,1)
        newMap2 = minPointDistanceDf(size,newMap2,3)
        newMap2 = dfRoundUp(size,newMap2 * NumberBiomeFoliageIndex)
        if display:
            dispStatNumpyDf(newMap,True,True,True)
            dispStatNumpyDf(newMap2,True,True,True)
        plt.imsave(biomeDfPath+'pointTree.png', newMap)
        plt.imsave(biomeDfPath+'pointFoliage.png', newMap2)
        plt.imsave(biomeDfPath+'NumberBiomeTileIndex.png', NumberBiomeTileIndex)
        
        sa = mergeDfIntoImage(biomeIndexDf,(newMap+(newMap2*16)).astype(int),NumberBiomeTileIndex)
        plt.imsave(biomeDfPath+'point2.png', sa)
        
        
        #if display :
        #fig = plt.figure(dpi=300, figsize=(10, 10))
        #plt.scatter(*foliageDencityPoint.T, s=0.2)
        #plt.savefig(biomeDfPath+'saved_figure.png')
        #plt.imsave(biomeDfPath+'saved_figure.png', *foliageDencityPoint.T)
        #dispStatNumpyDf((NumberBiomeTile*tile).astype(int),True,True,True)

def getAllSpriteNames(biomejsonRaw=None) :
    BiomeStatsList = biomejsonRaw["BiomeStats"]
    TreeMapping = biomejsonRaw["TreeMapping"]
    allTileNames = []
    allTreeNames = []
    allFoliageNames = []
    allTreeDict = {}
    for biome in BiomeStatsList :
        for tileName in biome["TileName"] :
            allTileNames.append(tileName)
        for treeName in biome["TreeList"] :
            allTreeNames.append(treeName)
        for foliageName in biome["FoliageList"] :
            allFoliageNames.append(foliageName)
    allTileNames = list(dict.fromkeys(allTileNames))
    allTreeNames = list(dict.fromkeys(allTreeNames))
    allFoliageNames = list(dict.fromkeys(allFoliageNames))
    for tree in TreeMapping :
        allTreeDict[tree["TreeName"]] = tree["TreeEvolutionSprite"]
    
    print(allTileNames)
    print(allTreeNames)
    print(allFoliageNames)
    print(allTreeDict)
def dfRoundUp(size=(100,100),df=None) :
    for x in range(size[0]) :
        for y in range(size[1]) :
            if df[x ,y]!=0 :
                df[x ,y] = math.ceil(df[x ,y])
    return df
def minPointDistanceDf(size=(100,100),df=None,minDistance=1) :
    for x in range(minDistance,size[0]-minDistance) :
        for y in range(minDistance,size[1]-minDistance) :
            if df[x ,y]!=0 :
                for x2 in range(-minDistance,minDistance) :
                    for y2 in range(-minDistance,minDistance) :
                        if df[x+x2 ,y+y2]!=0 :
                            if (x2==0 and y2==0) :
                                pass
                            else :
                                df[x+x2 ,y+y2] = 0
    return df
                    
def genPointsInBiome(size=(100,100),df=None,multip=1,relaxfact=0) :
        ret_arr = []
        for x in range(size[0]) :
            for y in range(size[1]) :
                if df[x,y]*multip>random.random() :
                    ret_arr.append([x,y])
        points = np.array(ret_arr)
        if relaxfact != 0 :
            points = relax(points,size,relaxfact)
            points = np.array(points)
        return points
    
def pointsToMap(size=(100,100),pointArray=None,defVal=0) :
    mapDf = np.zeros(size)
    for point in pointArray :
        mapDf[point[0],point[1]] = defVal
    return mapDf

def extractFrequencyBiome(size=(100,100),biomeIndexMap=None,biomeStatList=[],fieldName="",calculateLen=False) :
    ret_df = np.zeros(size)
    for biomeNum in range(len(biomeStatList)) :
        if not calculateLen :
            ret_df = ret_df + (biomeIndexMap==biomeNum).astype(int)*biomeStatList[biomeNum][fieldName]
        else :
            ret_df = ret_df + (biomeIndexMap==biomeNum).astype(int)*len(biomeStatList[biomeNum][fieldName])
    return ret_df

def openBiomeImage(folder="") :
    id1 = getDataFromImg(openImage(folder+"/biome1.png"))
    id2 = selectColorFromMat(getDataFromImg(openImage(folder+"/biome2.png")),0)
    return id1,id2

def openImage(path="") :
    img = Image.open(path).convert("RGB")
    return img

def getDataFromImg(img) :
    width, height = img.size
    px = img.load()
    data_ret = np.zeros((width, height,3))
    for x in range(width) :
        for y in range(height) :
            color = px[x,y]
            data_ret[x,y] = color
    return data_ret

def selectColorFromMat(mat,dataIndex=0) :
    width, height, depth = mat.shape
    data_ret = np.zeros((width, height))
    for x in range(width) :
        for y in range(height) :
            data_ret[x][y] = mat[x][y][dataIndex]
    return data_ret

def mergeMap(perlinMap,vonoidMap):
    listAvg = average_cells(vonoidMap,perlinMap)
    df_ret = fill_cells(vonoidMap,listAvg)
    df_ret = convertNumpyFloat(df_ret.shape,df_ret)
    return df_ret

def jsonToMat(jsonDictList) :
    maxX,maxY = jsonDictList[-1:][0]["pos"]
    ret_mat = [[{} for y in range(maxY+1)] for x in range(maxX+1)] 
    for x in range(maxX+1) :
        for y in range(maxY+1) :
            for jsonDict in jsonDictList :
                if jsonDict["pos"] == [x,y] :
                    ret_mat[x][y] = jsonDict
    return ret_mat

def openJson(path,filename,extention,disp=True) :
    with open(path+"/"+filename+"."+extention) as file:
        data = json.load(file)
    return data

def toBool(n):
    return bool(n)

def generateSea(size=(100,100),df=None,seaRange=[0,0.1],beachRange=[0.1,0.2],asInt=True) :
    sea = createMaskNumpyFloat(size,df,seaRange,asInt)
    beach = createMaskNumpyFloat(size,df,beachRange,asInt)
    return sea,beach

def generateTerain(size=(100,100),df=None,biomeNum=4,sea=None,beach=None) :
    validTerrainMask = np.invert((sea+beach).astype(bool)).astype(int)
    df = segmentation(size,df,biomeNum)
    df = ((df + 3)* validTerrainMask + sea*1 + beach*2)-1
    return df

def generateTerainNoSB(size=(100,100),biomeDf=None,biomeSize=4,sea=None,seaSize=0,beach=None,beachSize=0) :
    validTerrainMask = np.invert((sea+beach).astype(bool)).astype(int)
    df = segmentation(size,biomeDf,biomeSize-seaSize-beachSize)
    df = (sea*seaSize*(sea.astype(bool).astype(int))+ (beach*beachSize+seaSize)*(beach.astype(bool).astype(int)) + (df + seaSize+beachSize+1)* validTerrainMask)-1
    return df

def generateTerainDef(size=(100,100),biomeDf=None,biomeSize=4) :
    df = segmentation(size,biomeDf,biomeSize)
    return df

def dispStatNumpyDf(df,plotDf=False,plotBar=False,barChartUnique=False) :
    print(" === Numpy dataframe stats === ")
    print("Shape       :",df.shape)
    print("Minimum val :",df.min())
    print("Maximum val :",df.max())
    print("Average val :",np.average(df))
    print("Mean val    :",np.mean(df))
    print("Std val     :",np.std(df))
    print("Var val     :",np.var(df))
    if plotDf and not plotBar :
        plot(df)
    if plotDf and plotBar :
        plotDfAndBar(df,barChartUnique)
    #print(len(np.average(df,0)))
    # plt.hist(np.sum(df,0))
    # plt.show() 
    # plt.hist(np.sum(df,1))
    # plt.show() 
    #lol = plt.hist(df, bins='auto')
    #plt.show()

def plot(df,color='rainbow') :
    fig = plt.figure(dpi=200, figsize=(5, 5))
    plt.imshow(df,cmap = color)

def plotDfAndBar(df,barChartUnique=False) :
    fig, ax = plt.subplots(1 ,2)
    fig.set_dpi(200)
    fig.set_size_inches(10, 5)
    ax[0].imshow(df, cmap="rainbow")
    if barChartUnique :
        unique, counts = np.unique(df.astype(int), return_counts=True)
        if len(unique)<100:
            counts = counts/(sum(counts))
            ax[1].bar(unique, counts)
        else :
            ax[1].bar([0], [1])
    else :
        ax[1].hist(df.flatten(), bins=64, color="blue", alpha=0.66)
    plt.show() 
    
        
def genVornoi(size=(100,100),point=1000,relaxEnable=True,relaxIteration=10,smoothing=False,boundaryDisplacement=100,toFloat=True,display=True):
    vor_map = voronoiSetup(size,point,relaxEnable,relaxIteration,False)
    vor_map = bounderyCalculation(size,vor_map,smoothing,boundaryDisplacement,False)
    if toFloat :
        vor_map = convertNumpyFloat(size,vor_map)
    if display :
        dispStatNumpyDf(vor_map,True,True,False)
    return vor_map

def genPerl(size=(100,100),scale=5,octaves=5,persistence=0.5,lacunarity=2,histeqAlpha=0,display=True):
    perl_df = noise_map2(size, scale, random.randint(0,100), octaves=octaves, persistence=persistence, lacunarity=lacunarity)
    perl_df = histeq(perl_df,histeqAlpha)
    perl_df = convertNumpyFloat(size,perl_df)
    if display :
        dispStatNumpyDf(perl_df,True,True,False)
    return perl_df

def voronoiSetup(size=(50,50),pointNumber=50,relaxEnable=False,relaxIteration=5,display=False):
    points = np.random.randint(0, size, (pointNumber, 2))
    if relaxEnable : 
        points = relax(points, size, k=relaxIteration)
    vor = voronoi(points, size)
    vor_map = voronoi_map2(vor, size)
    if display :
        fig = plt.figure(dpi=150, figsize=(10, 10))
        plt.scatter(*points.T, s=1)
    return vor_map
        
def bounderyCalculation(size=(50,50),vor_map=None,smoothing=False,boundaryDisplacement=10,display=True) :
    if type(vor_map)!=type(None) :
        if smoothing :
            boundary_noise = np.dstack([noise_map(size[0], 32, 200, octaves=8), noise_map(size[0], 32, 250, octaves=8)])
            boundary_noise = np.indices(size).T + boundaryDisplacement*boundary_noise
            boundary_noise = boundary_noise.clip(0, size[0]-1).astype(np.uint32)
            blurred_vor_map = np.zeros_like(vor_map)

            for x in range(size[0]):
                for y in range(size[1]):
                    j, i = boundary_noise[x, y]
                    blurred_vor_map[x, y] = vor_map[i, j]
            vor_map = blurred_vor_map
        if display :
            fig = plt.figure(dpi=150, figsize=(10, 10))
            plt.imshow(vor_map,cmap = 'rainbow')
        return vor_map
    else :
        return None
    
def segmentation(size=(50,50),vor_map=None,segments=10,valRange=[0,1],defaultValue=None) :
    minVal = valRange[0]
    maxVal = valRange[1]
    vor_map_ret = np.zeros_like(vor_map)
    for x in range(size[0]):
        for y in range(size[1]):
            currentVal = vor_map[x, y]
            if currentVal >= minVal and currentVal <= maxVal :
                vor_map_ret[x, y] = int(min(int(((currentVal-minVal)/(maxVal-minVal))*segments),segments-1))
            else :
                vor_map_ret[x, y] = defaultValue
    return vor_map_ret.astype(int)

def mapListInDf(size=(100,100),df=None,mapList=None) :
    df_ret = np.zeros_like(df)
    mapList = list(mapList)
    print(len(mapList))
    for x in range(size[0]) :
        for y in range(size[1]) :
            df_ret[x][y] = mapList[int(df[x][y])]
            if x%200==0 and y%200==0 :
                pass
                #print(int(df[x][y]))
    return df_ret

def fill_cells(vor, data):
    size = vor.shape[0]
    image = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            p = vor[i, j]
            image[i, j] = data[p]

    return image
            
def convertNumpyFloat(size=(50,50),df=None) :
    if type(df)!=type(None) : 
        maxVal = df.max()
        minVal = df.min()
        df_ret = (df-minVal)/(maxVal-minVal)
        return df_ret
    else :
        return None    
    
def createMaskNumpyFloat(size=(50,50),df=None,valRange=[0,0.2],asInt=True) :
    if type(df)!=type(None) : 
        df_up = df>=valRange[0]
        df_down = df<=valRange[1]
        df_ret = np.logical_and(df_up, df_down)
        if asInt : 
            df_ret = df_ret.astype(int)
        return df_ret
    else :
        return None   
    
    
    
def layerSelection(size=(50,50),vor_map=None,segments=10,display=True) :
    vor_map_mask = vor_map == segments
    if display :
        fig = plt.figure(dpi=150, figsize=(10, 10))
        plt.imshow(vor_map_mask,cmap = 'gray')
        
        
    return vor_map_mask
def voronoi(points, size):
    # Add points at edges to eliminate infinite ridges
    edge_points = size*np.array([[-1, -1], [-1, 2], [2, -1], [2, 2]])
    new_points = np.vstack([points, edge_points])
    
    # Calculate Voronoi tessellation
    vor = Voronoi(new_points)
    
    return vor

def voronoi_map2(vor, size):
    # Calculate Voronoi map
    vor_map = np.zeros(size, dtype=np.uint32)

    for i, region in enumerate(vor.regions):
        # Skip empty regions and infinte ridge regions
        if len(region) == 0 or -1 in region: continue
        # Get polygon vertices    
        x, y = np.array([vor.vertices[i][::-1] for i in region]).T
        # Get pixels inside polygon
        rr, cc = polygon(x, y)
        # Remove pixels out of image bounds
        in_box = np.where((0 <= rr) & (rr < size[0]) & (0 <= cc) & (cc < size[1]))
        rr, cc = rr[in_box], cc[in_box]
        # Paint image
        vor_map[rr, cc] = i

    return vor_map

def relax(points, size, k=10):  
    new_points = points.copy()
    for _ in range(k):
        vor = voronoi(new_points, size)
        new_points = []
        for i, region in enumerate(vor.regions):
            if len(region) == 0 or -1 in region: continue
            poly = np.array([vor.vertices[i] for i in region])
            center = poly.mean(axis=0)
            new_points.append(center)
        new_points = np.array(new_points).clip(0, size)
    return new_points

def noise_map(size, res, seed, octaves=1, persistence=0.5, lacunarity=2.0, map_seed=0):
    scale = size/res
    return np.array([[
        snoise3(
            (x+0.1)/scale,
            y/scale,
            seed+map_seed,
            octaves=octaves,
            persistence=persistence,
            lacunarity=lacunarity
        )
        for x in range(size)]
        for y in range(size)
    ])

def noise_map2(size, res, seed, octaves=1, persistence=0.5, lacunarity=2.0):
    scale1 = size[0]/res
    scale2 = size[1]/res
    return np.array([[
        snoise3(
            (x+0.1)/scale1,
            y/scale2,
            seed,
            octaves=octaves,
            persistence=persistence,
            lacunarity=lacunarity
        )
        for x in range(size[0])]
        for y in range(size[1])
    ])

def histeq(img,  alpha=1) :
    img_cdf, bin_centers = exposure.cumulative_distribution(img)
    img_eq = np.interp(img, bin_centers, img_cdf)
    img_eq = np.interp(img_eq, (0, 1), (-1, 1))
    return alpha * img_eq + (1 - alpha) * img

def average_cells(vor, data):
    """Returns the average value of data inside every voronoi cell"""
    size = vor.shape[0]
    count = np.max(vor)+1

    sum_ = np.zeros(count)
    count = np.zeros(count)

    for i in range(size):
        for j in range(size):
            p = vor[i, j]
            count[p] += 1
            sum_[p] += data[i, j]

    average = sum_/count
    average[count==0] = 0

    return average

def superposeDFtoImage(d1,d2,d3):
    sizeX = d1.shape[0]
    sizeY = d1.shape[1]
    image = np.zeros((sizeX, sizeY, 3))
    for i in range(sizeX):
        for j in range(sizeY):
            image[i, j] = [d1[i,j],d2[i,j],d3[i,j]]
    return image

def colorNumpyBiome(d1,d2,biomeColorMat,display=True):
    size = d1.shape
    image = np.zeros((size[0], size[1], 3))
    for i in range(size[0]):
        for j in range(size[1]):
            col = '#%02x%02x%02x' % tuple(list(biomeColorMat[int(d2[i,j])][int(d1[i,j])].astype(int)))
            image[i, j] = ImageColor.getcolor(col, "RGB")
    image = image.astype(np.uint8)
    if display :
        fig = plt.figure(figsize=(10, 10), dpi=300)
        plt.imshow(image)
    return image

def mergeDfIntoImage(d1,d2,d3,display=True) :
    size = d1.shape
    image = np.zeros((size[0], size[1], 3))
    for i in range(size[0]):
        for j in range(size[1]):
            col = '#%02x%02x%02x' % tuple(list([int(d1[i,j]),int(d2[i,j]),int(d3[i,j])]))
            image[i, j] = ImageColor.getcolor(col, "RGB")
    image = image.astype(np.uint8)
    if display :
        fig = plt.figure(figsize=(10, 10), dpi=300)
        plt.imshow(image)
    return image
def indexNumpyBiome(d1,d2,biomeIndexMat,display=True):
    size = d1.shape
    image = np.zeros((size[0], size[1]))
    for i in range(size[0]):
        for j in range(size[1]):
            image[i, j] = biomeIndexMat[int(d2[i,j])][int(d1[i,j])]
    if display :
        fig = plt.figure(figsize=(10, 10), dpi=300)
        plt.imshow(image)
    return image

def colorBiomeMapStat(d1,d2,biomeMatSize,display=True):
    bioX = biomeMatSize[0]
    bioY = biomeMatSize[1]
    mat_stat = np.zeros((bioX, bioY))
    mat_statX = np.zeros((bioX))
    mat_statY = np.zeros((bioY))
    mat_statXIndex = np.array([x for x in range(bioX)])
    mat_statYIndex = np.array([y for y in range(bioY)])
    size = d1.shape[0]
    pct = 100
    for i in range(size):
        for j in range(size):
            x = int(d1[i,j])
            y = int(d2[i,j])
            mat_stat[x][y] = mat_stat[x][y] + 1
            mat_statX[x] = mat_statX[x] +1
            mat_statY[y] = mat_statY[y] +1
    mat_stat = pct*mat_stat/(size*size)
    mat_statX = pct*mat_statX/(size*size)
    mat_statY = pct*mat_statY/(size*size)
    fig, ax = plt.subplots(1,3)
    fig.set_dpi(300)
    fig.set_size_inches(15, 5)
    im = ax[0].imshow(mat_stat)
    for i in range(bioX):
        for j in range(bioY):
            text = ax[0].text(j, i, round(mat_stat[i, j],2), ha="center", va="center", color="w")
    ax[1].bar(mat_statXIndex, mat_statX)
    ax[2].bar(mat_statYIndex, mat_statY)
    print(mat_statY)
    fig.tight_layout()
    plt.show()
    
def getEdgeMask(df,asInt=False) :
    sx = ndimage.sobel(df, axis=0, mode='nearest')
    sy = ndimage.sobel(df, axis=1, mode='nearest')
    mask = (np.hypot(sx, sy)==0)
    # = (ndimage.sobel(df, mode='constant')==0)
    if asInt :
        mask = mask.astype(int)
    return mask

def getEdgeBlur(df,border=3,sd=3) :
    edge = getEdgeMask(df,True)
    edge1 = ndimage.uniform_filter(edge, size=int(border/2))*100
    gf = ndimage.gaussian_filter(edge1,sd)
    return convertNumpyFloat(gf.shape,gf)


ins1 = {"MapSize":[200,200],"BiomeSize":1,"NumberOfBiomes":5,"NumberOfSeaBiomes":1,"SeaBiomeSize":1,"BeachEnable":True}
ntb = naturalTerrainBuilder(ins1)