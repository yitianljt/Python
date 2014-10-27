#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)


while True:
    print 'waiting for message...'
    data ,addr = udpSerSock.recvfrom(BUFFSIZE)
    udpSerSock.sendto('[%s] %s' %(ctime(),data) ,addr)
    
    print '...received from and returned to :' , addr
udpSerSock.close()
    
    
    
    
    