# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:34:42 2018

@author: 1
"""

'''先求出每分钟，每小时，每天等于多少秒，再从天开始对输入的秒数整除取余'''
time = eval(input())
# 计量单位
oneday = 24 * 60 * 60
onehour = oneday // 24
oneminute = onehour // 60

# 整除取余
resultday = time // oneday
time %= oneday
resulthour = time // onehour
time %= onehour
resultminute = time // oneminute
time %= oneminute
print(str(resultday) + ":" + str(resulthour) + ":" + str(resultminute) + ":" + str(time))