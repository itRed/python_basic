#!/usr/bin/python
# coding:utf-8
# @author: Red(it_red@sina.com)
# @version: 1.0
'''
打印99表
'''

def printJJT():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print i, '*', j, '=', i * j, ' ',
        print ''

if __name__ == '__main__':
    printJJT()
    print '完成'

