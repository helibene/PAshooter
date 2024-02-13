# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:54:07 2023

@author: Alexandre
"""
import pygame
from pygame.locals import *
import spriteLoader as sl
import time
import sys
import random
# Take colors input
class testPyGame :
    def __init__(self):
        spload = sl.spriteLoader()
        self.GRAY = (200, 200, 200)
        w, h = 1366, 768
        flag = pygame.RESIZABLE|pygame.SHOWN
        pygame.init()
        pygame.display.init()
        self.screenSurface = pygame.display.set_mode(size=(w-100, h-100),flags=flag)
        #pygame.Surface.convert_alpha(self.screenSurface)
        # wm_dict = pygame.display.get_wm_info()
        # vidInfo = pygame.display.Info()
        # print(wm_dict)
        # print(vidInfo)
        pygame.display.set_caption("Hello Wolrld")
        self.running=True
        imgList = spload.imgList
        itemData = []
        cnt = 0
        posX = 0
        posY = 0
        sizX = 0
        sizY = 0
        imgList = imgList#[0:500]
        print(len(imgList))
        for img in imgList :
            newImg,size = pilImageToPygameImage(img)
            if True : #size[1]<50 :#if size[0]*size[1]<5000 :
                itemData.append([newImg,posX,posY])
                posX = posX + size[0] +2
                if size[1] > sizY :
                    sizY = size[1]
                if posX>w-30 :
                    posX = 0
                    posY = posY + sizY +2
                    sizY = 0
                cnt = cnt +1
        #print(cnt)
        #print(itemData)
        self.itemData = itemData
        
        self.gameLoop()
        
    def gameLoop(self) :
        count = 0
        fpsNum = 0
        posX = 0
        posY = 0
        speed = 30
        clock = pygame.time.Clock()
        while self.running:
            start = time.time()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_UP:
                        posY = posY - speed
                    if event.key == pygame.K_DOWN:
                        posY = posY + speed
                    if event.key == pygame.K_RIGHT:
                        posX = posX + speed
                    if event.key == pygame.K_LEFT:
                        posX = posX - speed
        
            self.screenSurface.fill(self.GRAY)
            for x in range(len(self.itemData)) :
                self.screenSurface.blit(self.itemData[x][0], (self.itemData[x][1]+posX,self.itemData[x][2]+posY))#imgrectList[i][1])
            
            clock.tick(60)
            pygame.display.flip()
            count = count + 1
            end = time.time()
            if end!=start :
                fpsNum = float(1/float((float(end)-float(start))))
                #print(fpsNum)
        pygame.quit()
        sys.exit()
        
def pilImageToPygameImage(image) :
    if image!=None :
        mode = image.mode
        size = image.size
        data = image.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)
        return py_image,size
    else :
        return None,None


tp = testPyGame()