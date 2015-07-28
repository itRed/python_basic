#!/usr/bin/python
# coding:utf-8
# @author: Red(mail:it_red@sina.com)
# @version: 1.0

'''递归算法案例'''

'''计算1+2+3+...+99+100'''
def foo(n):
    if n > 0:return n + foo(n - 1)
    if n <= 0:return 0

'''阶乘'''
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


'''
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第
　　　3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后 
　　　问第一个人，他说是10岁。请问第五个人多大？
'''
def fun(i):
    if i == 1:
        return 10
    return fun(i - 1) + 2


if __name__ == '__main__':
    print foo(100)
    # print fun(5)
    print fac(9)


