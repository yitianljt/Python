#!/usr/bin/python
#encoding:utf-8

import socket
s=socket.socket()
s.bind(('localhost',21111))    #ip地址和端口号
s.listen(5)
cs,address = s.accept()
print 'got connected from',address
cs.send('byebye')
ra=cs.recv(512)
print ra
cs.close()
