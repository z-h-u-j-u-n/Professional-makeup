#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:53:12 2018

@author: zhujun
"""

class lruQueue():
    '''最近最久未访问队列'''
    
    def __init__(self, maxsize):
        # 0号索引代表oldest, qsize-1号索引代表newest
        self._maxsize = maxsize
        self._queue = []
        self._qsize = 0
        self._lackBlocks = 0
        
    def __len__(self):
        return self._qsize
    
    def __repr__(self):
        return str(self._queue)
        
    def insertE(self, data):
        if data in self._queue: # 待插入的元素在队列中
            index = self._queue.index(data) # 更新该元素的位置
            temp = self._queue.pop(index)
            self._queue.append(temp)
        else: # 待插入的元素不在队列中
            self._lackBlocks += 1
            if len(self) < self._maxsize: # 队列未满则直接插入
                self._queue.append(data)
                self._qsize += 1
            else: # 队列已满则淘汰最久未访问的元素
                self._queue.pop(0) # 弹出首元素
                self._queue.append(data)
                
    def lackBlocks(self):
        return self._lackBlocks
    
class fifoQueue():
    '''先进先出队列'''
    
    def __init__(self, maxsize):
        self._maxsize = maxsize
        self._queue = []
        self._qsize = 0
        self._lackBlocks = 0
        
    def __len__(self):
        return self._qsize
    
    def __repr__(self):
        return str(self._queue)
        
    def insertE(self, data):
        if data in self._queue: # 待插入的元素在队列中，什么也不用做
            return
        else: # 待插入的元素不在队列中
            self._lackBlocks += 1
            if len(self) < self._maxsize: # 队列未满则直接插入
                self._queue.append(data)
                self._qsize += 1
            else: # 队列已满则淘汰停留时间最长的的元素
                self._queue.pop(0) # 弹出首元素
                self._queue.append(data)
                
    def lackBlocks(self):
        return self._lackBlocks
                
if __name__ == '__main__':
    m = eval(input('请输入物理块个数m: '))
    n = eval(input('请输入进程页数n: '))
    p = eval(input('请输入页面访问顺序: '))
    print('\n最近最久未访问算法：')
    lruq = lruQueue(m)
    for i in p:
        lruq.insertE(i)
        print('insert %d ->' % i, lruq)
    print('缺页率：', lruq.lackBlocks()/len(p))
    print('\n先进先出算法：')
    fifoq = fifoQueue(m)
    for i in p:
        fifoq.insertE(i)
        print('insert %d ->' % i, fifoq)
    print('缺页率：', fifoq.lackBlocks()/len(p))
    
                
            
        
    