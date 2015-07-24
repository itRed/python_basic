#! /usr/bin/env python   
# coding=utf-8   
'''发送邮件'''
import smtplib
from email.mime.text import MIMEText
_user = "it_red@sina.com"
_pwd = "*******"
_to = "it_wang@foxmail.com"

# 使用MIMEText构造符合smtp协议的header及body
msg = MIMEText("测试_Python发送邮件")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP("smtp.sina.com.cn", timeout=30)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()
