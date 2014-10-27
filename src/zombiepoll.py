#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

import os, time
from Carbon.AppleEvents import pID
 
def reap():
    while 1:
        print "while"
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print 'reaped child process %d' % result[0]

print "Before the fork ,my PID is " , os.getpid()

pid = os.fork()
if pid:
    print "Hello from the parent. The child PID %d" % pid
    print "Parent sleeping 20s"
    time.sleep(20)
    print "Parent sleep done"
    reap()
    print "Parent sleeping 20s"
    time.sleep(20)
    print "Parent sleep done"

else:
    print 'child sleeping 5s'
    time.sleep(5)
    print "Child terminating "



