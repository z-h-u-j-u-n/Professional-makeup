#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:33:59 2018

@author: zhujun
"""

'''逆运算 k = (k + 1) * 2 执行9次'''
k = 1
for i in range(9):
    k = (k + 1) * 2
print("猴子第一天摘了" + str(k) + "个桃子")