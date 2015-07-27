#!/usr/bin/python
#coding:utf-8
#文件内容追加，从0到9的随机整数, 10个数字一行，共10行
import random

f=open('f.txt','a')
for i in range(0,10):
    for i in range(0,10):
        f.write(str(random.randint(0,9)))
    f.write('\n')
f.close()
