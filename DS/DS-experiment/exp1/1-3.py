# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:55:35 2018

@author: 1
"""

'''首先判断是否闰年'''
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
rflag = False # rflag=True表示闰年
flag = False # flag=True表示日期正确
string = input()
slist = string.split()
year = eval(slist[0])
month = eval(slist[1])
day = eval(slist[2])
if year%4==0 and year%100!=0:
    rflag = True
elif year%400==0:
    rflag = True
else:
    rflag = False
# 先排出明显出错的情况
if year<=0 or month<=0 or month>12 or day<=0 or day>366:
    flag = False
else:
    # 然后看年份是闰年的时候是否出错
    if rflag:
        days[1] = 29
    if day>days[month-1]:
        flag = False
    else:
        flag = True
# 输出结果
if flag:
    print("正确")
else:
    print("不正确")
    