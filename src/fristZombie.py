#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''
import os,time,signal,traceback

def childhandler(signum,stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
            print result 
        except OSError,e:
            print "error2 ",e
            break
        print "Reaped child process %d" % result[0]
    signal.signal(signal.SIGCHLD,childhandler)

print "Before the fork,My Pid is %d" % os.getpid()

signal.signal(signal.SIGCHLD,childhandler)

pid = os.fork()
if pid :
    print "Hello from the parent .The child will be pid ",pid
    print "Sleeping 40 s...."
    time.sleep(100)
    print "praent ok"#任何信号处理程序被调用，睡眠立即终止
else:
    print "Child sleeping 5 s"
    time.sleep(5)
    


    
#os.waitpid(-1, os.WNOHANG)

