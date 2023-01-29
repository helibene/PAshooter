# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:18:53 2023

@author: Alexandre
"""
import tkinter as tk
from tkinter import *

class windowUtil :
    def __init__(self):
        pass
    

def setRoot(w,width,height,offx=0,offy=0,top=True,fullscreen=False,resizable=True,zoom=True):
    root = tk.Tk()
    if type(width)!=type(None) :
        width_return = width
    else :
        width_return = root.winfo_screenwidth()
    if type(height)!=type(None) :
        height_return = height
    else :
        height_return = root.winfo_screenheight()
    root.geometry(str(width_return)+"x"+str(height_return)+"+"+str(offx)+"+"+str(offy))
    if top :
        root.attributes('-topmost',1)   
    root.resizable(resizable, resizable)
    if zoom :
        root.state('zoomed')
    root.attributes("-fullscreen",fullscreen)
    root.attributes('-alpha', 1)
    return root,width_return,height_return
    
def getCanvasFullScreen(w,root,width,height,color,borderwidth=-2):
    canvas = Canvas(root, width = width, height = height, bg=color,borderwidth=borderwidth)
    canvas = drawBackground(w,canvas,width,height,color)
    return canvas
    
def drawBackground(w,canvas,width,height,color):
    canvas.create_rectangle(-10, -10, width+10, height+10, fill=color)
    return canvas
    