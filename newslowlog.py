#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年11月30日

@author: 宋家斌
'''
import mail,os,re
logcmd = os.popen("/usr/bin/mysqldumpslow -s al -t 10 /home/yx/slow.log").read()
mail.sm('songjiabin89@163.com','Mysql慢日志查信息',logcmd)
