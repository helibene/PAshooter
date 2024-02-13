# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 18:18:51 2023

@author: Alexandre
"""
import json 
import csv
import os
import re
from PIL import ImageTk,Image,ImageOps

class originalGameConfLoader:
    def __init__(self):
        pass
    
""" Open and save text files """

def openFile(path,filename,extention,disp=False) :
    with open(path+"/"+filename+"."+extention) as file:
        lines = [line.rstrip() for line in file]
    if disp :
        print("File '"+filename+"."+extention+"'  LOADED  (",len(lines),"lines)")
    return lines

def openJson(path,filename,extention,disp=True) :
    with open(path+"/"+filename+"."+extention) as file:
        data = json.load(file)
    return data

def saveDict(dictionary,path,filename,extention="json",indent=2,disp=False):
    with open(path+"/"+filename+"."+extention, 'w') as f:
        json.dump(dictionary, f, indent=indent)
    if disp :
        print("File '"+filename+"."+extention+"'  SAVED  (",len(dictionary),"dict entries)")
        
def saveList(list_save,path,filename,extention="txt",disp=False):
    with open(path+"/"+filename+"."+extention, 'w') as f:
        for ele in list_save :
            f.write(str(ele)+"\n")
    if disp :
        print("File '"+filename+"."+extention+"'  SAVED  (",len(list_save),"list entries)")

""" Open and save image files """

def openImageList(settingList,path) :
    for val in settingList :
        img = Image.open(path+val[0]+".png").convert("RGBA")
        val.append(img)
    return settingList

def getImageFromList(imgList,imgName) : #EXT
    for vallist in imgList :
        if vallist[0]==imgName :
            return vallist[2],vallist[1]
    return None,None

def openSpriteImageList(path="",spriteSheetList=[]) : #EXT
    imageList = openImageList(spriteSheetList,path)
    return imageList


""" Format txt and spritebank files """


def getDictFromFile(file,extention="txt",filename="") : #EXT
    if extention=="txt" :
        return getDictFromFileTXT(file,filename)
    elif extention=="spritebank" :
        return getDictFromFileSPRITE(file,filename)
    
def getDictFromFileTXT(lines,filename="") :
    line_count = 0 
    mastertestdict = {}
    currentKey = "none"
    while line_count < 100000 and line_count <len(lines):
        valid_instance=True
        if lines[line_count][0:5]=="BEGIN" :
            currentKey = lines[line_count][6:]
            line_count = line_count +1
            testdict = {}
            if currentKey not in mastertestdict.keys():
                mastertestdict[currentKey] = []
                
            while lines[line_count][0:3]!="END" and line_count<len(lines):       
                line = lines[line_count]
                if "None" not in line :
                    if "BEGIN" in line and not "END" in line :
                        if "BEGIN SpriteBank" in line :
                            testdict["SpriteBank"] = {}
                            line_count = line_count + 1
                            line = lines[line_count]
                            while "END" not in lines[line_count] and line_count<len(lines):   
                                line = reduceSpace(line).split(" ")
                                testdict["SpriteBank"][line[0]] = line[1]
                                line_count = line_count + 1
                                line = lines[line_count]
                    if "BEGIN" in line and "END" in line :
                        test = line.replace("BEGIN", "").replace("END", "")
                        test = reduceSpace(test).split(" ")
                        testdict[test[0]] = castDictionary(convertToDict(test[1:]))
                    else :
                        dictValList = reduceSpace(line).split(" ")
                        if len(dictValList)==2 :
                            if dictValList[1]!="None" :
                                if dictValList[0] not in testdict.keys():
                                    testdict[dictValList[0]] = dictValList[1]
                                else :
                                    if type(testdict[dictValList[0]])!=type([]) :
                                        testdict[dictValList[0]] = [testdict[dictValList[0]],dictValList[1]]
                                    else :
                                        testdict[dictValList[0]].append(dictValList[1])
                            else :
                                valid_instance = False
                else :
                    valid_instance = False
                line_count = line_count +1
            if "Room" not in currentKey and valid_instance:
                mastertestdict[currentKey].append(testdict)
        line_count = line_count +1
    return mastertestdict

def getDictFromFileSPRITE(lines,filename="") :
    line_count = 0 
    mastertestdict = {}
    currentKey = "none"
    while line_count < 10000 and line_count <len(lines):
        line = lines[line_count]
        if line[0:5]=="BEGIN" and "Size 0  END" not in line :
            currentKey = line[5:].replace(" ","")
            mastertestdict[currentKey] = []
        if '    BEGIN "[i ' in line :
            if '"Medical Supplies"' in line :
                line = line.replace('"Medical Supplies"', 'Medical_Supplies')
            line = line.replace('    BEGIN "[i ','').replace(']"','').replace('END','').replace('"','')
            line = reduceSpace(line).split(" ")
            dictinoary = castDictionary(convertToDict(line[1:]))
            mastertestdict[currentKey].append(dictinoary)
        line_count = line_count +1
    return mastertestdict

def reduceSpace(line):
    line = line.replace("\t"," ")
    for i in range(1,19) :
        line = line.replace(str(" "*(20-i)),str(" "*(19-i)))
    if len(line)>0 :
        if line[0]==" " :
            line = line[1:]
        if line[-1]==" " :
            line = line[:-1]
    return line

def convertToDict(list_to_dict):
    it = iter(list_to_dict)
    res_dct = dict(zip(it, it))
    return res_dct

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def isbool(num):
    if num=="True" or num=="true" :
        return True
    if num=="False" or num=="false" :
        return False
    return None

def castField(val) :
    if isint(val) :
        return int(val)
    if isfloat(val) :
        return float(val)
    if isbool(val)!=None :
        return isbool(val)
    return val

def castDictionary(dictionary) :
    for dictKey in dictionary.keys() :
        dictionary[dictKey] = castField(dictionary[dictKey])
    return dictionary

def removeNumberString(string) :
    pattern_order = r'[0-9]'
    ret_str = re.sub(pattern_order, '', string)
    return ret_str

""" Data preparation and metadata implementation """

def generateJsonList(filenameList,inputPath,outputFolder,extention) : #EXT
    for filename in filenameList :
        dictionary = generateJson(filename,inputPath,extention)
        saveDict(dictionary,inputPath+"/"+outputFolder,filename,"json")

def generateJson(filename,inputPath,extention) :
    file = openFile(inputPath,filename,extention)
    mastertestdict = getDictFromFile(file,extention,filename)
    return mastertestdict

def joinMaterial(materialList) :
    retDict = materialList[0]
    for material in materialList[1:] :
        for matkey in retDict.keys() :
            if matkey in material.keys() :
                for matkeykey in material[matkey] :
                    retDict[matkey].append(matkeykey)
    return retDict

def openMaterialList(path="") : #EXT
    mat1 = generateJson("materials",path,"txt")
    mat2 = generateJson("materials_dlc",path,"txt")
    mat3 = openJson(path,"materials_edit","json")
    mat_ret = joinMaterial([mat1,mat2,mat3])
    mat_ret = addSubcategoryToMatList(mat_ret)
    return mat_ret


def addFilenameToDictList(dictonaryList,filenameList,selectKey="Sprites",filenameFieldName="file",extraMapping=[]) :
    for i in range(len(filenameList)) :
        dictonaryList[i] = addFilenameToDict(dictonaryList[i],filenameList[i],selectKey,filenameFieldName,extraMapping)

def addFilenameToDict(dictonary,filename,selectKey="Sprites",filenameFieldName="file",extraMapping=[]):
    if selectKey!=None :
        dictonary = dictonary[selectKey]
    if filename!=extraMapping[2] :
        for dictele in dictonary :
            dictele[filenameFieldName] = filename
    else :
        for dictele in dictonary :
            if dictele["x"]>=64 :
                dictele["x"] = dictele["x"] -64
                dictele[filenameFieldName] = extraMapping[0]#"special-entities"
            elif dictele["y"]>=64 :
                dictele["y"] = dictele["y"] -64
                dictele[filenameFieldName] = extraMapping[1]
            else :
                dictele[filenameFieldName] = extraMapping[2]
    return dictonary
        
def addSubcategoryToMatList(matlist,category=["Object","Material","Equipment"]):
    for cat in category :
        for ele in matlist[cat] :
            subCat = "Other"
            if "Properties" in ele.keys() :
                properties = ele["Properties"]
                if type(properties) == type("") :
                    properties = [properties]
                if "Material" in properties :
                    subCat = "Material"
                if "StaticObject" in properties :
                    subCat = "StaticObject"
                if "Entity" in properties :
                    subCat = "Entity"
                if "Vehicle" in properties :
                    subCat = "Vehicle"
                if "IsFoundationWall" in properties :
                    subCat = "IsFoundationWall"
                if "HeatWaveAffected" in properties :
                    subCat = "HeatWaveAffected"
                if "NoImport" in properties :
                    subCat = "NoImport"
                if "Weapons" in properties :
                    subCat = "Weapons"
                if "Narcotics" in properties :
                    subCat = "Narcotics"
                if "Tools" in properties :
                    subCat = "Tools"
            if "SpriteType" in ele.keys() :
                SpriteType = ele["SpriteType"]
                if SpriteType=="Connected" :
                    subCat = "Connected"
                if SpriteType=="RandomArea" :
                    subCat = "RandomArea"
                if SpriteType=="AlignedArea" :
                    subCat = "AlignedArea"
            if "MadeOf" in ele.keys() :    
                if ele["MadeOf"]=="Wood" :
                    subCat = "Wood"
                if ele["MadeOf"]=="Composite" :
                    subCat = "Composite"
            if "Filter" in ele.keys() :    
                if ele["Filter"]=="Foliage" :
                    subCat = "Foliage"
                if ele["Filter"]=="Work" :
                    subCat = "Work"
                if ele["Filter"]=="Decoration" :
                    subCat = "Decoration"
                if ele["Filter"]=="Catering" :
                    subCat = "Catering"
            ele["SubCategory"] = subCat
    return matlist


def getListAllSpriteConf(path="",dictFilenameList=[],imageList=[],extraMapping=[]) : #EXT
    dictList = []
    for i in range(len(dictFilenameList)) :
        ele = generateJson(dictFilenameList[i],path,"spritebank")["Sprites"]
        dictList.append(ele)
    addFilenameToDictList(dictList,imageList,None,"file",extraMapping)
    dictList2 = []
    for dicti in dictList :
        for ele in dicti :
            dictList2.append(ele)
    return dictList2

def spriteNameListFromSpriteList(spriteList,removeNumber=False,removeToolbar=False):
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