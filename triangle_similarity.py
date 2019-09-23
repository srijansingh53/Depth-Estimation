# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:32:44 2019

@author: SRIJAN
"""

import imutils
import numpy as np
import cv2

def find_marker(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edge = cv2.Canny(gray, 35, 125)
    cv2.imwrite('edge.jpg', edge)

img = cv2.imread('1.jpg')
find_marker(img)
    