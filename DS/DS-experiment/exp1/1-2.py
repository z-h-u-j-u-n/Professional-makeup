# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:35:12 2018

@author: 1
"""

'''将26个字母用列表存储，可以观察到相互替换的字母索引之和相等'''
table = [
         'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z'
         ] 
length = len(table)
s = input()
index = table.index(s)
print(table[length-1-index])