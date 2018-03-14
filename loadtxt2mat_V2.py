# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:02:09 2018

@author: hanl
"""
import types

from numpy import *

def loadDataSet(fileName,col_num=None):      
    # count  txt colnum number
    if col_num is None:
        col_num = len(open(fileName).readline().split('\t')) 
    
    dataMat = [];   
    
    fr = open(fileName) 
                  
    for linestr in fr.readlines():   

        linefloatList =[]
         
        linestrList = linestr.strip().split('\t')  

        for i in range(col_num):
            linefloatList.append(float(linestrList[i]))
                      
        dataMat.append(linefloatList)
    return mat(dataMat)



    
datamat=loadDataSet('ex0.txt',3)
print(datamat)
print(type(datamat))
print(shape(datamat))
