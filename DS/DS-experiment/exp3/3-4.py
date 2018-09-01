#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 15:10:24 2018

@author: zhujun
"""

'''利用数组存储，全部初始化为1，已经访问过的就置为0'''
# 寻找下一个未出列的人
def findNext(nlist, index):
    i = (index + 1) % len(nlist)
    while True:
        if nlist[i] == 1:
            break
        else:
            i = (i + 1) % len(nlist)
    return i
        
size = eval(input("n: "))
# 假设 m < n
m = eval(input("m: "))
nlist = [ 1 for i in range(size)]
norder = [ -1 for i in range(size)]
begin = 0
k = 0
# 寻找第m个人
while size > 0:
    for i in range(m-1): # 第一次寻找只需要调用m-1次函数
        begin = findNext(nlist, begin)
    if size < len(nlist): # 如果是第二次寻找以及以后的情况，则需要调用m次函数
        begin = findNext(nlist, begin)
    norder[k] = begin
    k += 1
    nlist[begin] = 0
    size -= 1
print(norder)
    