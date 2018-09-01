#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:03:01 2018

@author: zhujun
"""

from socket import *

# 建立tcp套接字
s = socket(AF_INET, SOCK_STREAM)
# 服务器ip地址和端口
serverAddress = '127.0.0.1'
serverPort = 10009
# 套接字连接到服务器
s.connect((serverAddress, serverPort))
# print(s.recv(1024))
while True: # 数据传输
    message = input('Please input your data: ')
    s.send(message.encode())
    if message.upper() == 'QUIT':
        break
    print(s.recv(1024))
s.close()
    
