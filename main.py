# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:59:13 2023

@author: Alexandre
"""
import configLoader as cf
import window as wi
import os
from win32api import GetSystemMetrics

class main :
    def __init__(self):
        rootPath = invertSlash(getFolderLocation())
        width,height = getScreenSize()
        sl = wi.window(cf.configLoader(rootPath,width,height))

def getScreenSize() :
    return GetSystemMetrics(0),GetSystemMetrics(1)

def getFolderLocation() :
    return str(os.getcwd())

def invertSlash(string) : 
    return string.replace("\\","/")

ma = main() 