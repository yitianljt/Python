#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

import os,time

print "Before the fork,my pid is:",os.getpid()

if os.fork():
    print "Hello from the parent.My PID is :",os.getpid()
else:
    print "Hello from the child .My Pid is :",os.getpid()

print "Hello from both os us"
    