#!/usr/bin/env python
#coding=utf-8
#导入相关模块
import MySQLdb
 
#建立和mysql数据库的连接
conn = MySQLdb.connect(host='localhost',user='root',passwd='123456')
#获取游标
curs = conn.cursor()
#选择连接哪个数据库
conn.select_db('test')
#执行SQL,创建一个表
rs=curs.execute("select * from student")

print rs
print curs.fetchone()
#提交修改                               
conn.commit()
#关闭游标连接,释放资源
curs.close()
#关闭连接
conn.close()
