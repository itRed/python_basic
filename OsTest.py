#!/usr/bin/python
# coding:utf-8
# @author: Red
import os
import uuid 
import socket
# print os.system('ping 192.168.1.80')
# print os.system('ipconfig')
# print os.listdir('E:\\')
# print os.path.abspath('')
'''获取机器的MAC地址'''
def get_mac_address(): 
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


#获取本机电脑名
def get_ip():
    myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
    myaddr = socket.gethostbyname(myname)
    print myname
    print myaddr
    return myaddr,'==',myname

if __name__ == '__main__':
    print get_mac_address()
    print get_ip()
