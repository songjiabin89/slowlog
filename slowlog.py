#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年11月27日

@author: 宋家斌
'''
##################################
#此脚本是用来发送Mysql慢查询日志信息到邮箱内。#
##################################



import mail,os

#FILEPATH='/home/yx/slow.log'
#MYSQLCMD='/usr/bin/mysqldumpslow'

send_info_file_path = "/home/yx/"


if os.path.exists(send_info_file_path + 'sendinfo.txt'):
    os.remove(send_info_file_path + 'sendinfo.txt')
else:
    pass
#移除上次写入的邮件缓存文件。

slow_log_info = os.popen("/usr/bin/mysqldumpslow -s al -t 10 /home/yx/slow.log").read()
#读取慢查询日志内容。
slow_log_info_forma = slow_log_info.replace('\n','')
low_log_list = slow_log_info_forma.split('Count')
#将读取的慢日志进行格式化。
for i in range(len(low_log_list)):
    if low_log_list[i] =='':
        pass
    else:
        write_info = "Count" + low_log_list[i]
        change_info = '%s<br />' %write_info
        send_info_file = open(send_info_file_path + 'sendinfo.txt','a+')
        send_info_file.write(change_info + "\n" + '<br />' + "\n")
        send_info_file.close()
#以上是将列表内的空值移除，并将非空信息写到sendinfo.txt文件内。

echo_log = os.popen("echo > /home/yx/slow.log")
note = '注:以上为上周慢查询出现次数最多的前十条语句信息。<br />'
send_file = file(send_info_file_path + 'sendinfo.txt')
send_file_info = send_file.read()
send_info = '<html><body> %s\n%s </body></html>' %(send_file_info,note)
mail.sm('web_server@p2peye.com','Mysql慢日志查询信息',send_info)
#mail.sm('songjiabin89@163.com','Mysql慢日志查询信息',send_info)
#以上是将文件信息进行格式整理并以邮件的形式发送出去。


