#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:47:57 2018

@author: zhujun
"""

'''先进行插入排序，再进行奇偶排序'''
string = input()
nlist = string.split()
# 插入排序
for i in range(len(nlist)):
    nlist[i] = eval(nlist[i])
for i in range(1, len(nlist)):
    temp = nlist[i]
    insertindex = i
    for j in range(i):
        if nlist[j] > temp:
            insertindex = j
            break
    if insertindex != i:
        for j in range(i, insertindex, -1):
            nlist[j] = nlist[j-1]
    nlist[insertindex] = temp
print("第一次排序后的队列：", end="")
print(nlist)
# 实现奇偶分流
# 借助队列存储偶数项，先将奇数项排好，再直接顺序排列偶数项
from queue import Queue
queue = Queue(maxsize=len(nlist))
k = 0
for i in range(len(nlist)):
    if nlist[i] % 2 != 0:
        nlist[k] = nlist[i]
        k += 1
    else:
        queue.put(nlist[i])
while not queue.empty():
    nlist[k] = queue.get()
    k += 1
print("第二次排序后的队列：", end="")
print(nlist)