# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 00:45:37 2023

@author: Alexandre
"""
import os, shutil

class cleaner :
    def __init__(self,texture=True,collision=True,rawSplit=True,objectImage=True):
        mapPath = "C:/Users/Alexandre/Desktop/PAshooter/sprites/map/"
        if texture :
            emptyFolder(mapPath+"texture/")
        if collision :
            emptyFolder(mapPath+"collision/")
        if rawSplit :
            emptyFolder(mapPath+"raw/"+"split/")
        if objectImage :
            emptyFolder(mapPath+"object/")
        
    

def emptyFolder(folder) :
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            
            
            
cl = cleaner()