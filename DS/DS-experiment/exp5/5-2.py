#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:38:14 2018

@author: zhujun
"""

nlist = eval(input())
def linkHash(nlist, p):
    '''链地址法解决哈希冲突'''
    hl = [ [] for i in range(p) ]
    for i in nlist:
        hl[i%p].append(i)
    return hl

def linearHash(nlist, p):
    '''线性探测解决哈希冲突'''
    ll = [ 0 for i in range(p) ]
    for i in nlist:
        k = 0
        if ll[i%p] == 0:
            ll[i%p] = i
        else:
            while ll[(i%p+k)%p] == 0:
                k += 1
            if k >= p:
                raise ValueError('哈希表已满')
            ll[(i%p+k)%p] = i%p 
    return ll

# 测试链哈希表
it1 = linkHash(nlist, 11)
k = 0
print('linkHash:')
for i in it1:
    print(k, end=':')
    for j in i:
        print(j, end=' ')
    print()
    k += 1

# 测试线性再散列哈希表
it2 = linearHash(nlist, 11)
print('linearHash:', end='')
print(it2)