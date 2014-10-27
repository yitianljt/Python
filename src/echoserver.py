#!/usr/bin/python
#encoding:utf-8
'''
Created on 2014年10月27日

@author: jintao
'''

import socket,traceback,os,sys
from _socket import AF_INET

def reap():
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
            if not result[0]:
                break
        except:
            break
        print "Reaped child process %d" % result[0]
        
host = ''
port = 51423

s = socket.socket(AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)


print "Parent at %d listening for connections " % os.getpid()

while 1:
    try:
        print "try pid = ",os.getpid()
        clientsocket, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except :
        traceback.print_exc()
        continue

    reap()
    pid = os.fork()
    if pid:
        clientsocket.close()
        continue
    else:
        s.close()
        try:
            print "child from %s being handled by PID %d" %\
            (clientsocket.getpeername(),os.getpid())
            while 1:
                data = clientsocket.recv(4096)
                if not len(data):
                    break
                clientsocket.sendall(data)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()
            
        try:
            clientsocket.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
        sys.exit(0)
         
                
            
        
        
        
        





  