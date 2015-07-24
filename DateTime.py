#!/usr/bin/python
# coding:utf-8
import time
import datetime
'''
日期时间的基本操作
'''
def getNow():
    now = int(time.time())
    #now1=datetime.datetime.now()# 2015-07-23 12:58:37.890000
    #now1=datetime.datetime.today()#2015-07-23 12:58:14.749000
    return now
#print getNow()


if __name__ == '__main__':
    print getNow()
   