#!/usr/bin/python
# coding:utf-8
# @author: Red(it_red@sina.com)
# @version: 1.0

'''Random随机处理方法'''
import random

'''获取随机整数,0~10'''
def getRandInt():
    return random.randint(0, 10)

'''随机选取0~100之间的偶数'''
def getEvenNum():
    return random.randrange(0, 101, 2)

'''随机浮点数'''
def getFloatNum():
    return random.random()

'''随机浮点数范围'''
def getFloatNumRange():
    return random.uniform(1, 10)

'''随机字符'''
def getRandChar():
    return random.choice('abcdefghijklmn!@#$%^&*')

'''在字符串中选取特定数量的字符'''
def getRandCharInRange():
    return random.sample('lkijuhygtfrdbvcx', 5)

'''随机选取字符串'''
def getRandStr():
    return random.choice(['apple', 'panda', 'balana', 'blueberry', 'lemo', 'peer', 'milk', 'water'])

'''乱序'''
def getRandOrder():
    items = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(items)
    return items
if __name__ == '__main__':
    # print getRandInt()
    # print getEvenNum()
    # print getFloatNum()
    # print getFloatNumRange()
    # print getRandChar()
    # print getRandCharInRange()
    # print getRandStr()
    print getRandOrder()
 

