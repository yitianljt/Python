#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月28日

@author: jintao
'''
import threading ,time

a=50
b=50
c=50
d=50

def printvars():
    print "a=", a
    print "b=", b
    print "c=", c
    print "d=", d
    
def threadcode():
    global a,b,c,d
    a+=50
    b= b+50
    c=100
    d= "hello"
    print "[ChildThread] values of variables in child thread"
    printvars()
    
    
print "[MainThread] values of variables before child thread:"

printvars()

t = threading.Thread(target=threadcode,name = "ChildThread")
t.setDaemon(True)
t.start()
t.join()

print "[MainThread] values of variables after child thread:"
printvars()


