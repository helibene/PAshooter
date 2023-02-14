# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:24:51 2023

@author: Alexandre
"""
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#Print the screen size
print("Screen width:", screen_width)
print("Screen height:", screen_height)

win.destroy()
win.mainloop()