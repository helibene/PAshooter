# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:25:33 2023

@author: Alexandre
"""
import json

class configLoader :
    def __init__(self,jsonPath="C:/Users/Alexandre/Desktop/pa/config.json"):
        f = open(jsonPath)
        configJson = json.load(f)
        self.screenWidth = castValue(configJson.get("screenWidth"),"int")
        self.screenHeight = castValue(configJson.get("screenHeight"),"int")
        self.fullscreen = castValue(configJson.get("fullscreen"),"bool")
        self.windowOnTop = castValue(configJson.get("windowOnTop"),"bool")
        self.spritePath = castValue(configJson.get("spritePath"),"string")
        self.maxInventorySize = castValue(configJson.get("maxInventorySize"),"int")
        self.itemSize = castValue(configJson.get("itemSize"),"int")
        self.sleepPerFrame = castValue(configJson.get("sleepPerFrame"),"int")
        self.generateNewMap = castValue(configJson.get("generateNewMap"),"bool")
        self.distancePickupPixel = castValue(configJson.get("distancePickupPixel"),"int")
        self.startHealth = castValue(configJson.get("startHealth"),"int")
        self.maxBulletOnScreen = castValue(configJson.get("maxBulletOnScreen"),"int")
        self.sprintMultiplier = castValue(configJson.get("sprintMultiplier"),"int")
        self.weponFrameCooldown = castValue(configJson.get("weponFrameCooldown"),"int")
        self.peopleSpawnNum = castValue(configJson.get("peopleSpawnNum"),"int")
        self.peopleSpawnRangeX = castValue(configJson.get("peopleSpawnRangeX"),"list")
        self.peopleSpawnRangeY = castValue(configJson.get("peopleSpawnRangeY"),"list")
        self.peopleSpeedRange = castValue(configJson.get("peopleSpeedRange"),"list")
        self.peopleAttackRange = castValue(configJson.get("peopleAttackRange"),"list")
        self.peopleDamageMultiRange = castValue(configJson.get("peopleDamageMultiRange"),"list")
        self.objInitInstance = castValue(configJson.get("objInitInstance"),"int")
        self.myName = castValue(configJson.get("myName"),"string")
        self.mySprite = castValue(configJson.get("mySprite"),"int")
        self.myGender = castValue(configJson.get("myGender"),"string")
        self.myRandomName = castValue(configJson.get("myRandomName"),"bool")
        self.mySpeed = castValue(configJson.get("mySpeed"),"int")
        self.myPosition = castValue(configJson.get("myPosition"),"list")
        self.myHealth = castValue(configJson.get("myHealth"),"int")
        self.myDamageMulti = castValue(configJson.get("myDamageMulti"),"int")
        self.myAttackRange = castValue(configJson.get("myAttackRange"),"int")
        #self.myGender = castValue(configJson.get("myGender"),"string")
        #self.myGender = castValue(configJson.get("myGender"),"string")
        self.confVars = vars()


def castValue(val,valType) :
    if val==None :
        if valType=="int":
            return 0
        if valType=="string":
            return ""
        if valType=="list" :
            return []
    if valType=="bool":
        if val == 1 or val=="1" or val == "True" :
            return True
        elif val == 0 or val=="0" or val == "False" :
            return False
        else :
            return False
    return val

cl = configLoader()