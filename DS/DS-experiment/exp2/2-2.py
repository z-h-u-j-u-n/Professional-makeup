#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:38:16 2018

@author: zhujun
"""

'''根据行和列以及flag的值调整权重w， 最终产生z字形'''
n = eval(input())
i, j = 1, 1
w = [[0, 1],
     [1, -1],
     [1, 0],
     [-1, 1]]
flag = True
k = 1
index = 0
while k<n:
    if i == 1 and flag: # 垂直向下移动
        index = 0
        flag = False
    elif i == 1 and not flag: # 朝左下移动
        index = 1
        flag = True
    elif j == 1 and flag: # 水平向右移动
        index = 2
        flag = False
    elif j == 1 and not flag: # 朝右上移动
        index = 3
        flag = True    
    i += w[index][0]
    j += w[index][1]
    k += 1
        
print("第N项为" + str(i) + "/" + str(j))