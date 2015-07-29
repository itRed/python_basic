#!/usr/bin/python
# coding:utf-8
# @author: Red
import base64

'''base64加密'''
def getEncodeStr(str):
    return base64.encodestring(str)

'''base64解密'''
def getDecodeStr(str):
    return base64.decodestring(str)

if __name__ == '__main__':
    str = 'This is Base64.测试'
    en = getEncodeStr(str)
    de = getDecodeStr(en)
    print en
    print de
