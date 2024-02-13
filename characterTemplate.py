# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:31:56 2023

@author: Alexandre
"""
import json

class characterTemplate :
    def __init__(self,pjPath="",charFile="",senFile="",readFromJson=False):#,pjPath="C:/Users/Alexandre/Desktop/PAshooter",charFile="charConfig.json",senFile="sentenceList.txt",readFromJson=False
        f = open(pjPath+"/"+charFile)
        configJson = json.load(f)
        self.nameListM = configJson.get("nameListM")
        self.nameListF = configJson.get("nameListF")
        self.characterDef = configJson.get("characterDef")
        self.sentenceList = []
        if readFromJson :
            self.sentenceList = configJson.get("sentenceList")
        else :
            f2 = open(pjPath+"/"+senFile)
            while True:
                line = f2.readline()
                if not line:
                    break
                self.sentenceList.append(str(line.strip()))