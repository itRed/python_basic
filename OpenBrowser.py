#!/usr/bin/python
# coding:utf-8
# @author: Red(mail:it_red@sina.com)
# @version: 1.0
'''
  python打开浏览器并跳转到指定网站
'''
import webbrowser

def openBrowser():
    url = 'www.cnblogs.com/itred'
    webbrowser.open(url)
    print webbrowser.get()
    
if __name__ == '__main__':
    openBrowser()
