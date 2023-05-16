# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import json 
import csv
from PIL import ImageTk,Image,ImageOps, ImageColor, ImageFilter
import random
import re
import os
import pygame
from originalGameConfLoader import *
from pygame.locals import *
import pandas as pd
import math

class spriteLoader :
    def __init__(self,resizeTile=True,resizeElse=True,tileSize=32,elseSizePct=1,resampleSelection=1):
        #print("sprint loader start")
        self.resampleList = [Image.ANTIALIAS,Image.NEAREST,Image.BILINEAR,Image.BICUBIC,Image.LANCZOS]
        self.resizeTile = resizeTile
        self.resizeElse = resizeElse
        self.tileSize = tileSize
        self.elseSizePct = elseSizePct
        self.resampleSelection = resampleSelection
        
        self.spritebankPath = "C:/Users/Alexandre/Desktop/test_lua/test5"
        self.materialsPath = "C:/Users/Alexandre/Desktop/test_lua/test5"
        self.imageFolder = "/image/"
        self.imageOutputFolder = self.imageFolder+"out4/"
        self.settingsList = [[False,False]]#[[False,False],[True,False],[False,True]],[False,True]
        self.spritebankFilename = ["interface","interface_d11","objects","objects_d11","objects_d11_2"]
        self.spritesheetFilename = ["ui","ui_d11","objects","objectsTexture_d11","objects_d11_2"]
        self.spriteSheetListConf = [["objects",32],["objects_d11_2",32],["objectsTexture_d11",32],["people",32],["special-entities",32],["ui",32],["ui_d11",32],["tilesetpadded",72]]
        self.extraMapping = ["special-entities","people","objects"]
        
        self.masterLoad()
        #print(self.stat_df.loc[(self.stat_df["Category"]=="Entity")].loc[(self.stat_df["VarNum"]==1)])
        
        #print(seleMaterial(self.matConfList,["Object"],"Properties","Entity"))
        #itemList = seleMaterial(self.matConfList,["Object"],"Properties","Wearable")
        #self.saveObjList2(itemList,self.spritebankPath+self.imageOutputFolder,4,5)
    
    def masterLoad(self) :
        print("start load")
        self.spriteConfList = getListAllSpriteConf(self.spritebankPath,self.spritebankFilename,self.spritesheetFilename,self.extraMapping)
        self.matConfList = openMaterialList(self.materialsPath)
        self.spriteImageList = openSpriteImageList(self.spritebankPath+self.imageFolder,self.spriteSheetListConf)
        self.objNameList = self.spriteNameListFromSpriteList(self.spriteConfList)
        self.stat_df = self.generateStatsFromMatListDF(self.matConfList)
        print("gen img")
        #self.generateAllSprites()
        
    def processLoadRequest(self,request,orienRange=-1,variantRange=-1) :
        retd,retm = self.loadFromInstructions(request)
        imgList, infodf = self.imageFromMatList(retm,[],[],orienRange,variantRange,retd)
        pyGameImgList = self.getPygameImageList(imgList)
        del(imgList)
        return pyGameImgList,infodf
        
    def loadFromInstructions(self,instruMat) :
        materialList = []
        infoDf = None
        for instruEle in instruMat :
            if len(instruEle) != 1 :
                varnum = None
                otherVals = []
                if len(instruEle)>3 :
                    varnum = instruEle[3]
                if len(instruEle)>2 :
                    otherVals = instruEle[2]
                retd,retm = self.masterSelect(instruEle[0],instruEle[1],otherVals,varnum,"dm")
            else :
                retd,retm = self.masterSelectName(instruEle[0])
            if type(retd) != type(None) and type(retm) != type(None) :
                materialList.extend(retm)
                if type(infoDf) == type(None) :
                    infoDf = retd
                else :
                    infoDf = infoDf.append(retd, ignore_index=True)
        infoDf = infoDf.reset_index(drop=True)
        return infoDf , materialList
       
    def generateAllSprites(self) :
        itemList = seleMaterial(self.matConfList,["Object","Material","Equipment"],None,None)#["Object"],"Properties","Vehicle")#["Object"],None,None)##,"SpriteType","RandomArea"["Material"],"Name","Dirt"   ["Material"],"Name","Dirt"
        savedList = self.saveObjList2(itemList,self.spritebankPath+self.imageOutputFolder,4,50,True,False)
        objNameList = self.spriteNameListFromSpriteList(self.spriteConfList,False,True)
        count = 0
        for objName in objNameList :
            if objName not in savedList :
                count = self.generateSpriteFromName(objName,count,True)
                
    def generateStatsFromMatList(self,mat,category=["Object","Material","Equipment"]) :#,"Material","Equipment"
        strList=[]
        for cat in category :
            for ele in mat[cat] :
                string = self.generateStatsFromMat2(ele,cat)
                if string != None :
                    strList.append(string)
        saveList(strList,self.spritebankPath,"statsnew2","txt")

    def generateStatsFromMatListDF(self,mat,category=["Object","Material","Equipment"]) :#,"Material","Equipment"
        valMat=[]
        for cat in category :
            for ele in mat[cat] :
                valList = self.generateStatsFromMat2(ele,cat,False)
                valMat.append(valList)
        df = pd.DataFrame(valMat, columns =["Type","Name","Category","AddInfos","VarNum","StackFlag","spList"])#, dtype = float)
        return df
        
    def masterSelect(self,eletype=[],category=[],addinfo=[],varnum=None,returnType="d") : #d dataframe n name l name list m material
        stat_df = self.stat_df
        if eletype!=[] :
            stat_df = stat_df[stat_df["Type"].isin(eletype)]
        if category!=[] :
            stat_df = stat_df[stat_df["Category"].isin(category)]
        if varnum!=None :
            if varnum>=0 :
                stat_df = stat_df[stat_df["VarNum"]>varnum]
            else :
                stat_df = stat_df[stat_df["VarNum"]<=-varnum]
        if addinfo!=[] :
            allNoFlag = True
            for info in addinfo :
                if "no_" not in info :
                    allNoFlag = False
            nameList=[]
            if addinfo == ["no_Dog"] :
                print(allNoFlag)
            for name in list(stat_df["Name"]) :
                flag = True
                noFlag = False
                val = list(stat_df.loc[(stat_df["Name"]==name)]["AddInfos"])[0]
                # if addinfo == ["no_Dog"] :
                #     print("------",name)
                #     print(stat_df.shape)
                #     print(flag)
                #     print(noFlag)
                for info in addinfo :
                    info2 = info
                    # if addinfo == ["Head","FromFig"] :
                    #     print(info2,"   ",val)
                    if "no_" in info2 :
                        info2 = info2.replace("no_","")
                        if info2 in val :
                            noFlag = True
                    else :
                        if info not in val :
                            flag = False
                # if addinfo == ["no_Dog"] :
                #     print(stat_df.shape)
                #     print(flag)
                #     print(noFlag)
                if flag and not noFlag:
                    nameList.append(name)
            stat_df = stat_df[stat_df["Name"].isin(nameList)]
        if stat_df.empty :
            if returnType == "dm" :
                return None,None
            else :
                return None
        if returnType == "d" :
            return stat_df
        if returnType == "n" :
            return stat_df["Name"]
        if returnType == "cm" :
            return dfToList(stat_df,["Type","Name"])
        if returnType == "dl" :
            return dfToDict(stat_df,["Name","VarNum"],["Name","SpriteVariants"])
        if returnType == "l" :
            return list(stat_df["Name"])
        if returnType == "m" :
            return self.selListMaterialByName(stat_df["Name"])
        if returnType == "ai" :
            return self.getAdditionalInfoFromStat(stat_df)
        if returnType == "dm" :
            return stat_df,self.selListMaterialByName(stat_df["Name"])
        return None
    
    def masterSelectName(self,Name) :
        stat_df = self.stat_df
        stat_df = stat_df[stat_df["Name"]==Name]
        if not stat_df.empty :
            return stat_df,self.selListMaterialByName(stat_df["Name"])
        else :
            return None,None
    
    def getAdditionalInfoFromStat(self,stat_df) :
        if type(stat_df)==type(None) :
            return None
        ai_list = []
        stat_ai_list = list(stat_df["AddInfos"])
        if stat_ai_list != [] :
            for ai_ele in stat_ai_list :
                if ai_ele != None and ai_ele != [] :
                    for ai in ai_ele :
                        if ai not in ai_list :
                            ai_list.append(ai)
        return ai_list
    def selOneMaterialByName(self,name="Accountant",category=["Object","Material","Equipment"]) :
        eleList = []
        for cat in category :
            if cat in self.matConfList.keys() :
                for ele in self.matConfList[cat] :
                    if "Name" in ele.keys() :
                        if name==ele["Name"] :
                            eleList.append(ele)
        if eleList == [] :
            return None
        else :
            return eleList[0]
        
    def selListMaterialByName(self,nameList=["Accountant"],category=["Object","Material","Equipment"]) :
        if type(nameList) == type(None) :
            return None
        else :
            nameList = list(nameList)
        eleList = []
        for name in nameList :
            ele = self.selOneMaterialByName(name)
            if ele!=None :
                eleList.append(ele)
        return eleList

    def generateStatsFromMat2(self,mat,category,returnString=True) :
        Name = ""
        matfilter = []
        properties = []
        MadeOf = None
        Research = None
        Group = None
        Equipment = None
        IndoorOutdoor = None
        ObjectRequired = None
        BlockMovement = None
        SpriteType = None
        SpecialRestriction = None
        stackFlag = False
        maxVar = self.imageFromMat(mat,0,0,False,False,True)
        maxVar2 = self.imageFromMat(mat,0,0,False,True,True)
        if maxVar2!= None :
            stackFlag = True
        if maxVar!=None :
            maxVar = int(maxVar)
        if "Name" in mat.keys() :
            Name = mat["Name"]
        if "Filter" in mat.keys() :
            matfilter = mat["Filter"]
            if type(matfilter) == type("") :
                matfilter = [mat["Filter"]]
        if "Properties" in mat.keys() :
            properties = mat["Properties"]
            if type(properties) == type("") :
                properties = [mat["Properties"]]
        if "MadeOf" in mat.keys() :
            MadeOf = mat["MadeOf"]
        if "Group" in mat.keys() :
            Group = mat["Group"]
        if "Research" in mat.keys() :
            Research = mat["Research"]
        if "Equipment" in mat.keys() :
            Equipment = mat["Equipment"]
        if "IndoorOutdoor" in mat.keys() :
            IndoorOutdoor = mat["IndoorOutdoor"]
        if "ObjectRequired" in mat.keys() :
            ObjectRequired = mat["ObjectRequired"]
        if "BlockMovement" in mat.keys() :
            BlockMovement = mat["BlockMovement"]
        if "SpriteType" in mat.keys() :
            SpriteType = mat["SpriteType"]
        if "SpecialRestriction" in mat.keys() :
            SpecialRestriction = mat["SpecialRestriction"]
        subcategory = "None"
        otherVals = []
        if category == "Object" :
            if "Vehicle" in properties :
                subcategory = "Vehicle"
            elif "Entity" in properties :
                subcategory = "Entity"
                properties2 = properties.copy()
                if "Entity" in properties2 :
                    properties2.remove("Entity")
                if "DoesNotTire" in properties2 :
                    properties2.remove("DoesNotTire")
                otherVals = properties2
            elif "BodyPart" in properties :
                subcategory = "BodyPart"
                properties2 = properties.copy()
                if "BodyPart" in properties2 :
                    properties2.remove("BodyPart")
                otherVals = properties2
            elif "Wearable" in properties :
                subcategory = "Wearable"
                properties2 = properties.copy()
                if "Wearable" in properties2 :
                    properties2.remove("Wearable")
                otherVals = properties2
            elif "Mail" in Name :
                subcategory = "Mail"
            elif "Door" in properties :
                subcategory = "Door"
                if "Jail" in Name :
                    otherVals.append("Jail")
                if "Large" in Name :
                    otherVals.append("Large")
                if "Gate" in Name :
                    otherVals.append("Gate")
                if "Fence" in Name :
                    otherVals.append("Fence")
            elif "Utility" in properties or "Electrical" in properties or "Wired" in properties or "WaterUtility" in properties :
                if "Decoration" not in matfilter and "Rest" not in matfilter and "Exercise" not in matfilter and "Entertainment" not in matfilter and "Catering" not in matfilter :
                    subcategory = "Utility"
                else :
                    subcategory = "Furniture"
            elif "Signs" in matfilter :
                subcategory = "Signs"
            elif "Foliage" in matfilter or "TreeStump" in Name:
                subcategory = "Foliage"
                if "TreeYoungCustom" in Name :
                    otherVals.append("TreeYoungCustom")
                if "TreeCustom" in Name :
                    otherVals.append("TreeCustom")
                if "TreeYoung" in Name :
                    otherVals.append("TreeYoung")
                if "Tree" in Name :
                    otherVals.append("Tree")
                if "Plant" in Name :
                    otherVals.append("Plant")
                if "Crop" in Name :
                    otherVals.append("Crop")
                if "Flower" in Name :
                    otherVals.append("Flower")
                if "Topiary" in Name :
                    otherVals.append("Topiary")
                if "Bush" in Name :
                    otherVals.append("Bush")
            elif "Bakery" in Name or "Ingredient" in Name or "Restaurant" in Name or "FoodTray" in Name or "FoodBow" in Name or "FoodTrash" in Name:
                subcategory = "Cooking"
            elif "Material" in properties :
                subcategory = "Material"
            if matfilter != [] and (subcategory == "None" or subcategory == "Furniture"):
                subcategory = "Furniture"
                matfilter2 = matfilter
                if "RequiresElectricity" in matfilter2 :
                    matfilter2.remove("RequiresElectricity")
                if "RequiresWater" in matfilter2 :
                    matfilter2.remove("RequiresWater")
                otherVals = matfilter2
            if subcategory == "None" :
                if "Uncloneable" in properties or "Undamageable" in properties :
                    subcategory = "Static"
                    
        if category == "Equipment" :
            subcategory = "standard"
            properties2 = properties
            if "NoImport" in properties2 :
                properties2.remove("NoImport")
            if "ExtraContraband" in properties2 :
                properties2.remove("ExtraContraband")
            otherVals = properties2
            
        if category == "Material" : 
            properties2 = properties
            if "IsFoundationWall" in properties2 or "Wall" in Name:
                subcategory = "FoundationWall"
            elif "Fence" in Name:
                subcategory = "Fence"
            elif IndoorOutdoor == "1" :
                subcategory = "OutdoorFloor"
            elif IndoorOutdoor == "2" or "Tiles" in Name or "Floor" in Name or "Flooring" in Name:
                subcategory = "IndoorFloor"
                
            # if SpriteType != None :
            #     if SpriteType == "Connected" :
            #         subcategory = "wall"
            #     else :
            #         subcategory = "floor"
            
            if "HeatWaveAffected" in properties2 :
                otherVals.append("Foliage")
            if SpriteType!=None : 
                otherVals.append(SpriteType)
            if ObjectRequired != None :
                otherVals.append(ObjectRequired)
            if BlockMovement!=None :
                if BlockMovement == "false" :
                    otherVals.append("NotBlockMovement")
                else :
                    otherVals.append("BlockMovement")
        if returnString :
            string = str(category)+";"+str(Name)+";"+str(subcategory)+";"+str(otherVals)
            return string
        else :
            return [str(category),str(Name),str(subcategory),otherVals,maxVar,stackFlag,[]]

        
    def generateSpecForCharaSel(self,path,filename) : #For cha selector window
        itemList = seleMaterial(self.matConfList,["Object"],"Properties","Head")
        headDict = self.getObjListName(itemList)
        itemList = seleMaterial(self.matConfList,["Object"],"Properties","Body")
        bodyDict = self.getObjListName(itemList)
        itemList = seleMaterial(self.matConfList,["Object"],"Properties","Entity","Dog")
        entityList = self.getObjListName(itemList)
        itemList = seleMaterial(self.matConfList,["Object"],"Properties","Dog")
        dogList = self.getObjListName(itemList) 
        
        headDictF = []
        headDictM = []
        bodyDictF = []
        bodyDictM = []
        headFig = {}
        bodyFig = {}
        womanFaceList = ["Female","Woman","Daughter","Wife"]
        for ele in headDict :
            if "FromFig" in ele["Name"] :
                headFig = ele
            else :
                isFemaleFlag = False
                for femaleWord in womanFaceList :
                    if femaleWord in ele["Name"] :
                        isFemaleFlag = True
                if isFemaleFlag :
                    headDictF.append(ele)
                else :
                    headDictM.append(ele)

        for ele in bodyDict or "Woman" in ele["Name"]:
            if "Female" in ele["Name"] :
                bodyDictF.append(ele)
            elif "FromFig" in ele["Name"] :
                bodyFig = ele
            else :
                bodyDictM.append(ele)
                
        masterDict = {"Character" : {"Preset" : {"Humain":entityList,"Dog":dogList}, "Custom" : {"Head" : {"Preset" : headFig,"Custom" : {"Male" : headDictM,"Female":headDictF}},"Body" : {"Preset" : bodyFig,"Custom" : {"Male" : bodyDictM,"Female":bodyDictF}}}}}
        saveDict(masterDict,path,filename,"json",2,False)

    def generateSpecForCharaSel2(self,path,filename) : #For cha selector window
        
        HeadFromFig = self.masterSelect(["Object"],["BodyPart"],["Head","FromFig"],None,"dl")
        HeadMale = self.masterSelect(["Object"],["BodyPart"],["Head","Male","no_FromFig"],None,"dl")
        HeadFemale = self.masterSelect(["Object"],["BodyPart"],["Head","Female","no_FromFig"],None,"dl")
        
        BodyFromFig = self.masterSelect(["Object"],["BodyPart"],["Body","FromFig"],None,"dl")
        BodyMale = self.masterSelect(["Object"],["BodyPart"],["Body","Male","no_FromFig","no_Naked"],None,"dl")
        BodyFemale = self.masterSelect(["Object"],["BodyPart"],["Body","Female","no_FromFig","no_Naked"],None,"dl")
        BodyMaleNaked = self.masterSelect(["Object"],["BodyPart"],["Body","Male","no_FromFig","Naked"],None,"dl")
        BodyFemaleNaked = self.masterSelect(["Object"],["BodyPart"],["Body","Female","no_FromFig","Naked"],None,"dl")
        
        Entity = self.masterSelect(["Object"],["Entity"],["no_Dog"],None,"dl")
        EntityMultVar = self.masterSelect(["Object"],["Entity"],["no_Dog"],1,"dl")
        EntitySingleVar = self.masterSelect(["Object"],["Entity"],["no_Dog","no_Warden"],-1,"dl")
        EntityDog = self.masterSelect(["Object"],["Entity"],["Dog"],None,"dl")
        EntityWarden = self.masterSelect(["Object"],["Entity"],["Warden"],None,"dl")

        #Wearable = self.masterSelect(["Object"],["Wearable"],[],None,"dl")
        WearableHeadTattoo = self.masterSelect(["Object"],["Wearable"],["Head","Tattoo"],None,"dl")
        WearableHeadElse = self.masterSelect(["Object"],["Wearable"],["Head","no_Tattoo"],None,"dl")
        WearableBodyTattoo = self.masterSelect(["Object"],["Wearable"],["Body","Tattoo"],None,"dl")
        WearableBodyElse = self.masterSelect(["Object"],["Wearable"],["Body","no_Tattoo"],None,"dl")
        WearableElse = self.masterSelect(["Object"],["Wearable"],["no_Body","no_Head"],None,"dl")

        masterDict = {"Wearable":{"Head" :{"Tattoo" : WearableHeadTattoo , "Other" : WearableHeadElse},"Body" :{"Tattoo" : WearableBodyTattoo , "Other" : WearableBodyElse},"Other":WearableElse},"Character" : {"Preset" : {"HumainSingle":EntitySingleVar,"HumainCategory":EntityMultVar,"Warden":EntityWarden,"Dog":EntityDog}, "Custom" : {"Head" : {"Preset" : HeadFromFig,"Custom" : {"Male" : HeadMale,"Female":HeadFemale}},"Body" : {"Preset" : BodyFromFig,"Custom" : {"Clothes" : {"Male" : BodyMale,"Female":BodyFemale},"Naked" : {"Male" : BodyMaleNaked,"Female":BodyFemaleNaked}}}}}}
        saveDict(masterDict,path,filename,"json",2,False)

                
    def generateSpriteFromName(self,name,count,singleFolder=False) :
        conf = self.getSpriteConfFromName(name)
        if conf!=None :
            if singleFolder and conf["file"] != "ui" and conf["file"] != "ui_d11" :
                path = self.spritebankPath+self.imageOutputFolder+"Other/"
            else :
                path = self.spritebankPath+self.imageOutputFolder+"Other/"+conf["file"]+"/"
            img = self.getImgFromSprite(conf)
            createFolder(path)
            if singleFolder :
                img.save(path+str(count)+"."+conf["file"]+"."+conf["Name"]+".png","PNG")
            else :
                img.save(path+str(count)+"."+conf["Name"]+".png","PNG")
            count = count +1
        return count
    

    def saveObjList2(self,itemList,path="C:/Users/Alexandre/Desktop/test_lua/test3/image/out14/",rotationNum=1,variantNum=1,subcategorybool=True,collectImage=False) :
        count = 0
        savedList = []
        for it in itemList :
            mat = selOneMaterial(self.matConfList,it[0],it[1])
            if subcategorybool :
                SubCategory = mat["SubCategory"]
            if mat!=None :
                for x in range(rotationNum) :
                    for y in range(variantNum) :
                        for seting in self.settingsList :
                            img,name = self.imageFromMat(mat,x,y,seting[0],seting[1])
                            if img!=None :
                                newpath = path
                                if subcategorybool :
                                    newpath = newpath+it[0]+"/"+SubCategory+"/"
                                createFolder(newpath)
                                if not collectImage :
                                    if name not in savedList :
                                        savedList.append(name)
                                else :
                                    savedList.append(img)
                                    # imgcop = img.copy()
                                    # mask = imageToMask(imgcop)
                                    # img = Image.alpha_composite(img,mask)
                                img.save(newpath+str(count)+"."+it[0]+"."+name+"."+str(x)+"."+str(y)+".png","PNG")
                            else :
                                pass
            else :
                pass
            count = count + 1
        return savedList


            
    def getImageObj(self,name,rotationNum=4,variant=1) :
        imgList = []
        mat = selOneMaterial(self.matConfList,"Object",name)
        if mat!=None :
            for x in range(rotationNum) :
                img,name = self.imageFromMat(mat,x,variant)
                if img!=None :
                    imgList.append(img) 
        return list(imgList)
    
    def getImageObjReplaceColor(self,name,rotationNum=4,variant=1,hexColor=None,forceSize=[0,0]) :
        imgList = self.getImageObj(name,rotationNum,variant)
        if forceSize==[0,0] and hexColor==None :
            return imgList
        else :
            imgListTemp = []
            if hexColor!=None : 
                rgbcolor = ImageColor.getcolor(hexColor, "RGB")
                rgbacolor = rgbcolor + (255,)
                count = 0
                for img in imgList :
                    imgcop = img.copy()
                    imgcop.resize((forceSize[0],forceSize[1]), resample=self.resampleList[self.resampleSelection])
                    imgcop = imageToMask3(imgcop,rgbacolor)
                    #imgcop = Image.alpha_composite(img,mask)
                    imgListTemp.append(imgcop) 
                    count = count +1
            else :
                imgListTemp = imgList
            imgListTemp2 = []
            if forceSize!=[0,0] :
                for img in imgListTemp :
                    imgcop = img.copy()
                    imgcop.resize((forceSize[0],forceSize[1]), resample=self.resampleList[self.resampleSelection])
                    #imgcop2 = imgcop.filter(ImageFilter.BoxBlur(1)) 
                    #imgcop2 = imgcop.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)) 
                    #imgcop2 = imgcop.filter(filter=ImageFilter.EDGE_ENHANCE)
                    #imgcop2 = imgcop.filter(filter=ImageFilter.EDGE_ENHANCE_MORE)
                    imgListTemp2.append(imgcop)
            else :
                imgListTemp2 = imgListTemp

            return imgListTemp2

    def getObjListName(self,itemList,extraPropertyList=["SpriteVariants"]) :
        nameList = []
        for it in itemList :
            mat = selOneMaterial(self.matConfList,it[0],it[1])
            #print(mat)
            newdict = {}
            newdict["Name"] = mat["Name"]
            if extraPropertyList==["SpriteVariants"] :
                SpriteVariants = int(self.stat_df[self.stat_df["Name"]==it[1]]["VarNum"].values[0])
                newdict["SpriteVariants"] = SpriteVariants
                nameList.append(newdict)
            elif extraPropertyList!=[] :
                for pro in extraPropertyList :
                    if pro in mat.keys() :
                        newdict[pro] = castField(mat[pro])
                    else :
                        newdict[pro] = 1
                    nameList.append(newdict)
        return nameList

    def getImgFromSprite(self,obj) :
        if obj!=None :
            objValList = list(obj.values())
            img, scale = getImageFromList(self.spriteImageList,objValList[7])
            rottype = objValList[5]
            xoff = 0
            yoff = 0
            box = ([(obj["x"]+obj["w"]*xoff)*scale,
                (obj["y"]+obj["h"]*yoff)*scale,
                (obj["x"]+obj["w"]*(xoff+1))*scale,
                (obj["y"]+obj["h"]*(yoff+1))*scale])
            imgcropped = img.crop(box)
            return imgcropped

    def getImgFromSprite2(self,file,posX,posY,width,height,offx,offy,transType,isTile=False) :
        img, scale = getImageFromList(self.spriteImageList,file)
        if img!=None :
            box = ([(posX+offx)*scale,
                (posY+offy)*scale,
                (posX+width+offx)*scale,
                (posY+height+offy)*scale])
            imgcropped = img.crop(box)
            if transType != "" :
                if transType == "lr":
                    imgcropped = imgcropped.transpose(Image.FLIP_LEFT_RIGHT)
                elif transType == "tb":
                    imgcropped = imgcropped.transpose(Image.FLIP_TOP_BOTTOM)
                elif transType == "90":
                    width, height = switchValues(width,height)
                    imgcropped = imgcropped.transpose(Image.ROTATE_90)
                elif transType == "180":
                    imgcropped = imgcropped.transpose(Image.ROTATE_180)
                elif transType == "-90" or transType == "270":
                    width, height = switchValues(width,height)
                    imgcropped = imgcropped.transpose(Image.ROTATE_270)

            if self.resizeTile and isTile :
                 imgcropped = imgcropped.resize((int(self.tileSize),int(self.tileSize)), resample=self.resampleList[self.resampleSelection])
            if self.resizeElse and not isTile :
                imgcropped = imgcropped.resize((int(width*scale*float(self.elseSizePct)),int(height*scale*float(self.elseSizePct))), resample=self.resampleList[self.resampleSelection])
            return imgcropped
        else :
            return None

    def getSpriteFromMatList(self,materialList) :
         spList = []
         for mat in materialList :
             if type("")!=type(mat) :
                 spmat = self.getSpriteFromMat(mat)
                 if spmat!=None :
                     sp = spmat
                     spList.append(sp)
         return spList
    

    def spriteNameListFromSpriteList(self,spriteList,removeNumber=False,removeToolbar=False):
        nameList = []
        for sp in spriteList :
            if sp!=None :
                if "Name" in sp.keys() :
                    name = sp["Name"]
                    if removeNumber :
                        name = removeNumberString(name)
                    if removeToolbar :
                        name = name.replace("Toolbar","")
                    nameList.append(name)
        return nameList
                    
                    
    def getSpriteFromMat(self,material) :
        spriteObj = None
        spriteObjTool = None
        spriteObjStack = None
        spriteType = None#SpriteVariants
        numSprite = None
        spriteVarient = None
        stackFlag=False
        spriteCooList = []
        properties = []
        if "Sprite" in material.keys() :
            spriteObj = self.getSpriteConfFromName(material["Sprite"])
        if "ToolbarSprite" in material.keys() :
            spriteObjTool = self.getSpriteConfFromName(material["ToolbarSprite"])
        if "StackSprite" in material.keys() :
            spriteObjStack = self.getSpriteConfFromName(material["StackSprite"])
            stackFlag = True
        if "SpriteBank" in material.keys() :
            if "Sprite"in material["SpriteBank"].keys() :
                spriteObj = self.getSpriteConfFromName(material["SpriteBank"]["Sprite"])
            if "ToolbarSprite"in material["SpriteBank"].keys() :
                spriteObjTool = self.getSpriteConfFromName(material["SpriteBank"]["ToolbarSprite"])
            if "StackSprite"in material["SpriteBank"].keys() :
                spriteObjStack = self.getSpriteConfFromName(material["SpriteBank"]["StackSprite"])
                stackFlag = True
        if "SpriteType" in material.keys() :
            spriteType = material["SpriteType"]
        if "Properties" in material.keys() :
            properties = material["Properties"]
        if "NumSprites" in material.keys() :
            numSprite = material["NumSprites"]
        if "SpriteVariants" in material.keys() :
            spriteVarient = int(material["SpriteVariants"])
        if numSprite != None :
            for i in range(int(numSprite)) :
                sprString = "Sprite"+str(i)
                if sprString in material :
                    spriteCooList.append(material[sprString])
        return spriteObj,spriteObjTool,spriteObjStack,spriteType,spriteVarient,spriteCooList,properties
    
    def getSpriteConfFromName(self,name) :
        for sp in self.spriteConfList :
            if sp["Name"]==name:
                return sp
        return None
    
    def imageFromMatList(self,materialList,orientationList=[],variantList=[],orientationRange=1,variantRange=1,infodf=None) :
        imageList = []
        useAllLists = True
        defor = 0
        defvar = 0
        count = 0
        masterVariantRange = 1
        masterOrientationRange = 1
        if variantRange == -1 and type(infodf) != type(None) :
            masterVariantRange = -1
        else :
            masterVariantRange = variantRange
        if type(materialList)!=type([]) :
            materialList = [materialList]
        if not(len(materialList) == len(orientationList) and len(materialList) == len(variantList)) :
            useAllLists = False 
        for i in range(len(materialList)) :
            spriteMat = []
            masterVariantRangeForEle = masterVariantRange
            if masterVariantRange == -1 :
                masterVariantRangeForEle = int(infodf.loc[infodf["Name"]==materialList[i]["Name"]]["VarNum"].values[0])
            if orientationRange == -1 :
                matType = infodf.loc[infodf["Name"]==materialList[i]["Name"]]["Type"].values[0]
                if matType == "Material" :
                    masterOrientationRange = 1
                else :
                    masterOrientationRange = 4
            else :
                masterOrientationRange = orientationRange
            if not useAllLists :
                for y in range(masterVariantRangeForEle) :
                    spriteList = []
                    for x in range(masterOrientationRange) :
                        for seting in self.settingsList :
                            #if seting == [False,True]: # or seting == [False,False]: # or seting == [False,False]: #
                            img,name = self.imageFromMat(materialList[i],x,y,seting[0],seting[1])
                            if img!=None :
                                imageList.append(img)
                                if type(infodf) != type(None) :
                                    spriteList.append(count)
                                count = count + 1
                    if spriteList != [] :
                        spriteMat.append(spriteList)
            if type(infodf) != type(None) :
                indexNum = int(infodf[infodf["Name"]==materialList[i]["Name"]].index[0])
                if spriteMat != [] :
                    infodf.at[indexNum,"spList"] = spriteMat
                else :
                    infodf.at[indexNum,"spList"] = spriteMat
        if type(infodf) != type(None) :
            return imageList, infodf
        else :
            return imageList
    def imageFromMat(self,material,orientation=0,variant=0,tool=False,stack=False,returnMaxVar=False) :
        spriteObj,spriteObjTool,spriteObjStack,spriteType,spriteVarient,spriteCooList,properties = self.getSpriteFromMat(material)
        selectedSprite = spriteObj
        spriteVarientList = ["Corner","Cross","TJunction","Terminator","_Frozen","_FrozenCorner","_FrozenCross","_FrozenTJunction","_FrozenTerminator","_Lagged","_LaggedCorner","_LaggedCross","_LaggedTJunction","_LaggedTerminator","Digging","Sitting","Sleeping","_1","_2","_3","_4","Decorated"]
        valConf = True
        body = False
        isMaterial = False
        nameList = []
        offx = 0
        offy = 0
        posX = 0
        posY = 0
        width = 1
        height = 1
        file = ""
        if tool :
            if spriteObjTool != None :
                if variant == 0:
                    selectedSprite = spriteObjTool
                    
                else :
                    valConf = False
            else :
                valConf = False
        if stack :
            if spriteObjStack != None :
                selectedSprite = spriteObjStack
                spriteVarient = 3
            else :
                valConf = False
                spriteVarient = None
        if spriteType!=None and not stack:
            spriteVarient = 1
            if (spriteType == "RandomArea" or spriteType == "AlignedArea") and len(spriteCooList)==2: 
                file = "tilesetpadded"
                posX = spriteCooList[0]["x"]
                posY = spriteCooList[0]["y"]
                offx = int(variant%(spriteCooList[1]["x"]))
                offy = int(variant/(spriteCooList[1]["x"]))
                if spriteCooList[1]["y"]<=offy :
                    valConf = False
                isMaterial = True
                spriteVarient = (spriteCooList[1]["x"])*(spriteCooList[1]["y"])
            elif spriteType == "Connected" or spriteType == "SpecialRubble" :
                file = "tilesetpadded"
                posX = spriteCooList[0]["x"]
                posY = spriteCooList[0]["y"]
                offx,offy = connectedSelection(variant)
                if offx==None or offy==None :
                    valConf = False
                isMaterial = True
                spriteVarient = 23
            elif spriteType == "SingleSprite" or spriteType == "Linked" or spriteType == "ChoosableSingle" :
                file = "tilesetpadded"
                if len(spriteCooList) > variant :
                    posX = spriteCooList[variant]["x"]
                    posY = spriteCooList[variant]["y"]
                else :
                    valConf = False
                spriteVarient = len(spriteCooList)
                isMaterial = True
            else :
                pass
        if not isMaterial and not stack:  
            if 'Head' in properties and "FromFig" in material["Name"]:
                spriteVarientList = figList
            elif 'Body' in properties and "FromFig" in material["Name"]:
                spriteVarientList = figList
                body=True
    
            if spriteVarient == None :
                spriteVarient = 1
            nameList = []
            if selectedSprite!=None :
                nameList = [selectedSprite["Name"]]
                nameList2 = self.getAllPossibleSpriteName(selectedSprite["Name"],spriteVarientList)
                if selectedSprite["Name"] in nameList2 :
                    nameList2.remove(selectedSprite["Name"])
                nameList = nameList + nameList2
            else :
                if not stack :
                    if "Sprite" in material.keys() :
                        nameList = self.getAllPossibleSpriteName(material["Sprite"],spriteVarientList)
                    else :
                        if "SpriteBank" in material.keys() :
                            if "Sprite" in material["SpriteBank"].keys() :
                                nameList = self.getAllPossibleSpriteName(material["SpriteBank"]["Sprite"],spriteVarientList)
                else :
                    if "StackSprite" in material.keys() :
                        nameList = self.getAllPossibleSpriteName(material["StackSprite"],spriteVarientList)
                    else :
                        if "SpriteBank" in material.keys() :
                            if "StackSprite" in material["SpriteBank"].keys() :
                                nameList = self.getAllPossibleSpriteName(material["SpriteBank"]["StackSprite"],spriteVarientList)
            if nameList == [] :
                spriteVarient = 1
                valConf = False
            else :
                spriteVarient = len(nameList)
                #print(spriteVarient)
            #if variant != 0 :
                #if material["Name"]=="FaceSon" :
                    #print(nameList)
                if variant < spriteVarient:
                    #print()
                    selectedSprite = self.getSpriteConfFromName(nameList[variant])#-1
                else :
                    valConf = False
                if selectedSprite==None :
                    valConf = False
        if returnMaxVar :
            return spriteVarient
        if isMaterial and valConf :
            return self.getImgFromSprite2(file,posX,posY,width,height,offx,offy,"",True),material["Name"]
        elif selectedSprite!=None and valConf:
            return self.getImgFromSpriteObj(selectedSprite,orientation,body),selectedSprite["Name"]
        else :
            return None,None
            
    def getAllPossibleSpriteName(self,spName,spriteVarientList) :
        retList = []
        if spName[-2:]=="01" :
            spName = spName[:-2]
        if spName[-1:]=="1" :
            spName = spName[:-1]
        if spName[-1:]=="0" :
            spName = spName[:1]
        for i in range(50) :
            if spName+str(i) in self.objNameList :
                retList.append(spName+str(i))
        for i in range(10) :
            if spName+"0"+str(i) in self.objNameList :
                retList.append(spName+"0"+str(i))
        for spv in spriteVarientList :
            if spName+str(spv) in self.objNameList :
                retList.append(spName+str(spv))
        return retList
    
    def getImgFromSpriteObj(self,spriteObj,orientation=0,body=False):
        if spriteObj==None :
            return None
        offx = 0
        offy = 0
        posX = 0
        posY = 0
        width = 1
        height = 1
        file = ""
        transType = ""
        supportedRot = [0,1,2,3,4,6,7,8,11]
        posX = spriteObj["x"]
        posY = spriteObj["y"]
        width = spriteObj["w"]
        height = spriteObj["h"]
        rotType = spriteObj["RotateType"]
        file = spriteObj["file"]
        if rotType in supportedRot :
            if rotType == 0 :
                if orientation==1 :
                    transType="90"
                if orientation==2 :
                    transType="180"
                if orientation==3 :
                    transType="-90"
            if rotType == 1 or rotType == 3:
                if orientation==1 :
                    offx = offx + width
                if orientation==2 :
                    offx = offx + width*2
                    if rotType == 1 :
                        offy = offy + height -width
                        width, height = switchValues(width,height)
                if orientation==3 :
                    offx = offx + width*2
                    if rotType == 1 :
                        offy = offy + height -width
                        width, height = switchValues(width,height)
                    transType = "lr"
            if rotType == 2 or rotType == 11 :
                if orientation==2 :
                    offx = offx + width
                    offy = offy + height -width
                    width, height = switchValues(width,height)
                        
                if orientation==3 :
                    offx = offx + width
                    offy = offy + height -width
                    width, height = switchValues(width,height)
                    transType = "lr"
            if rotType == 6 :
                if orientation==0 :
                    offx = offx - width*5
                if orientation==1 :
                    offx = offx - width*1
                if orientation==2 :
                    offx = offx - width*7
                if orientation==3 :
                    offx = offx - width*3
            if rotType == 7 :
                if orientation==1 :
                    offy = offy - height
                if orientation==2 :
                    offx = offx + width
                    offy = offy + height - width
                    width, height = switchValues(width,height)
                if orientation==3 :
                    offx = offx + width
                    offy = offy + height - width*2
                    width, height = switchValues(width,height)
            if rotType == 8 :
                if orientation==1 :
                    offy = offy - height
                if orientation==2 :
                    offx = offx + width
                if orientation==3 :
                    offy = offy - height
                    offx = offx + width
            if body :
                offx = offx - width*3
            return self.getImgFromSprite2(file,posX,posY,width,height,offx,offy,transType)
        else :
            return None
        
    def pilImageToPygameImage(self,image,posX=0,posY=0) :
        if image!=None :
            mode = image.mode
            print(mode)
            size = image.size
            print(size)
            data = image.tobytes()
            py_image = pygame.image.fromstring(data, size, mode)
            rect = py_image.get_rect()
            print(rect)
            rect.left = posX
            rect.top = posY
            return py_image,rect
        else :
            return None,None
        
    def pilImageToPygameImage2(self,image,sizeMulti=1) :
        if image!=None :
            mode = image.mode
            size = image.size
            size2 = (int(size[0]*sizeMulti),int(size[1]*sizeMulti))
            data = image.tobytes()
            py_image = pygame.image.fromstring(data, size, mode)
            py_image = pygame.transform.scale(py_image, (size2[0], size2[1]))
            #py_image = py_image.convert_alpha()
            return py_image
        else :
            return None
        
    def pilImageToPygameImageList(self,imageList,posList=None) :
        imgRectList = []
        if posList == None :
            posList = [[(x%35)*35,int(x/35)*35] for x in range(len(imageList))]
        for i in range(len(imageList)) :
            py_image,rect = self.pilImageToPygameImage(imageList[i],posList[i][0],posList[i][1])
            if py_image!=None :
                imgRectList.append([py_image,rect])
        return imgRectList
    
    def getPygameImageList(self,imageList) :
        pgimgList = []
        for i in range(len(imageList)) :
            py_image = self.pilImageToPygameImage2(imageList[i])
            if py_image!=None :
                pgimgList.append(py_image)
        return pgimgList
    
    
