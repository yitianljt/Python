#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''
from socket import *


HOST = 'localhost'
PORT = 21567
ADDR = (HOST,PORT)
BUFFSIZE = 1024

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFFSIZE)
    if not data:
        break
udpCliSock.close()
