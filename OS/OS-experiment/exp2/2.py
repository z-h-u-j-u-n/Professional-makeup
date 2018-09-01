#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:31:59 2018

@author: zhujun
"""

class PCB():
    '''进程控制块'''
    
    def __init__(self, name, arrivetime, needtime, priority=0, cputime=0, waittime=0):
        self.name = name # 进程名
        self.priority = priority # 进程优先级
        self.arrivetime = arrivetime # 进程到达时间
        self.needtime = needtime # 进程需要运行的时间
        self.cputime = cputime # 进程已运行的时间
        self.waittime = waittime # 进程已等待的时间
        self.state = 'ready' # 进程状态：'ready'-就绪态 'run'-运行态 'block'-等待态
                             # 'exit'-终止态

    def __repr__(self): # 返回PCB的字符串表示
        return ' %s\t%d\t  %d\t    %d\t     %d\t    %d\t   %s\t' % (self.name, self.priority, 
                self.arrivetime, self.needtime, self.cputime, self.waittime, self.state)
    
    def needytime(self): # 进程还需要cpu的时间
        return self.needtime - self.cputime
    
    def run(self): # 运行进程
        self.state = 'run'
        self.cputime += 1
        if self.needytime() == 0:
            self.toexit()
    
    def wait(self): # 进程继续等待
        self.waittime += 1
        
    def isExit(self): # 进程是否结束
        return self.state == 'exit'
        
    # 修改进程状态    
    def torun(self):
        self.state = 'run'
    
    def toready(self):
        self.state = 'ready'
    
    def toblock(self):
        self.state = 'block'
    
    def toexit(self):
        self.state = 'exit'

def printProcess(readq, runq, blockq, exitq, time):
    '''打印所有进程''' 
    # 分别打印等待队列、运行进程、阻塞队列和完成队列的进程信息
    print('The time is %d:' % time)
    print('name priority arrivetime needtime cputime waittime state ')
    for p in readq: # 等待队列
        print(p)
    if runq: # 运行进程
        print(runq)
    for p in blockq: # 阻塞队列
        print(p)
    for p in exitq: # 完成队列
        print(p)
        
def incProcess(readq, time):
    '''增加就绪队列的所有进程的等待时间'''
    # cpu在运行过程中，就绪队列中的进程等待时间需要增加
    for p in readyQ:
        if p.arrivetime < time:
            p.wait()

'''       
def runProcess(readyQ, runpro, blockQ, exitQ, time):
    # 这段代码无法正确运行
    global exitcnt
    runpro.run()
    for p in readyQ:
        if p.arrivetime < time:
            p.wait()
    if runpro.isExit():
        exitQ.append(runpro)
        runpro = None # 此处的None无法正确返回
        exitcnt += 1
    printProcess(readyQ, runpro, blockQ, exitQ, time)
'''
       
if __name__ == '__main__':
    n = eval(input("请输入进程数目:"))
    # 因为python内置的queue模块无法遍历队列各个元素，所以用list实现queue的功能
    readyQ = []
    blockQ = []
    exitQ = []
    print('请输入进程的名字，到达时间，需要运行的时间：', end='')
    inputstring = ''
    for i in range(n):
        inputstring = input()
        inputlist = inputstring.split()
        readyQ.append(PCB(inputlist[0], eval(inputlist[1]), eval(inputlist[2])))
    # 选择算法
    command = eval(input('请选择调度算法:\n0: 先来先服务\n1: 时间片轮转\n2: 最短时间优先\n'))
    print()
    time = 0
    exitcnt = 0
    runpro = None
    if command == 0:
        '''先来先服务算法'''
        # 先对就绪队列按照到达时间进行排序
        readyQ = sorted(readyQ, key=lambda item: item.arrivetime)
        while exitcnt < n: # 当完成的进程数目小于输入的进程数目时就进入循环
            if not runpro: # 此时cpu空闲
                # 如果此时刻的就绪队列中有进程存在
                if readyQ and readyQ[0].arrivetime <= time:
                    runpro = readyQ.pop(0) # 弹出进程
                    # runProcess(readyQ, runpro, blockQ, exitQ, time)
                    runpro.run() # 转为运行态
                    incProcess(readyQ, time) # 增加等待队列中的进程的时间
                    # 判断进程是否结束
                    if runpro.isExit():
                        exitQ.append(runpro)
                        runpro = None
                        exitcnt += 1
                    # 打印所有进程
                    printProcess(readyQ, runpro, blockQ, exitQ, time)
                else: # 如果此时刻的就绪队列中没有进程存在
                    print('The time is %d:' % time)
                    print('None')
            else:
                # runProcess(readyQ, runpro, blockQ, exitQ, time)
                runpro.run()
                incProcess(readyQ, time) # 增加等待队列中的进程的时间
                # 判断进程是否结束
                if runpro.isExit():
                    exitQ.append(runpro)
                    runpro = None
                    exitcnt += 1
                printProcess(readyQ, runpro, blockQ, exitQ, time)
            time += 1
    elif command == 1:
        '''时间片轮转'''
        timeslice = eval(input('请输入时间片大小：'))
        pertime = timeslice
        readyQ = sorted(readyQ, key=lambda item: item.arrivetime) # 按照到达时间排序
        while exitcnt < n: # 当完成的进程数目小于输入的进程数目时就进入循环
            if not runpro:
                if readyQ[0].arrivetime <= time:
                    runpro = readyQ.pop(0)
                    # runProcess(readyQ, runpro, blockQ, exitQ, time)
                    runpro.run()
                    pertime -= 1 # 时间片计时
                    incProcess(readyQ, time) # 增加等待队列中的进程的时间
                    if runpro.isExit():
                        exitQ.append(runpro)
                        runpro = None
                        exitcnt += 1
                    printProcess(readyQ, runpro, blockQ, exitQ, time)
                else:
                    print('The time is %d:' % time)
                    print('None')
            else:
                # runProcess(readyQ, runpro, blockQ, exitQ, time)
                runpro.run()
                pertime -= 1 # 时间片计时
                incProcess(readyQ, time) # 增加等待队列中的进程的时间
                if pertime == 0: # 时间片用完的情况
                    if runpro.isExit(): # 该进程运行结束，转入结束态
                        exitQ.append(runpro)
                        runpro = None
                        exitcnt += 1
                    else: # 该进程未结束，转入就绪态
                        runpro.toready()
                        readyQ.append(runpro)
                        runpro = None
                printProcess(readyQ, runpro, blockQ, exitQ, time)
            time += 1
            if pertime == 0: # 一个时间片用完需要回复初值
                pertime = timeslice

    elif command == 2:
        '''最短时间优先'''
        readyQ = sorted(readyQ, key=lambda item: item.arrivetime)
        while exitcnt < n: # 当完成的进程数目小于输入的进程数目时就进入循环
            if not runpro:
                index = 0 # 指示第一个最短时间的进程的索引
                flag = True # True表示就绪队列首元素的到达时间>cpu当前时刻的时间
                            # False表示首元素是拥有最短时间的进程
                for i in range(len(readyQ)): # 查找最短时间的进程
                    if readyQ[i].arrivetime > time:
                        break
                    if readyQ[i].needtime <= readyQ[index].needtime:
                        index = i
                        flag = False
                if index == 0 and flag: # 还未找到满足条件的进程
                    print('The time is %d:' % time)
                    print('None')
                else:
                    runpro = readyQ.pop(index)
                    # runProcess(readyQ, runpro, blockQ, exitQ, time)
                    runpro.run()
                    incProcess(readyQ, time) # 增加等待队列中的进程的时间
                    if runpro.isExit(): # 判断进程是否结束
                        exitQ.append(runpro)
                        runpro = None
                        exitcnt += 1
                    printProcess(readyQ, runpro, blockQ, exitQ, time)
            else:
                # runProcess(readyQ, runpro, blockQ, exitQ, time)
                runpro.run()
                incProcess(readyQ, time) # 增加等待队列中的进程的时间
                if runpro.isExit(): # 判断进程是否结束
                    exitQ.append(runpro)
                    runpro = None
                    exitcnt += 1
                printProcess(readyQ, runpro, blockQ, exitQ, time)
            time += 1
    else:
        print('输入错误!')

    
        
        