def switchValues(val1,val2) :
    return val2, val1

def connectedSelection(val) :
    posX=val%7
    posY=int(val/7)
    if posY==3 :
        posX = posX+2
        if posX>3 :
            posX=None
            posY=None
    return posX,posY

            
def generateJsonList(filenameList,inputPath,outputFolder,extention) :
    for filename in filenameList :
        dictionary = generateJson(filename,inputPath,extention)
        saveDict(dictionary,inputPath+"/"+outputFolder,filename,"json")

def generateJson(filename,inputPath,extention) :
    file = openFile(inputPath,filename,extention)
    mastertestdict = getDictFromFile(file,extention,filename)
    return mastertestdict


    
def seleMaterial(matlist,category=["Object"],filterBy="MadeOf",filterVal="Wood",excludeList=""):
    retList = []
    for cat in category :
        for ele in matlist[cat] :
            if filterBy==None or filterVal==None :
                if "Name" in ele.keys() :
                    retList.append([cat,ele["Name"]])
            else :
                if filterBy in ele.keys() and "Name" in ele.keys() :
                    if type(ele[filterBy])==type([]) :
                        if filterVal in ele[filterBy] and excludeList not in ele[filterBy]:
                            retList.append([cat,ele["Name"]])
                    else :
                        if filterVal in ele[filterBy] :
                            retList.append([cat,ele["Name"]])
            
    return retList





