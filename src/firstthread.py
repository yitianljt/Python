#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月28日

@author: jintao
'''
import threading , time,sys

def sleepandprint():
    time.sleep(5)
    print "Hello from both of us."

def threadcode():
    sys.stdout.write("Hello from the new thread.My name is %s\n" % threading.currentThread().getName())
    sleepandprint()


print "Before starting a new threading my name is %s " % threading.currentThread().getName()

#create new thread
t = threading.Thread(target=threadcode,name="ChildThread")
t.setDaemon(1)#主线程结束后，会杀掉子线程
t.start()
sys.stdout.write("Hello from the main thread. my name is %s\n" % threading.currentThread().getName())
sleepandprint()
t.join()
print "Last print "






