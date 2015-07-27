#!/usr/bin/python
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

print getHtml("http://www.baidu.com")
