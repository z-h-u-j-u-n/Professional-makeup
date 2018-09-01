#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 19:58:40 2018

@author: zhujun
"""

from socket import *

serverName = '127.0.0.1'
serverPort = 11112
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Please input lower sentense: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    if message.upper() == 'QUIT':
        break
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage)
clientSocket.close()