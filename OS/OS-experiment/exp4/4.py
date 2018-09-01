#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:16:46 2018

@author: zhujun
"""

from threading import Thread, Lock, Semaphore
import time, random

class subProcess(Thread):
    '''子进程1'''
    
    def __init__(self, name, empty, full, lock, pipe):
        Thread.__init__(self, name=name)
        self._empty = empty
        self._full = full
        self._lock = lock
        self._pipe = pipe
        
    def run(self):
        while True:
            self._empty.acquire()
            self._lock.acquire()
            i = random.randint(10,100)
            self._pipe.append('%s writes %d at %s' % (self.getName(),i, time.clock()))
            # print('Producer is producing %d' % i)
            self._lock.release()
            self._full.release()
            time.sleep(1)
  
if __name__ == '__main__':
    pipe = []
    empty = Semaphore(1)
    full = Semaphore(0)
    lock = Lock()
    
    p1 = subProcess('subProcess1', empty, full, lock, pipe)
    p2 = subProcess('subProcess2', empty, full, lock, pipe)
    
    
    p1.start()
    p2.start()
    
    while True:
        full.acquire()
        lock.acquire()
        print('parProcess reads:' + str(pipe))
        pipe.pop()
        lock.release()
        empty.release()

    
    p1.join()
    p2.join()
#    for c in cs:
#        c.join()