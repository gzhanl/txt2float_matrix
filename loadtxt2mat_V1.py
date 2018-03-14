# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:02:09 2018

@author: hanl
"""
import types

from numpy import *

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    # count  txt colnum number
    col_num = len(open(fileName).readline().split('\t')) 
    
     # dataMat and labelMat , <class 'list'>
    dataMat = [];   
    # fr = file read
    fr = open(fileName) 
    # linestr =   string in each line ,  <class 'str'>               
    for linestr in fr.readlines():   

        linefloatList =[]
         # curLine = each line in txt is 1 list , <class 'list'> ,element num is colounm num ,like ['1.000000', '0.067732', '3.176513']
        linestrList = linestr.strip().split('\t')  

        for i in range(col_num):
            linefloatList.append(float(linestrList[i]))
                      
        dataMat.append(linefloatList)
    return mat(dataMat)



    
datamat=loadDataSet('ex0.txt')
print(datamat)
print(type(datamat))
print(shape(datamat))
