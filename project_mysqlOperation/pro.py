#!/usr/bin/env python
#coding=utf-8
#导入相关模块
import MySQLdb
 
#建立和mysql数据库的连接
conn = MySQLdb.connect(host='localhost',user='root',passwd='123456')
#获取游标
curs = conn.cursor()
#执行SQL,创建一个数据库
curs.execute("create database pythondb")
#选择连接哪个数据库
conn.select_db('pythondb')
#执行SQL,创建一个表
curs.execute("create table test(id int,message varchar(50))")
#插入一条记录
value = [1,"davehe"]
curs.execute("insert into test values(%s,%s)",value)
#插入多条记录
values = []
for i in range(20):
    values.append((i,'hello mysqldb' + str(i)))
curs.executemany("insert into test values(%s,%s)",values)
#提交修改                               
conn.commit()
#关闭游标连接,释放资源
curs.close()
#关闭连接
conn.close()

    
























        
