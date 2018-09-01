#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:22:56 2018

@author: zhujun
"""

from threading import Thread, Lock, Semaphore
import time, random

class Producer(Thread):
    '''生产者模型'''
    
    def __init__(self, name, full, empty, lock, slist):
        Thread.__init__(self, name=name)
        self._full = full
        self._empty = empty
        self._lock = lock
        self._slist = slist
        
    def run(self):
        global buffer
        while True:
            self._empty.acquire()
            self._lock.acquire()
            i = random.randint(10,100)
            buffer.append(i)
            print('Producer is producing %d' % i)
            self._lock.release()
            self._full.release()
            time.sleep(random.randint(1, 3))
            # time.sleep(1)

           
            
class Consumer(Thread):
    '''消费者模型'''
    
    def __init__(self, name, full, empty, lock, slist):
        Thread.__init__(self, name=name)
        self._full = full
        self._empty = empty
        self._lock = lock
        self._slist = slist
        
    def run(self):
        global buffer
        while True:
            self._full.acquire()
            self._lock.acquire()
            i = buffer.pop()
            print('%s is consuming %d' % (self.getName(),i))
            self._lock.release()
            self._empty.release()
            time.sleep(random.randint(4, 6))
            # time.sleep(1)

if __name__ == '__main__':
    buffer = []
    full = Semaphore(0)
    empty = Semaphore(10)
    lock = Lock()
    
    p = Producer('Producer', full, empty, lock, buffer)
    cs = [ Consumer('Consumer'+str(i), full, empty, lock, buffer)
                        for i in range(3)]
    p.start()
    for c in cs:
        c.start()
#    p.join()
#    for c in cs:
#        c.join()