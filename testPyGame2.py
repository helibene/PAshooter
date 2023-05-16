# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 00:31:53 2023

@author: Alexandre
"""
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
class testPyGame2 :
    def __init__(self):
        spload = sl.spriteLoader()
        print("load images pygame")
        self.GRAY = (200, 200, 200)
        self.RED = (255, 0, 0)
        w, h = 1366, 768#1920, 1080#
        flag = pygame.RESIZABLE|pygame.SHOWN
        pygame.init()
        pygame.display.init()
        self.screenSurface = pygame.display.set_mode(size=(w-35, h-35),flags=flag)
        pygame.display.set_caption("Hello Wolrld")
        self.running=True
        imgList,infodf = spload.processLoadRequest([[["Object"],["Entity"]]],1,-1)#["Object"],["Foliage"]##"Entity"
        del(spload)
        print(len(imgList))
        print(infodf)
        print(sum(list(infodf["VarNum"])))
        sizX = 32
        sizY = 32
        self.rectMat = []
        self.imgList = []
        for img in imgList :
            newImg= img.convert_alpha()
            if newImg!=None :
                self.imgList.append(newImg)
        for x in range(int((w-50)/sizX)) :
            for y in range(int((h-50)/sizY)) :
                self.rectMat.append(Rect(x*sizX, y*sizY, sizX, sizY))
        print("game loop")
        self.gameLoop()
        
    def gameLoop(self) :
        count = 0
        fpsNum = 0
        posX = 0
        posY = 0
        speed = 10
        clock = pygame.time.Clock()
        while self.running:
            start = time.time()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
            
            # for ret in self.rectList :
            #     ret.move_ip(int(speed*(random.random()-0.5)),int(speed*(random.random()-0.5)))
            #     # if count%20 :
            #     #     ret.inflate_ip((10,10))
            self.screenSurface.fill(self.GRAY)
            
            for x in range(len(self.rectMat)) :
                #pygame.draw.rect(self.screenSurface, self.RED, self.rectList[x])
                if x < len(self.imgList) :
                    self.screenSurface.blit(self.imgList[x%len(self.imgList)],(self.rectMat[x][0]+count*0,self.rectMat[x][1]+count*0))#%200,#imgrectList[i][1])
                
            #clock.tick(100)
            pygame.display.flip()
            end = time.time()
            if end!=start :
                fpsNum = float(1/float((float(end)-float(start))))
                #print(fpsNum)
            count = count + 1
        pygame.quit()
        sys.exit()
        
def pilImageToPygameImage(image,sizeMulti=0.5) :
    if image!=None :
        mode = image.mode
        size = image.size
        size2 = (int(size[0]*sizeMulti),int(size[1]*sizeMulti))
        data = image.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)
        py_image = pygame.transform.scale(py_image, (size2[0], size2[1]))
        py_image = py_image.convert_alpha()
        return py_image
    else :
        return None


tp = testPyGame2()