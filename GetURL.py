#!/usr/bin/python
# coding:utf-8
# @author: Red(it_red@sina.com)
# @version: 1.0

import re
import urllib

def getHtml(url):
    html = unicode(urllib.urlopen(url).read(), "GBK")
    html = html.encode("UTF-8")
    return html
    
def getURL(html):
    try:   
        f = open('itRed.txt', 'w')
        p = re.compile('<a .*?><a .*? href="(.*?)">(.*?)</a>')
        for url, name in p.findall(html):
            f.write(url + '\n')
            # print '%s(%s)' % (name, url)
    finally:
        f.close()

if __name__ == '__main__':
    url = 'http://search.51job.com/list/%2B,%2B,%2B,%2B,%2B,%2B,%25CA%25FD%25BE%25DD%25B7%25D6%25CE%25F6,1,%2B.html?lang=c&stype=1'    
    getURL(getHtml(url))
    print '获取数据成功！'
    
'''
url = 'http://search.51job.com/list/%2B,%2B,%2B,%2B,%2B,%2B,%25CA%25FD%25BE%25DD%25B7%25D6%25CE%25F6,1,%2B.html?lang=c&stype=1'
p = re.compile('<a .*?><a .*? href="(.*?)">(.*?)</a>')
webpage = unicode(urllib.urlopen(url).read(), "GBK")
webpage = webpage.encode("UTF-8")

for url, name in p.findall(webpage):
    print '%s(%s)' % (name, url)
'''
