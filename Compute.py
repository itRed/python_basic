#!/usr/bin/python
#coding:utf-8
import os
import urllib
'''
测试脚本：四则运算器
'''
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#print getHtml('http://www.sina.com')
 
def getNumber():
    number1 = int(raw_input('Please input the number1:'))
    number2 = int(raw_input('Please input the number2:'))
    print number1,'+',number2,'=',number1+number2
    print number1,'-',number2,'=',number1-number2
    print number1,'*',number2,'=',number1*number2
    print number1,'/',number2,'=',number1/number2   
    
getNumber()
