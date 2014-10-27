#!/usr/bin/python
#encoding:utf-8

import socket
s=socket.socket()
s.connect(('localhost',21111))   #与服务器程序ip地址和端口号相同
data=s.recv(512)
s.send('hihi')
s.close()
print 'the data received is',data