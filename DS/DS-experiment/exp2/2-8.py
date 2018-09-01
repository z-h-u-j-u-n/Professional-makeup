#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:09 2018

@author: zhujun
"""

'''求出平均数再迭代比较'''
string = input()
nlist = string.split()
for i in range(len(nlist)):
    nlist[i] = eval(nlist[i])
sum = 0
for i in range(len(nlist)):
    sum += nlist[i]
avg = sum / len(nlist)
for i in range(len(nlist)):
    if nlist[i] > avg:
        print(nlist[i], end=' ')