#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 10:10:06 2018

@author: zhujun
"""

"""
courses = [
            '程序设计基础','离散数学',
            '数据结构', '汇编语言',
            '语言的设计与分析', '计算机原理',
            '编译原理', '操作系统',
            '高等数学', '线性代数',
            '普通物理', '数值分析'
          ]
class Node():
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 

graph = [ Node((i, courses[i])) for i in range(12) ]
indegree = [ 0 for i in range(12) ]

# 建立图
graph[0].next = Node((1, courses[1]), graph[0].next)
graph[0].next = Node((2, courses[2]), graph[0].next)
graph[0].next = Node((3, courses[3]), graph[0].next)
graph[0].next = Node((11, courses[11]), graph[0].next)
indegree[1] += 1
indegree[2] += 1
indegree[3] += 1
indegree[11] += 1

graph[1].next = Node((2, courses[2]), None)
indegree[2] += 1

graph[2].next = Node((4, courses[4]), graph[2].next)
graph[2].next = Node((6, courses[6]), graph[2].next)
graph[2].next = Node((7, courses[7]), graph[2].next)
indegree[4] += 1
indegree[6] += 1
indegree[7] += 1

graph[3].next = Node((4, courses[4]), None)
indegree[4] += 1


graph[4].next = Node((6, courses[6]), None)
indegree[6] += 1

graph[5].next = Node((7, courses[7]), None)
indegree[7] += 1

graph[8].next = Node((9, courses[9]), graph[8].next)
graph[8].next = Node((10, courses[10]), graph[8].next)
graph[8].next = Node((11, courses[11]), graph[8].next)
indegree[9] += 1
indegree[10] += 1
indegree[11] += 1

graph[9].next = Node((11, courses[11]), None)
indegree[11] += 1

graph[10].next = Node((5, courses[5]), None)
indegree[5] += 1
print(indegree)
# print(graph[3].next.data)
# 以上均正确
from queue import Queue
q = Queue(20)
k = 0
order = []

for i in range(12):
    if indegree[i] == 0:
        q.put(graph[i])
        
while not q.empty():
    temp = q.get()
    order.append(temp.data[0])
    if temp.data[0] == 3:
        print("daola")
    #print(temp.data)
    while temp.next:
        temp = temp.next
        #print(temp.data)
        indegree[temp.data[0]] -= 1
        if indegree[temp.data[0]] == 0:
            q.put(temp)
print(order)
#for i in range(12):
#    print(order[i]+1, end='->')
"""

'''拓扑排序， 每次从入度表中挑选入度为0的课程进行学习.注意判断有环图的情况'''
# 本题使用的数据结构有：
# 字典g： 实现图的邻接表存储
# 列表indegrees： 存储每个节点的入度
# 列表q： 存储入度为0的顶点，当列表为空，说明学习完毕

g = {
        '1': ['2', '3', '4', '12'],
        '2': ['3'],
        '3': ['5', '7', '8'],
        '4': ['5'],
        '5': ['7'],
        '6': ['8'],
        '7': [],
        '8': [],
        '9': ['10', '11', '12'],
        '10':['12'],
        '11':['6'],
        '12':[]
    }
indegrees = dict((u, 0) for u in g.keys())
for u in g.keys():
    for v in g[u]:
        indegrees[v] += 1
q = [ u for u in g.keys() if indegrees[u] == 0 ]
s = []
k = 0
while q:
    u = q.pop()
    k += 1
    s.append(u)
    for v in g[u]:
        indegrees[v] -= 1
        if indegrees[v] == 0:
            q.append(v)
if k != len(g):
    print('图有环')
else:          
    print(s)













    