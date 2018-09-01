#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 07:48:50 2018

@author: zhujun
"""

'''本题属于哈夫曼编码。首先先要建立一颗哈夫曼树，其所有叶子节点为字符。然后通过遍历哈夫曼树确定
   叶子结点以及对应的哈夫曼编码，最后通过查找编码表即可实现字符串的压缩。'''
# 本题使用的数据结构有：
# PriorityQueue: 优先级队列，通过该结构快速选择最小的两个节点组成一个新的节点并加入队列，
#                直到队列中仅剩下一个元素为止，该元素即为哈夫曼树的根节点
# Node: 哈夫曼树的节点， 注意要实现__it__函数以实现优先队列的比较

from queue import PriorityQueue
def getItems():
    # 返回最初的编码频数表
    dicts = {
                'A': 64, 'B': 13, 'C': 22, 'D': 32, 'E': 103, 'F': 21, 'G': 15,
                'H': 47, 'I': 57, 'J': 1,  'K': 5,  'L': 32,  'M': 20, 'N': 57,
                'O': 63, 'P': 15, 'Q': 1,  'R': 48, 'S': 51,  'T': 80,
                'U': 23, 'V': 8,  'W': 18, 'X': 1,  'Y': 16,  'Z': 1,
                ' ': 168
            }
    return dicts

class Node():
    '''哈夫曼树的节点'''
    def __init__(self, data, freq, left = None, right = None, father = None):
        self._data = data
        self._freq = freq
        self._left = left
        self._right = right
        self._father = father
    
    def isleft(self):
        return self._left._father == self
    
    def __lt__(self, other):
        return self._freq < other._freq
    
def getCode(head, s, dicts):
    # 遍历的过程中存储编码表， 注意不要用if-else
    if head._left == None and head._right == None:
        dicts[head._data] = s
        return
    getCode(head._left, s+'0', dicts)
    getCode(head._right, s+'1', dicts)
     
def traversal(head):
    # 遍历哈夫曼树
    if head is None:
        return
    print(head._data, end=' ')
    traversal(head._left)
    traversal(head._right)

if __name__ == '__main__':
    q = PriorityQueue(30)
    dicts = getItems()
    for k, v in dicts.items():
        q.put((v, Node(k, v)))
    # 建立哈夫曼树
    while q.qsize() >= 2:
        node1 = q.get()[1]
        node2 = q.get()[1]
        fnode = Node('Nan', node1._freq + node2._freq, node1, node2)
        node1._father = fnode
        node2._father = fnode
        q.put((fnode._freq, fnode))
    hf = q.get()[1]
    
    print('哈夫曼树为：')
    traversal(hf)
    print('\n')
    # 实现哈夫曼编码
    s = 'C PROGRAM IS MY FAVORITE'
    rs = ''
    getCode(hf, '', dicts)
    for i in s:
        rs += dicts[i]
    print('哈夫曼编码表为：')
    print(dicts)
    print()
    print('哈夫曼编码为：')
    print(rs)
    
        