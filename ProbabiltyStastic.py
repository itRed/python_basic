#!/usr/bin/python
# coding:utf-8

import random
'''
概率统计：模拟实现掷硬币正反面的概率
'''
def getRandom():
    possible1 = 0
    possible2 = 0
    total = 0
    for i in range(1, 1000000):
        k = random.randint(0, 1)
        if k == 0:
            possible1 += 1
        elif k == 1:
             possible2 += 1
        
    print possible1, '=possible1'
    print possible2, '=possible2'
    total = possible1 + possible2
    print '出现0的概率为:', float(possible1) / float(total)
    print '出现1的概率为:', float(possible2) / float(total)

getRandom()
'''output:
500377 =possible1
499622 =possible2
出现0的概率为: 0.500377500378
出现1的概率为: 0.499622499622
'''