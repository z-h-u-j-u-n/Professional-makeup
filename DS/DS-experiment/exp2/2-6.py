#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:29:11 2018

@author: zhujun
"""

'''利用python的find函数'''
string = input()
tofind = "debug"
if string.find(tofind)!=-1:
    print("包含debug")
else:
    print("不包含debug")
