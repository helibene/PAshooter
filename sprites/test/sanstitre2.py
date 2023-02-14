# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:31:24 2023

@author: Alexandre
"""
from win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))