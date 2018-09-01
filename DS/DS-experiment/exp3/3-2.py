#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:08:42 2018

@author: zhujun
"""

'''递归求解，注意排除重复情况'''
import math
def getA(num, st): # num和st分别是分解的两个因子且num>st
    if num == 1: # 递归出口
        return 1
    else:
        cnt = 0
        # 下面的循环就可以消除重复项
        for i in range(st, num+1):
            if num % i == 0:
                cnt += getA(num//i, i)
        return cnt 
        
n = eval(input())   
print(getA(n, 2))