def selOneMaterial(matlist,category="Object",name="Accountant") :
    if category in matlist.keys() :
        for ele in matlist[category] :
            if "Name" in ele.keys() :
                if name==ele["Name"] :
                    return ele
    return None
            

def imageToMask(img,transparentCol=(0,0,0,0),targetCol=(255,255,255,255),fillCol=(249, 163, 125, 150)) :
    data = img.getdata()
    newData = []
    avgScherold = 0.7
    for item in data:
        if item[3] > 10 :
            totalDif = abs(item[0]-targetCol[0])+abs(item[1]-targetCol[1])+abs(item[2]-targetCol[2])
            totalDif2 = abs(item[0]-item[1])+abs(item[0]-item[2])+abs(item[1]-item[2])
            totalDif3 = abs(abs(item[0]-targetCol[0])-abs(item[1]-targetCol[1]))+abs(abs(item[0]-targetCol[0])-abs(item[2]-targetCol[2]))+abs(abs(item[1]-targetCol[1])-abs(item[2]-targetCol[2]))
            
            #avg = (totalDif/765)*0.7+(totalDif2/255)*0.3
            avg = (totalDif/765)*0.5+(totalDif2/255)*0.5
            #
            avg2 = math.pow((1-avg),2)
            if totalDif > 765-50 : #Black outline
                #newData.append((255,0,0,255))
                newData.append(transparentCol)
            elif totalDif < 50 : #Skin
                #newData.append((0,255,0,255))
                newData.append(fillCol[:3]+ (int(255*(1-avg)),))
            elif totalDif2 < 100 and totalDif < 250 : #skin outline
                #newData.append((int(fillCol[0]*avg2),int(fillCol[1]*avg2),int(fillCol[2]*avg2),255))#int(255*(1-avg))))
                #newData.append(fillCol[:3]+ (int(255*(1-(totalDif/1000))),))
                newData.append(fillCol[:3]+ (int(255),))
                #newData.append((255,255,255,255))
            else : #Beard and hair
                #newData.append((100,50,200,255))
                newData.append(transparentCol)
            # elif totalDif3 < 15 :
            #     newData.append((150,150,255,255))
            
            # else :
            #     newData.append(transparentCol)
                
            # avg = (totalDif/765)*0.5+(totalDif2/255)*0.5
            
            # if avg<avgScherold :
            #     avg2 = math.sqrt(1-(totalDif/765))#max((1-(totalDif/765))*2,1)#math.sqrt
            #     #newData.append(fillCol[:3]+ (int(255*(1-avg)),))#math.sqrt
            #     #avg = 1 - avg
            #    # newData.append((int(fillCol[0]*avg2),int(fillCol[1]*avg2),int(fillCol[2]*avg2),int(255*math.sqrt(1-avg))))#math.sqrt
            #     newData.append((int(fillCol[0]*avg2),int(fillCol[1]*avg2),int(fillCol[2]*avg2),int(255*math.pow(1-avg,2))))#math.sqrt
            # else :
            #     newData.append(transparentCol)
            
            
            # alphaCounter = alphaCounter + 1
            # if totalDif<dist :
            #     totalDifCount = totalDifCount + 1
            # if totalDif2<dist2:
            #     totalDif2Count = totalDif2Count + 1
            # if totalDif<dist and totalDif2<dist2 :
            #     newData.append(fillCol[:3]+ (item[3],))
            #     replaceFlag = True
            # else :
            #     if totalDif<35 and totalDif2<500 :
            #         newData.append((255,0,0,255))
            #     else :
            #         newData.append(transparentCol)
                
                #if counter%10==0 :
                #    print(totalDif2)
            #   print("item[3]:",item[3],"  totalDif:",totalDif,"  totalDif2:",totalDif2,"  rf:",replaceFlag)
            # counter = counter + 1
        else:
            newData.append(transparentCol)
        img.putdata(newData)
        # counter = counter + 1
        # if counter%10==0 :
        #     if replaceFlag :
        #         print(pct)
        #     if totalDif>700 :
        #         print(totalDif)
        
    #print("counter:",counter,"  tdc:",totalDifCount,"  tdc2",totalDif2Count,"  ac:",alphaCounter)
    return img

