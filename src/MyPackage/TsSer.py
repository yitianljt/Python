#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月25日

@author: jintao
'''

from socket import * 
from time  import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connect from :',addr
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime() ,data))
    tcpCliSock.close()
tcpSerSock.close()
        
            
