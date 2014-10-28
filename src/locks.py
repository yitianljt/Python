#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月28日

@author: jintao
'''

import threading,time

b=50
l = threading.Lock()

def threadcode():
    global b
    print "Thread %s invoked " % threading.currentThread().getName()
    l.acquire()
    try:
        print "Thread %s running" % threading.currentThread().getName()
        time.sleep(1)
        b+=50
        print "Thread %s set b = %d" % (threading.currentThread().getName(),b)
    finally:
        l.release()
        
print "Value of b at start of program:",b
childthreads = []

for i in range(1,5):
    t = threading.Thread(target=threadcode,name = "Thread-%d"%i)
    t.setDaemon(True)
    t.start()
    childthreads.append(t)
    

for t in childthreads:
    t.join()
    
print "New value of b:",b



