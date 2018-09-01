#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:52:30 2018

@author: zhujun
"""

'''先将范围内的所有素数写出啦，再判断是否是素数对'''
import math
# 判断是不是素数
def isPrime(number):
    bound = math.floor(math.sqrt(number)) + 1
    flag = True
    for i in range(2, bound):
        if number%i == 0:
            flag = False
            break
    return flag

# 求所有素数对
def getAllPrime(n):
    plist = []
    for i in range(2, n+1):
        if isPrime(i):
            plist.append(i)
    for i in range(len(plist)-1):
        if plist[i+1] - plist[i] == 2:
            print(str(plist[i]) + " " + str(plist[i+1]), end=", ")
            
if __name__ == "__main__":
    n = eval(input())
    getAllPrime(n)
            