def imageToMask2(img,fillCol=(249, 163, 125, 150)) :
    data = img.getdata()
    newData = []
    whiteThrehold = 0.45
    blackThrehold = 0.2
    for item in data:
        if item[3] > 10 :
            colSum = item[0]+item[1]+item[2]
            if colSum>255*whiteThrehold*3 :
                newData.append(fillCol[:3]+ (int(colSum/3),))
            #if item[0]>(255*whiteThrehold) and item[1]>(255*whiteThrehold) and item[2]>(255*whiteThrehold) :
            #    newData.append(fillCol[:3]+ (int(colSum/3),))
            else :
                newData.append((0,0,0,0))
        else :
            newData.append((0,0,0,0))
        img.putdata(newData)
    return img

def imageToMask3(img,fillCol=(249, 163, 125, 150)) :
    width, height = img.size
    newData = []
    whiteThrehold = 0.7
    blackThrehold = 0.2
    for x in range(width):
        for y in range(height):
            coordinate = x, y
            item = img.getpixel(coordinate)
            if item[3] > 10 :
                colSum = item[0]+item[1]+item[2]
                totalDif = abs(item[0]-item[1])+abs(item[0]-item[2])+abs(item[1]-item[2])
                if colSum>255*0.5*3 :
                    img.putpixel((x, y), fillCol[:3]+ (int(colSum/3),))
                    #img.putpixel((x, y), (255,0,0,255))
                #elif colSum<255*blackThrehold*3 :
                    #img.putpixel((x, y), (0,0,0,255))
                elif item[0]>(255*whiteThrehold) and item[1]>(255*whiteThrehold) and item[2]>(255*whiteThrehold) :
                    img.putpixel((x, y), fillCol[:3]+ (int(colSum/3),))
                    #img.putpixel((x, y), (0,255,0,255))
                #elif totalDif<200 :
                    #img.putpixel((x, y), (0,0,255,255))
    return img

