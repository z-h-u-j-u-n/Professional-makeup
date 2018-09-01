#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:18:19 2018

@author: zhujun
"""

'''累加即可'''
# 假设日期输入都是合法的
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 0
string = input()
year = eval(string.split()[0])
month = eval(string.split()[1])
day = eval(string.split()[2])
if year%4==0 and year%100!=0:
    days[1] = 29
if year%400==0:
    days[1] = 29
for i in range(month):
    if i==month-1:
        break
    cnt += days[i]
cnt += day
print("这是一年中的第" + str(cnt) + "天")    

    