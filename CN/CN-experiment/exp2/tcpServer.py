#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:10:29 2018

@author: zhujun
"""

from socket import *
import time

# 建立服务器套接字
s = socket(AF_INET, SOCK_STREAM)
# 服务器地址和端口
serverAddress = '127.0.0.1'
serverPort = 10009
# 套接字绑定地址和端口
s.bind((serverAddress, serverPort))
# 最大允许5个连接
s.listen(5)
print('The server is waiting for connecting...')
# 收到的连接请求和连接地址，端口
sock, addr = s.accept()
print('The server gets new connection from %s:%s' % addr)

while True: # 数据传输
    message = sock.recv(1024)
    print('The message is ', message.decode('utf-8'))
    if message.decode('utf-8') == 'quit':
        break
    else:
        sock.send(message.upper())
s.close()
print('Connection is closed from %s:%s' % addr)