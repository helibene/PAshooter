# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:39:35 2023

@author: Alexandre
"""
from PIL import ImageTk,Image,ImageOps,ImageFilter,ImageEnhance

class imageProcessor :
    def __init__(self):
        self.resampleList = [Image.NEAREST,Image.ANTIALIAS,Image.BILINEAR,Image.BICUBIC,Image.LANCZOS]
        self.imageFilterList = [ImageFilter.BLUR,ImageFilter.CONTOUR,ImageFilter.DETAIL,ImageFilter.EDGE_ENHANCE,ImageFilter.EDGE_ENHANCE_MORE,ImageFilter.EMBOSS,ImageFilter.FIND_EDGES,ImageFilter.SHARPEN,ImageFilter.SMOOTH,ImageFilter.SMOOTH_MORE]
        imgpath="C:/Users/Alexandre/Desktop/test_lua/test_img/boardColor.png"
        img = Image.open(imgpath).convert("RGBA")#.convert("L")#
        newImg = self.resizePIL(img,2,2)
        newImgLast = self.colorizePIL(newImg,(0,0,255))
        newImgLast.save("C:/Users/Alexandre/Desktop/test_lua/test_img/boardColor19.png","PNG")
        pass
    
    def transformTerainTile(self,image,instList=[None,[None,None],[None,None],None,None,None]):
        image = self.trimPIL(image,instList[0])
        image = self.resizePIL(image,instList[1][0],instList[1][0],False,instList[1][1])
        image = self.colorizePIL(image,instList[2][0],overlayAlpha=instList[2][1])
        image = self.brightnessPIL(image,instList[3])
        image = self.contrastPIL(image,instList[4])
        image = self.sharpnessPIL(image,instList[5])
        return image
        
    def trimPIL(self,image,pixelNum) :
        if type(pixelNum)==type(None) :
            return image
        else :
            imageret = ImageOps.crop(image, border=pixelNum)
            return imageret
        
        
    def colorizePIL(self,image,white,black="black",mid=None,overlayAlpha=None):
        if type(white)==type(None) :
            return image
        else :
            imageOrig = image.copy()
            imageGray = image.convert("L")
            imageret = ImageOps.colorize(imageGray, black =black, white =white,mid=mid)
            if type(overlayAlpha)!=type(None) :
                imageOrig = imageOrig.convert("RGBA")
                imageret = imageret.convert("RGBA")
                imageret = Image.blend(imageOrig,imageret,overlayAlpha)
            return imageret
    
    def brightnessPIL(self,image,factor) :
        if type(factor)==type(None) :
            return image
        else :
            enhancer = ImageEnhance.Brightness(image)
            imageret = enhancer.enhance(factor)
            return imageret
    
    def colorEnhancePIL(self,image,factor) :
        if type(factor)==type(None) :
            return image
        else :
            enhancer = ImageEnhance.Color(image)
            imageret = enhancer.enhance(factor)
            return imageret
    
    def contrastPIL(self,image,factor) :
        if type(factor)==type(None) :
            return image
        else :
            enhancer = ImageEnhance.Contrast(image)
            imageret = enhancer.enhance(factor)
            return imageret
    
    def sharpnessPIL(self,image,factor) :
        if type(factor)==type(None) :
            return image
        else :
            enhancer = ImageEnhance.Sharpness(image)
            imageret = enhancer.enhance(factor)
            return imageret
    
    def resizePIL(self,image,width=1,height=1,pctMode=True,resampleSelection=0) :
        if type(width)==type(None) or type(height)==type(None) :
            return image
        else :
            newWidth = 0
            newHeight = 0
            imageret = image.copy()
            widthImg, heightImg = imageret.size
            if pctMode :
                newWidth = int(widthImg*width)
                newHeight = int(heightImg*height)
            else :
                newWidth = int(width)
                newHeight = int(height)
            imageret = imageret.resize((newWidth,newHeight), resample=self.resampleList[resampleSelection])
            return imageret
    
    def filterListPIL(self,image,filterIndexList=[]) :
        for filterIndex in filterIndexList :
            image = image.filter(filter=self.imageFilterList[filterIndex])
        return image
    
    def createSolidImage(self,image,color) :
        widthImg, heightImg = image.size
        return Image.new('RGBA',(widthImg,heightImg),color)
    
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

ip = imageProcessor()