# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:28:55 2023

@author: Alexandre
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:27:32 2022

@author: Alexandre
"""
import tkinter as tk
from tkinter import *  
from PIL import ImageTk,Image  
import time
import math 
import colorsys
import sys
from PIL import ImageGrab
import os
import numpy as np
import windowUtil as wu
from tkinter import ttk
import spriteLoader as sl
sys.setrecursionlimit(100000000)
import json 
from tkinter.font import Font

class chaSelector :
    def __init__(self,path="C:/Users/Alexandre/Desktop/PAshooter/newVars"):

        width = 600
        height = 550
        fullscreen = False
        self.paddings = {'padx': 6, 'pady': 6,'ipadx': 1, 'ipady': 1}
        #self.paddings = {'padx': 0, 'pady': 0,'ipadx': 0, 'ipady': 0}
        self.resampleList = [Image.ANTIALIAS,Image.NEAREST,Image.BILINEAR,Image.BICUBIC,Image.LANCZOS]
        self.bodyAloneSize = 80#96
        self.bodySize = 80#80
        self.headSize = 40#64
        self.bodySizeIncrement = 7
        self.headSizeIncrement = 4
        self.borderList = ["flat","solid","raised","sunken","ridge","groove"]
        self.dropDownWidth = 20
        self.dropDownHeight = 1
        self.spinWidth = 12
        self.borderwidthDrop = 4
        self.borderwidthSpin = 4
        self.borderReliefDrop = self.borderList[2]
        self.borderReliefSpin = self.borderList[2]
        self.borderColor = "black"
        self.highlightColor = "#19194d"
        self.borderwidth = 2
        self.imageList = []
        self.spload = sl.spriteLoader()
        #self.spload.generateSpecForCharaSel(path,"chaSelSetting")
        self.spload.generateSpecForCharaSel2(path,"chaSelSetting")
        settingDict = openJson(path,"chaSelSetting","json")
        self.openMasterdict(settingDict)
        self.radioFlag = False
        self.chaPresetVariantEnable = False
        self.canvasWidth = 600
        self.canvasHeight = 300
        self.gridXPreset = 0
        self.gridYPreset = 0
        self.backgroundColor = "white"
        self.defaultSelectorColor = "#f2f2f2"
        self.defaultSelectorColorFG = "#000000"
        self.defaultSelectorColorDisable = "#8c8c8c"
        self.defaultSelectorColorDisableFG  = "#595959"
        self.root,self.width,self.height = wu.setRoot(None,width,height,0,0,True,fullscreen,True,False) 
        self.canvas = wu.getCanvasFullScreen(None,self.root,self.canvasWidth,self.canvasHeight,self.backgroundColor)
        self.menu = Canvas(self.root, width = 600, height = 250, bg=self.backgroundColor)

        self.labelList=["Cha setting","Category","Type","Head setting","Body setting","Head type","Body type","Head gender","Body gender","Head setting","Body setting","Skin color","Clothes","Clothes color","Wearable","Head size","Body size","x","x"]
        self.labelCount = 0
        self.dropDict = {"WearableHead":9,"WearableBody":10,"WearableOther":11}
        self.dropdownListName = [["Preset","Custom"],self.presetHumainListSingleNm,["Preset","Custom"],["Preset","Custom"],["Male","Female"],["Male","Female"],list(skinColorList.keys()),["Clothes","Naked"],["white","black"],self.customWearableHeadListNm,self.customWearableBodyListNm,self.customWearableOtherListNm]
        self.dropdownList = []
        self.dropdownListObj = []
        self.dropdownListVarList = []
        self.dropdownCount = 0
        
        self.spinboxListVar = [[1,4],[1,self.headPresetDict["SpriteVariants"]],[1,self.bodyPresetDict["SpriteVariants"]],[1,8],[1,16],[-5,5],[-5,5]]
        self.spinboxList = []
        self.spinboxListObj = []
        self.spinboxCount = 0
        
        self.radioListName = [["Single","Category","Warden","Dog"]]
        self.radioList = []
        self.radioListVar = []
        self.radioListObj = []
        self.radioCount = 0
        

        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("r")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("p")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("d")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("p")
        self.addWidget("l")
        self.addWidget("p")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("d")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("p")
        self.addWidget("l")
        self.addWidget("p")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("d")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("d")
        
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("p")
        self.addWidget("l")
        self.addWidget("p")
        self.rootModif(0,0,True)
        self.addWidget("l")
        self.addWidget("d")
        self.addWidget("l")
        self.addWidget("d")
        
        self.reset_option_menu(1,self.presetHumainListSingleNm,0)
        #self.canvas.create_text(10,10, text="lldqsmdfcdwxcdgv", fill="orange", font=("Helvetica 10 bold"))
        self.menu.pack(expand=False,anchor="n")
        self.canvas.pack(expand=False,anchor="n")
        self.root.update()
        self.menuTrigger()
        self.root.mainloop() 
    
    
    def menuTrigger(self,choice=None) :
        
        radioList = []
        
        for radio in self.radioListVar :
            radioList.append(radio.get())
        print(radioList)
        if self.radioFlag : 
            if radioList[0]=='0' :
                self.disableScale([0],[])
                self.reset_option_menu(1,self.presetHumainListSingleNm,0)
                self.chaPresetVariantEnable = False
            if radioList[0]=='1' :
                self.disableScale([],[0])
                self.reset_option_menu(1,self.presetHumainListCategoryNm,0)
                self.chaPresetVariantEnable = True
            if radioList[0]=='2' :
                self.disableScale([0],[])
                self.reset_option_menu(1,self.presetHumainListWardeneNm,0)
                self.chaPresetVariantEnable = False
            if radioList[0]=='3' :
                self.disableScale([],[0])
                self.reset_option_menu(1,self.presetDogListNm,0)
                self.chaPresetVariantEnable = True
            self.radioFlag = False
            
        dropList = []
        spinList = []
        self.imgListWearable = []
        self.imgListWearableHead = []
        self.imgListWearableBody = []
        
        for drop in self.dropdownList :
            dropList.append(drop.get())
        for spin in self.spinboxList :
            spinList.append(spin.get())
        skcolor = skinColorList[dropList[6]]
        if dropList[0]==self.dropdownListName[0][0] : #Character Preset
            tempList = [0]
            variantSelection = int(spinList[0])-1
            if not self.chaPresetVariantEnable :
                tempList = []
                variantSelection= 0
            self.disableDrop([2,3,4,5,6,7,8],[1])
            self.disableScale([1,2,3,4],tempList)
            self.imageList = self.spload.getImageObjReplaceColor(str(dropList[1]),4,variantSelection)#)
            #self.imageList.extend(self.spload.getImageObjReplaceColor(str(dropList[9]),4,variantSelection))#))#)
            #self.displayImageList()
        else : #Character Custom
            self.disableDrop([1],[2,3,4,5,6])
            self.disableScale([0],[1,2,3,4])
            self.imageList = []
            if dropList[2]==self.dropdownListName[2][0] : #Head Preset
                self.disableDrop([4,6],[])
                self.disableScale([3],[1])
                imgList = self.spload.getImageObjReplaceColor("HeadFromFig",4,int(spinList[1]))
                self.imageList.extend(imgList)
            else : #Head Custom
                self.disableDrop([],[4,6])
                self.disableScale([1],[3])
                headName, headNum = headSelector(self.headCustomDict[dropList[4]],int(spinList[3])-1)
                maxHead = headSelector(self.headCustomDict[dropList[4]],0,True)
                self.imageList.extend(self.spload.getImageObjReplaceColor(str(headName),4,headNum,skcolor,[self.headSize,self.headSize]))#)
                self.spinboxList[3].config(to=int(maxHead))
            if dropList[3]==self.dropdownListName[3][0] : #Body Preset
                self.disableDrop([5,7,8],[])
                self.disableScale([4],[2])
                self.imageList.extend(self.spload.getImageObjReplaceColor("BodyFromFig",4,int(spinList[2])))#)
            else :#Body custom
                self.disableDrop([],[5,7,8])
                self.disableScale([2],[4])
                spinNum = int(spinList[4])-1
                bodyName, bodyNum = bodySelector(self.bodyCustomDict[dropList[7]][dropList[5]],spinNum)
                maxBody = bodySelector(self.bodyCustomDict[dropList[7]][dropList[5]],0,True)
                self.imageList.extend(self.spload.getImageObjReplaceColor(str(bodyName),4,bodyNum,skcolor,[self.bodySize,self.bodySize]))#)
                self.spinboxList[4].config(to=int(maxBody))
                
                # if dropList[9]=="TattooBody" :
                #     print("loooooool")
                #     self.imgListWearable = self.spload.getImageObjReplaceColor(dropList[9],4,spinNum+1)#int(spinList[0])-1)
        
            if dropList[7]==self.dropdownListName[7][0] or dropList[3]==self.dropdownListName[3][0] :
                self.disableDrop([],[8])
            else :
                self.disableDrop([8],[])
            if dropList[2]==self.dropdownListName[2][1] or dropList[7]==self.dropdownListName[7][1]:
                self.disableDrop([],[6])
            else :
                self.disableDrop([6],[])
            
            headAndBody = False
            if len(self.imageList)>4 :
                headAndBody = True
            if dropList[self.dropDict["WearableHead"]] != "None" and headAndBody:
                name, num = getSplitName(dropList[self.dropDict["WearableHead"]])
                self.imgListWearableHead = self.spload.getImageObjReplaceColor(name,4,num)

            if dropList[self.dropDict["WearableBody"]] != "None" and headAndBody:
                if "error" not in dropList[self.dropDict["WearableBody"]] :
                    self.imgListWearableBody = self.spload.getImageObjReplaceColor(dropList[self.dropDict["WearableBody"]],4,0)#int(spinList[0])-1)

            # if dropList[7]==self.dropdownListName[7][0] or dropList[2]==self.dropdownListName[2][1] :
            #     self.disableDrop([8],[6])
            #     #naked=True
            # else :
            #     self.disableDrop([6],[8])
            #     #naked=True
            self.imageList = list(self.imageList)
                
            
        self.displayImageList()
        self.root.update()
    
    def menuTrigger2(self,choice=None) :
        self.radioFlag = True
        self.menuTrigger()
    def menuTrigger3(self,value) :
        self.dropdownList[1].set(value)
        self.menuTrigger()
        return value

    
    def openMasterdict(self,masterdict) :
        dv1 = ["Character","Wearable"]
        dv2 = ["Preset","Custom"]
        dv3 = ["HumainSingle","HumainCategory","Warden","Dog","Head","Body"]
        dv4 = ["Preset","Custom"]
        dv5 = ["Clothes","Naked"]
        dv6 = ["Male","Female"]
        
        dv22 = ["Head","Body","Other"]
        dv23 = ["Tattoo","Other"]
        
        self.presetHumainListSingleNm = dictListToList(masterdict[dv1[0]][dv2[0]][dv3[0]],"Name")
        self.presetHumainListCategoryNm = dictListToList(masterdict[dv1[0]][dv2[0]][dv3[1]],"Name")
        self.presetHumainListCategoryVar = dictListToList(masterdict[dv1[0]][dv2[0]][dv3[1]],"SpriteVariants")
        self.presetHumainListWardeneNm = dictListToList(masterdict[dv1[0]][dv2[0]][dv3[2]],"Name")
        self.presetDogListNm = dictListToList(masterdict[dv1[0]][dv2[0]][dv3[3]],"Name")
        self.presetWearableListNm = ["test"]#dictListToList(masterdict[dv1[1]],"Name")
        self.presetWearableListVar = [1]#dictListToList(masterdict[dv1[1]],"SpriteVariants")

        self.headPresetDict = masterdict[dv1[0]][dv2[1]][dv3[4]][dv4[0]][0]
        self.bodyPresetDict = masterdict[dv1[0]][dv2[1]][dv3[5]][dv4[0]][0]
        self.headCustomDict = masterdict[dv1[0]][dv2[1]][dv3[4]][dv4[1]]
        self.bodyCustomDict = masterdict[dv1[0]][dv2[1]][dv3[5]][dv4[1]]
        self.presetWearableListNm.insert(0, "None")
        self.presetWearableListVar.insert(0, 0)
        
        self.customWearableHeadListNm = dictListToIteList(masterdict[dv1[1]][dv22[0]][dv23[0]]+masterdict[dv1[1]][dv22[0]][dv23[1]])
        self.customWearableBodyListNm = dictListToIteList(masterdict[dv1[1]][dv22[1]][dv23[0]]+masterdict[dv1[1]][dv22[1]][dv23[1]],True)
        self.customWearableOtherListNm = dictListToList(masterdict[dv1[1]][dv22[2]],"Name")
        self.customWearableHeadListNm.insert(0, "None")
        self.customWearableBodyListNm.insert(0, "None")
        self.customWearableOtherListNm.insert(0, "None")
        print(self.customWearableOtherListNm)
        #self.customWearableBodyTatooDict = masterdict[dv1[1]][dv22[2]]
        #self.presetWearableListVar = dictListToList(masterdict[dv1[1]],"SpriteVariants")

        #print(self.bodyCustomDict)
    
    def addWidget(self,widgtype="l") :
        root, x, y = self.rootSelection()
        bd=0
        packGrid=True
        if widgtype=="l" : #Label
            text = self.labelList[self.labelCount]
            self.labelCount = self.labelCount +1
            w = tk.Label(root, text = text+" :",bd=bd,bg=self.backgroundColor,disabledforeground=self.defaultSelectorColorDisableFG,foreground =self.defaultSelectorColorFG,anchor="center",font=Font(family='Helvetica', size=10, weight='bold'))#, borderwidth=2, relief="groove")
        if widgtype=="d" : # Drop down Menu
            dropdownList = self.dropdownListName[self.dropdownCount]
            self.dropdownCount = self.dropdownCount +1
            variable = StringVar()
            variable.set(dropdownList[0])
            w = OptionMenu(root, variable,*dropdownList,command=self.menuTrigger)
            w.config(bd=bd,width=self.dropDownWidth,height=self.dropDownHeight,bg=self.defaultSelectorColor,disabledforeground =self.defaultSelectorColorDisableFG,foreground =self.defaultSelectorColorFG, borderwidth=self.borderwidthDrop, relief=self.borderReliefDrop,highlightbackground=self.borderColor,highlightthickness=self.borderwidth,highlightcolor=self.highlightColor)#width=15,height=1
            self.dropdownList.append(variable)
            self.dropdownListObj.append(w)
            self.dropdownListVarList.append(dropdownList)
        
        if widgtype=="b" : # Button
            w = Button(root, text = "Generate Curve" , command = self.menuTrigger,height=0)
            w.config(bg=self.defaultSelectorColor,pady=0,padx=0,borderwidth=0)
        
        if widgtype=="p" : # Spinbox
            max_range = self.spinboxListVar[self.spinboxCount]
            self.spinboxCount = self.spinboxCount +1
            from_val = 0
            if type(max_range) == type([]) :
                from_val = max_range[0]
                max_range = max_range[1]
            integer_variable  = tk.IntVar(0)
            w = Spinbox(root, from_=from_val, to=max_range,width=self.spinWidth, command = self.menuTrigger,textvariable=integer_variable,font=Font(family='Helvetica', size=10, weight='bold'),disabledbackground=self.defaultSelectorColorDisable,borderwidth=self.borderwidthSpin, relief=self.borderReliefSpin,bg=self.backgroundColor)#,activeforeground =self.highlightcolor)
            w.config(bg=self.defaultSelectorColor,disabledforeground=self.defaultSelectorColorDisableFG,foreground =self.defaultSelectorColorFG,highlightbackground=self.borderColor,highlightcolor=self.highlightColor,highlightthickness=self.borderwidth)
            self.spinboxList.append(w)
            
        
        if widgtype=="r" : # Radio
            packGrid=False
            nameList = self.radioListName[self.radioCount]
            self.radioCount = self.radioCount +1
            offset = 0
            offset2 = 0
            var = StringVar(None,0)
            stickyList = [tk.W,tk.W,tk.W]
            for i in range(len(nameList)) :
                w = Radiobutton(root, text = nameList[i], variable =var, value = i,command=self.menuTrigger2,bg=self.backgroundColor,activebackground=self.backgroundColor)
                w.config(highlightbackground=self.borderColor,highlightcolor=self.highlightColor,highlightthickness=self.borderwidth)
                if i >1  :
                    w.grid(column=x+1, row=y, sticky=tk.W,columnspan=len(nameList),padx=offset2+30)
                    offset2 = offset2 + len(nameList[i])*12
                else :
                    w.grid(column=x, row=y, sticky=tk.W,columnspan=len(nameList),padx=offset)
                    offset = offset + len(nameList[i])*10
                self.radioListObj.append(w)
            self.radioListVar.append(var)
            
        if packGrid :
            w.grid(column=x, row=y,sticky=tk.W,  **self.paddings)#sticky=tk.N,
        self.rootModif(1)

    
    def addSeparator(self) :
        root, x, y = self.rootSelection()
        paddings = {'padx': 5, 'pady': 0}
        label = tk.Label(root, text = " " ,height=2,bd=0,bg="black")
        
    def rootSelection(self):
        root = self.menu
        x = self.gridXPreset
        y = self.gridYPreset
        return root, x, y
    
    def rootModif(self,addx=0,addy=0,resetLine=False) :
        if resetLine :
            self.gridXPreset = 0
            self.gridYPreset = self.gridYPreset +1
        else :
            self.gridXPreset = self.gridXPreset +addx
            self.gridYPreset = self.gridYPreset +addy
    
    def actionFunction1(self,choice):
        self.able_disable(choice,0)
        
    def actionFunction2(self,choice):
        self.able_disable(choice,1)
        
    def actionFunction3(self,choice):
        self.able_disable(choice,2)
    
    def actionFunction5(self,choice) :
        self.imageList = self.spload.getImageObjReplaceColor(str(self.CharacterPreset),4,int(choice))
        self.displayImageList()
    
    def clearDisplay(self) :
        self.imageList = []
        self.displayImageList()
        
    def displayImageList(self) :
        if self.imageList[0]!=None:
            counter = 0
            posX = 0
            posY = 0

            resampleList = [Image.ANTIALIAS,Image.NEAREST,Image.BILINEAR,Image.BICUBIC,Image.LANCZOS]
            self.imageList2 = []
            cellWidth = self.canvasWidth/5
            cellHeight = self.canvasHeight/4
            
            for img in self.imageList :
                w, h = img.size
                addhead = int(self.spinboxList[5].get())
                addbod = int(self.spinboxList[6].get())
                if len(self.imageList) == 4:
                    w = self.bodyAloneSize+addbod*self.bodySizeIncrement
                    h = self.bodyAloneSize+addbod*self.bodySizeIncrement
                else :
                    if posY == 0 :
                        w = self.headSize+addhead*self.headSizeIncrement
                        h = self.headSize+addhead*self.headSizeIncrement
                    else :
                        w = self.bodySize+addbod*self.bodySizeIncrement
                        h = self.bodySize+addbod*self.bodySizeIncrement
                if len(self.imageList) != 4:
                    if counter<4 :
                        if self.imgListWearableHead != [] :
                            img = Image.alpha_composite(img,self.imgListWearableHead[counter])
                    else :
                        if self.imgListWearableBody != [] :
                            img = Image.alpha_composite(img,self.imgListWearableBody[counter-4])
                # if self.imgListWearable != [] and counter>3 and counter<8:
                #     #c2 = counter-4
                #     imgWearable = self.imgListWearable[counter-4]
                #     img = Image.alpha_composite(img,imgWearable)#img.paste(imgWearable)
                resized_image= img.resize((w,h), resampleList[1])
                tkimg = ImageTk.PhotoImage(resized_image)
                self.imageList2.append(tkimg)
                x = (posX+1)*cellWidth
                y = (posY+1)*cellHeight
                self.canvas.create_image(x,y, image=tkimg)
                if counter==3 :
                    posX = 0
                    posY = posY +1
                else :
                    posX = posX +1
                counter = counter +1
                print(counter)
        self.menu.pack(expand=False,anchor="n")
        self.canvas.pack(expand=False,anchor="n")
        self.root.update()
        

    def disableDrop(self,widgetListd,widgetLista=[]):
        dStatus = "disabled"
        aStatus = "active"
        dColor = self.defaultSelectorColorDisable
        aColor = self.defaultSelectorColor
        for i in range(len(self.dropdownListObj)) :
            if i in widgetListd :
                self.dropdownListObj[i].config(state=dStatus,bg=dColor)
            if i in widgetLista :
                self.dropdownListObj[i].config(state=aStatus,bg=aColor)
                
    def disableScale(self,widgetListd,widgetLista=[]):
        dStatus = "disabled"
        aStatus = "normal"
        dColor = self.defaultSelectorColorDisable
        aColor = self.defaultSelectorColor
        for i in range(len(self.spinboxList)) :
            if i in widgetListd :
                self.spinboxList[i].config(state=dStatus,bg=dColor,disabledbackground=dColor)
            elif i in widgetLista :
                self.spinboxList[i].config(state=aStatus,bg=aColor,disabledbackground=aColor)
                
    def disableRadio(self,widgetListd,widgetLista=[]):
        dStatus = "disabled"
        aStatus = "active"
        dColor = self.defaultSelectorColorDisable
        aColor = self.defaultSelectorColor
        for i in range(len(self.radioList)) :
            if i in widgetListd :
                self.radioList[i].config(state=dStatus,bg=dColor)
            elif i in widgetLista :
                self.radioList[i].config(state=aStatus,bg=aColor)
                
        
    def reset_option_menu(self,dropdownIndex=1,newList=[],index=None):
        menu = self.dropdownListObj[dropdownIndex]["menu"]
        menu.delete(0, "end")
        for string in newList:
            menu.add_command(label=string,command=lambda value=string:self.menuTrigger3(value))
        if index is not None:
            self.dropdownList[dropdownIndex].set(newList[index])

def headSelector(headDictList,headNum,returnSum=False) :
    if not returnSum :
        for headDict in headDictList :
            if headDict['SpriteVariants']<=headNum :
                headNum = headNum - headDict['SpriteVariants']
            else :
                return headDict['Name'],headNum
        return "Head",0
    else :
        counter = 0
        for headDict in headDictList :
            counter = counter + headDict['SpriteVariants']
        return counter
    
def bodySelector(bodyDictList,bodyNum,returnSum=False) :
    if not returnSum :
        for headDict in bodyDictList :
            if headDict['SpriteVariants']<=bodyNum :
                bodyNum = bodyNum - headDict['SpriteVariants']
            else :
                return headDict['Name'],bodyNum
        return "PrisonerX",0 
    else :
        counter = 0
        for headDict in bodyDictList :
            counter = counter + headDict['SpriteVariants']
        return counter
    
def openJson(path,filename,extention,disp=True) :
    with open(path+"/"+filename+"."+extention) as file:
        data = json.load(file)
    return data

def dictListToList(dictionaryList,fiedlName) :
    returnList = []
    for dictionary in dictionaryList :
        if fiedlName in dictionary.keys() :
            returnList.append(dictionary[fiedlName])
    return returnList

def dictListToIteList(dictionaryList,body=False) :
    returnNameList = []
    if not body :
        for dictionary in dictionaryList :
            for i in range(dictionary['SpriteVariants']) :
                returnNameList.append(dictionary['Name']+"_"+str(i+1))
    else :
        for dictionary in dictionaryList :
            if dictionary['SpriteVariants'] == 4 :
                returnNameList.append(dictionary['Name'])
            else :
                returnNameList.append(dictionary['Name']+"error")
    return returnNameList

def getSplitName(name) :
    return name[:-2],int(name[-1:])-1

skinColorList = {"None":None,
                 "White":"#ffffff",
                 "Pale1":"#ffe6e6",
                 "Pale2":"#f9d2d2",
                 "Light1":"#f6d0d0",
                 "Light2":"#f0a5a5",
                 "Mat1":"#ffccaa",
                 "Mat2":"#ffaa88",
                 "Mat3":"#ff8866",
				 "Mat4":"#dd6655",
                 "Brown1":"#bf3d1f",
                 "Brown2":"#af472f",
                 "Brown3":"#9f260f",
                 "Brown4":"#4f130f",
				 "Yellow1":"#f9f9bb",
				 "Yellow2":"#f7f7a1",
                 "Yellow3":"#ffff99",
				 "Yellow4":"#f0f0a8",
				 "Dark1":"#885500",
				 "Dark2":"#663a00",
				 "Dark3":"#885510",
				 "Dark4":"#663a10",
				 "Red":"#ff6666",
				 "Green":"#8cff66",
				 "Turquoise":"#66ffb3",
				 "Blue":"#668cff",
				 "Purple":"#d966ff"}
alphaList = [1,0.9,0.8,0.75,0.5]
win = chaSelector()