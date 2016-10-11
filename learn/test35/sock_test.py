#!/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('169.254.1.1', 23))

buffer=[]
while (True):
    d=s.recv(16*1024)
    if (d):
        print("%s" % d)
    else:
        break