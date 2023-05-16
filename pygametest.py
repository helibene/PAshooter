import pygame
from pygame.locals import *
import spriteLoader as sl
import time
import sys
import random
# Take colors input

spload = sl.spriteLoader()
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
  
# Construct the GUI game
pygame.init()
  
# Set dimensions of game GUI
w, h = 1366, 768
mapsize = 100
screen = pygame.display.set_mode((w, h))
running=True
#imgrectList = spload.imgrectList
pgimgList = spload.pgimgList
matNumMatrix = [[None for x in range(mapsize)] for y in range(mapsize)] 
for x in range(mapsize) :
    for y in range(mapsize) :
        matNumMatrix[y][x] = int(random.random()*len(pgimgList))
# Setting what happens when game is in running state
count = 0
fpsNum = 0
posX = 0
posY = 0
speed = 30
#imp = pygame.image.load("C:\\Users\\Alexandre\\Desktop\\PAshooter\\sprites\\map\\texture\\map3_tex.jpeg").convert()
while running:
    start = time.time()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    # Set the background 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                posY = posY - speed
            if event.key == pygame.K_DOWN:
                posY = posY + speed
            if event.key == pygame.K_RIGHT:
                posX = posX + speed
            if event.key == pygame.K_LEFT:
                posX = posX - speed
                print("lol")
    screen.fill(YELLOW)
    for x in range(mapsize) :
        for y in range(mapsize) :
            screen.blit(pgimgList[matNumMatrix[y][x]], (x*spload.matSize+posX,y*spload.matSize+posY))#imgrectList[i][1])
    #   
    
    # for i in range(len(imgrectList)) :
    #screen.blit(imgrectList[i][0], ((i%35)*35+count,int(i/35)*35+count))#imgrectList[i][1])
    # screen.blit(imp, (count, count))
    # for i in range(len(imgrectList)) :
    #     screen.blit(imgrectList[i][0], ((i%35)*35+count,int(i/35)*35+count))#imgrectList[i][1])
    # #     #pygame.draw.rect(screen, BLUE, imgrectList[i][1], 2)
    # for i in range(1000) :
    #     screen.blit(imgrectList[0][0], ((i%35)*35+count,int(i/35)*35+count))#imgrectList[i][1])
    #     #pygame.draw.rect(screen, BLUE, imgrectList[i][1], 2)
      
    # Update the GUI pygame
    pygame.display.update()
    count = count + 1
    
    end = time.time()
    if end!=start :
        fpsNum = float(1/float((float(end)-float(start))))
    print(fpsNum)
# Quit the GUI game
pygame.quit()
sys.exit()