def createFolder(path) :
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

def dfToList(df,columnsList=[]) :
    if columnsList==[] :
        return []
    tempMat = []
    returnMat = []
    for col in columnsList:
        tempMat.append(list(df[col]))
    for i in range(len(tempMat[0])) :
        tempList = []
        for j in range(len(columnsList)) :
            tempList.append(tempMat[j][i])
        returnMat.append(tempList)
    return returnMat

def dfToDict(df,columnsList=[],columnsListRename=[]) :
    
    if columnsList==[] or (columnsListRename!=[] and len(columnsList)!=len(columnsListRename)) :
        return []
    tempMat = []
    returnDictList = []
    for col in columnsList:
        tempMat.append(list(df[col]))
    for i in range(len(tempMat[0])) :
        tempDict = {}
        for j in range(len(columnsList)) :
            tempDict[columnsListRename[j]] = tempMat[j][i]
        returnDictList.append(tempDict)
    return returnDictList
        
figList = [100294
        ,101059
        ,101646
        ,101906
        ,102722
        ,102798
        ,103155
        ,104292
        ,105139
        ,106569
        ,107617
        ,108741
        ,112492
        ,112790
        ,113432
        ,115003
        ,118474
        ,119715
        ,125987
        ,126461
        ,127257
        ,127280
        ,133813
        ,135616
        ,139546
        ,148599
        ,149554
        ,154063
        ,165219
        ,179008
        ,198804
        ,2
        ,214446
        ,218681
        ,224027
        ,228859
        ,292397
        ,3
        ,370087
        ,4
        ,41711
        ,46854
        ,5
        ,50590
        ,50771
        ,55062
        ,56295
        ,60080
        ,60741
        ,60787
        ,61059
        ,61370
        ,62307
        ,65274
        ,66457
        ,68853
        ,72094
        ,72986
        ,74173
        ,75791
        ,76678
        ,80569
        ,81147
        ,81374
        ,81428
        ,81601
        ,81682
        ,82533
        ,83037
        ,83710
        ,83918
        ,83944
        ,85363
        ,86934
        ,88222
        ,88430
        ,89046
        ,89538
        ,89905
        ,90601
        ,91147
        ,92146
        ,94122
        ,98223
        ,98442]
#sp = spriteLoader()