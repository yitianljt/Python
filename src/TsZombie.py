#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

import os,time

print "Before the fork, my pid is :",os.getpid()
pid = os.fork()
if pid:
    print "hello from the parent .The child will be PID:%d" %pid 
    print "Sleeping 12 seconds..."
    time.sleep(12);
    print "12 seconds "

