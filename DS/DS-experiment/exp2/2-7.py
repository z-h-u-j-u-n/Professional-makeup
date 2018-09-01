#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:34:03 2018

@author: zhujun
"""

'''先排序再进行插入排序'''
string = input()
nlist = string.split()
for i in range(len(nlist)):
    nlist[i] = eval(nlist[i])
# 考试的时候写详细 不要调用库函数
nlist.sort(reverse=False)
number = eval(input())
index = 0
# 假设输入的数都是正整数
# 插入排序
for i in range(len(nlist)):
    if number < nlist[i]:
        index = i
        break
for i in range(len(nlist), index, -1):
    if i == len(nlist):
        nlist.append(0)
    nlist[i] = nlist[i-1]
nlist[index] = number
print(nlist)