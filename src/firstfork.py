#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

import os ,time

print "Before the fork,my pid is %d" % os.getpid()

if os.fork():
    print "Hello from the parent .My pid is %d"% os.getpid()
else:
    print "Hello from the child .My pid is %d" % os.getpid()

print "hello from both of us ."
