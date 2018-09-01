#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:14:32 2018

@author: zhujun
"""
from socket import *

serverName = '127.0.0.1'
serverPort = 11112
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

print('the server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Server received from %s:%s and the data is' % clientAddress)
    print('\tdata: ' + str(message))
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
serverSocket.close()
