#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:02:24 2018

@author: zhujun
"""

'''先求出某数所有因子，如果因子之和等于本身，则满足完数的条件'''
import math
def get(number):
    ylist = [1]
    for i in range(math.floor(math.sqrt(number))):
        j = i+1
        if j==1:
            continue
        else:
            if number%j==0:
                ylist.append(j)
                ylist.append(number/j)
    return ylist

if __name__=="__main__":
    j = 0
    for i in range(1001):
        if i>0:
            numberlist = get(i)
            if sum(numberlist) == i:
                print(i, end=" ")
                j += 1
            if j == 5:
                j = 0
                print("\n")
            
                