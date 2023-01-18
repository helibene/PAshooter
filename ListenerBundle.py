# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:39:28 2023

@author: Alexandre
"""
from pynput import keyboard,mouse

class ListenerBundle :
    def __init__(self):
        self.print = False
        self.pressedKeys = []
        self.mouseVal = [-1,-1,0]
        self.mousePos = [-1,-1]
        self.keyMappingList = ["z","s","q","d","e","m","tab"]
        self.stopKey = keyboard.Key.esc
        self.exitFlag = False
        self.keyListener,self.mouseListener = self.startListenerBundle()
        
    def startListenerBundle(self) :
        keyListener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        keyListener.start()
        mouseListener = mouse.Listener(on_move=self.on_move,on_click=self.on_click,on_scroll=self.on_scroll)
        mouseListener.start()
        return keyListener,mouseListener
    
    def killListener(self) :
        self.keyListener.stop()
        self.mouseListener.stop()
        del(self)
        
    def printBundle(self) :
        print("Keys pressed :",self.pressedKeys)
        print("Mouse clicked : (",self.mouseVal[0],self.mouseVal[1],")")
        print("Mouse position : (",self.mousePos[0],self.mousePos[1],")")
        print("Scroll direction :",self.mouseVal[2])
        
    def on_press(self,key):
      try:
          if str(key.char) not in self.pressedKeys :
              self.pressedKeys.append(str(key.char))
      except AttributeError:
          pass
      if key == keyboard.Key.tab :
          if "tab" not in self.pressedKeys :
              self.pressedKeys.append("tab")
    
    def on_release(self,key):
        try:
            if str(key.char) in self.pressedKeys :
                self.pressedKeys.remove(str(key.char))
        except AttributeError:
            pass
        if key == self.stopKey:
            self.exitFlag = True
            return False
        if key == keyboard.Key.tab :
            if "tab" in self.pressedKeys :
                self.pressedKeys.remove("tab")
    
    def on_scroll(self,x, y, dx, dy):
        if dy<0 :
            self.mouseVal[2] = -1
        else : 
            self.mouseVal[2] = 1

        
    def on_move(self,x, y):
        self.mousePos[0] = x
        self.mousePos[1] = y


    def on_click(self,x, y, button, pressed):
        if pressed :
            self.mouseVal[0] = x
            self.mouseVal[1] = y
    
    def resetClick(self) :
        self.mouseVal[0] = -1
        self.mouseVal[1] = -1
        
    def keyAction(self) :
        keyDir = [0,0]
        interact = False
        drop = False
        sprint = False
        if "z" in self.pressedKeys :
            keyDir = [keyDir[0],keyDir[1]-1]
        if 's' in self.pressedKeys :
            keyDir = [keyDir[0],keyDir[1]+1]
        if 'q' in self.pressedKeys :
            keyDir = [keyDir[0]-1,keyDir[1]]
        if 'd' in self.pressedKeys :
            keyDir = [keyDir[0]+1,keyDir[1]]
        if 'e' in self.pressedKeys :
            interact = True
        if 'm' in self.pressedKeys :
            drop = True
        if "tab" in self.pressedKeys :
            sprint = True
        return keyDir,interact,drop,sprint
    
    def keyActionMapped(self) :
        keyDir = [0,0]
        interact = False
        drop = False
        sprint = False
        if self.keyMappingList[0] in self.pressedKeys :
            keyDir = [keyDir[0],keyDir[1]-1]
        if self.keyMappingList[1] in self.pressedKeys :
            keyDir = [keyDir[0],keyDir[1]+1]
        if self.keyMappingList[2] in self.pressedKeys :
            keyDir = [keyDir[0]-1,keyDir[1]]
        if self.keyMappingList[3] in self.pressedKeys :
            keyDir = [keyDir[0]+1,keyDir[1]]
        if self.keyMappingList[4] in self.pressedKeys :
            interact = True
        if self.keyMappingList[5] in self.pressedKeys :
            drop = True
        if self.keyMappingList[6] in self.pressedKeys :
            sprint = True
        return keyDir,interact,drop,sprint

    