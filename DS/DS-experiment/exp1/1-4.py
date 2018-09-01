# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 19:32:09 2018

@author: 1
"""
'''先将各个位数上的数字求出来，再+7取模数为10，最后进行交换'''
def encode(number):
    nlist = []
    base = 1000
    for i in range(4):
        nlist.append(number // base)
        number %= base
        base //= 10
        nlist[i] = (nlist[i] + 7) % 10
    nlist[0], nlist[2] = nlist[2], nlist[0]
    nlist[1], nlist[3] = nlist[3], nlist[1]
    print(nlist)    

'''先将位数进行交换，再根据数字的大小分别处理'''
def decode(nlist):
    nlist[1], nlist[3] = nlist[3], nlist[1]
    nlist[0], nlist[2] = nlist[2], nlist[0]
    for i in range(4):
        # 原先的数+7 < 10
        if nlist[i]>=7:
            nlist[i] -= 7
        else: # 原先的数+7 > 10
            nlist[i] = 10 + nlist[i] - 7
    # 组装成四位数
    number = 0
    for i in range(4):
        number = 10 * number + nlist[i]
    print(number)

number = eval(input())
string = input()
nlist = string.split(",")
for i in range(4):
    nlist[i] = eval(nlist[i])
encode(number)
decode(nlist)