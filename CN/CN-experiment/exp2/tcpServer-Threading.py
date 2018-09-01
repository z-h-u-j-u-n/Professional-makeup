#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:36:53 2018

@author: zhujun
"""

from socket import *
from threading import Thread
import time

class tcpLink(Thread):
    '''tcp连接的线程'''
    
    def __init__(self, name, sock, addr):
        # 初始化
        Thread.__init__(self, name=name)
        self._sock = sock
        self._addr = addr
        
    def run(self):
        # 数据传输
        print('Accept new connection from %s:%s...' % addr)
        while True:
            message = self._sock.recv(1024)
            # time.sleep(1)
            print('The message is ', message.decode('utf-8'))
            if message.decode('utf-8') == 'quit':
                break
            else:
                self._sock.send(message.upper())
        sock.close()
        print('Connection from %s:%s closed.' % self._addr)    
    


    
# =============================================================================
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     # sock.send(b'Welcome!')
#     while True:
#         message = sock.recv(1024)
#         time.sleep(1)
#         print('The message is ', message.decode('utf-8'))
#         if message.decode('utf-8') == 'quit':
#             break
#         else:
#             sock.send(message.upper())
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
# =============================================================================




# 建立服务器套接字
s = socket(AF_INET, SOCK_STREAM)
# 服务器ip地址和端口
serverAddress = '127.0.0.1'
serverPort = 10009
# 套接字绑定服务器ip地址和端口
s.bind((serverAddress, serverPort))
# 最大允许5个连接
s.listen(5)

print('The server is waiting for connecting...')

while True: # 数据传输
    sock, addr = s.accept()
    #t = threading.Thread(target=tcplink, args=(sock, addr))
    t = tcpLink('tcpLink', sock, addr)
    t.start()
s.close()