
# =========1、尝试mysql语句读取表中的列标题===========
import csv
import pymysql
import MySQLdb
# con=MySQLdb.connect(user='xiaozhou',password='xiaozhou',host='localhost',\
# db='test1',port=3306,charset='utf8')
# cur=con.cursor()
# cur.execute("select column_name from information_schema.columns \
# where table_name='firsttest';")
# rows=cur.fetchall()
# header_list=[]
# for row in rows:
	# 输出为元组，"('name',)"形式，所以要去掉逗号，再取其中的值。。机智如我
	# header_list.append(str(row).replace(',','')[2:-2])
# print(header_list)
#
#================2、测试for表达式================
#格式：
#result = [dosomething(x) for x in iterator]
#
lst = [1,2,3,4]
# [print(x*x,end=".") for x in lst]   # 1.4.9.16.


# ---------------------3、测试map(func,iterator)函数-----------------------

def getSqure(x):
	return x*x

multi = list(map(getSqure,lst))
# print(multi)   # [1, 4, 9, 16]


# multi = list(map(str,lst))
# print(multi)   # ['1', '2', '3', '4']

# ---------------------4、测试zip(iterator1,iterator2,iterator3,...)函数-----------------------

s = ['a','b','c','d']
# d = dict(zip(lst,s))
# print(d)   # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

d = list(zip(lst,s))
# print(d)   # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# ---------------------5、测试正则表达式中 .*?和 .*-----------------------

import re
# s = "aaabc11123aaabc"
# # print(s)


# pattern_1 = re.compile('a.*?b')
# match_1 = pattern_1.findall(s)
# print(match_1)   # ['aaab', 'aaab']

# match_3 = pattern_1.findall(s)
# print(match_3)

# pattern_2 = re.compile('a.*b')
# match_2 = pattern_2.findall(s)
# print(match_2)    # ['aaabc11123aaab']


# ---------------------6、测试requests中param参数使用-----------------------
import requests


# ua_headers = {"User-Agent":"Mozilla/5.0 (compatiable; MSTE 9.0; Windows NT 6.1 Trident/5.0;)"}

url = "http://tieba.baidu.com/f"
# params = {"kw":"清华大学","pn":"50"}
# res = requests.get(url,params=params,headers=ua_headers)
# html = res.text
# print(type(html))   # <class 'str'>
# print(res.text)   # 正常显示
# content = res.content
# print(type(content))   # <class 'bytes'>
# print(content)

# myUrl = url+"?"   # 可以加
# myRes = requests.get(myUrl,params=params,headers=ua_headers)
# html = myRes.text
# print(type(html))   # <class 'str'>
# print(html)   # 正常显示
# content = myRes.content
# print(type(content))   # <class 'bytes'>
# print(content)

# ---------------------7、测试urllib 中的 read返回类型-----------------------
import urllib

# res = urllib.request.urlopen(url)
# print(res)   # <http.client.HTTPResponse object at 0x00000045DBF754A8>
# html = res.read()   # <class 'bytes'>
# print(type(html))
# print(html)   # 乱码---因为是bytes格式
# html = html.decode()   # 将bytes格式转为str
# print(html)  # 正常

# ---------------------8、测试requests打开图片链接返回内容并存储图片----------------------

# imageUrl = "http://imgsrc.baidu.com/forum/w%3D580/sign=18d28a24516034a829e2b889fb1249d9/f7db2f2eb9389b50ce35e3778835e5dde6116ed3.jpg"

# imageRes = requests.get(imageUrl)
# imageHtml = imageRes.text
# image_content = imageRes.content
# # print(imageHtml)   # 一堆乱七八糟的符号
# # print(image_content)  # 一堆字符

# with open('./'+str(1)+'.png','wb') as imageFile:  # image里是二进制内容，要用wb
# 			# imageFile.write(imageHtml)   # 存储失败，文件存在，但无法打开，因为空文件
# 			imageFile.write(image_content)   # 成功存储该图片


# ---------------------9、time模块操作----------------------
import time

# cur_time = time.time()   # 返回float类型--从1970年1月1日 00：00点开始，按秒计算
# print("cur_time: \t"+str(int(cur_time)))

# local = time.localtime()  # [seconds] --> tm_year,9个元素的数组
# print(local)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=5, tm_hour=20, tm_min=29, tm_sec=34, tm_wday=2, tm_yday=248, tm_isdst=0)



# s = '2018-9-5 20:37:00'
# strp = time.strptime(s,"%Y-%m-%d %H:%M:%S")   # 将格式字符串转化为struct_time日期格式
# # print(strp)
# # time.struct_time(tm_year=2018, tm_mon=9, tm_mday=5, tm_hour=20, tm_min=29, tm_sec=34, tm_wday=2, tm_yday=248, tm_isdst=-1)

# strf = time.strftime("%Y-%m-%d %H:%M:%S",strp)   # 把时间元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串，
# # 格式由参数format决定。如果未指定，将传入time.localtime()。
# print(strf)   # 2018-09-05 20:37:00

# down = time.mktime(strp) # 元组 --> float
# print(down) #  1536151020.0


# ---------------------10、time 模块倒计时----------------------
import sys
from datetime import datetime

end_time = "2018-09-05 21:32:30"  # 设置结束时间
# print("end_time:\t"+end_time)

# time.strptime
# datetime模块中的strptime
# end_time = datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")   # 转化为struct_time日期格式
# print(type(end_time))  # <class 'datetime.datetime'>
# print(end_time)  # 2018-09-05 20:55:00
# end_time = int(time.mktime(end_time.timetuple()))
# print(end_time)   # 1536152100

# time模块中的strptime  --元组
# end_time = time.strptime(end_time,"%Y-%m-%d %H:%M:%S")
# print(type(end_time))  # <class 'time.struct_time'>
# print(end_time)
# end_time_count = int(time.mktime(end_time))
# print(end_time)   # 1536152100


# while True:
# 	time.sleep(1)
# 	cur_time_count = time.time()  # 获取当前时间戳 秒
# 	cur_time = time.localtime(cur_time_count) # 将时间戳转为struct_time元组
# 	cur_time = time.strftime("%Y-%m-%d %H:%M:%S",cur_time)
# 	print("cur_time:\t"+cur_time)

# 	left_time_count = int(end_time_count - cur_time_count)  # 剩余时间差，秒
# 	print(left_time_count)
# 	if left_time_count <= 0:
# 		print("clock clock")
# 		time.sleep(1)
# 		sys.exit()


# ---------------------10、msvcrt 模块---------------------
import msvcrt

anykey = msvcrt.getch()

# 一种用法
# print(type(anykey))   # bytes类型
# print(anykey)
# if anykey in [b'\r',b'\n',b'\t',b' ']:
# 	print(anykey)
# 	sys.exit()
# else:
# 	print("try again")

# 第二种用法
# print("按任意键结束：")
# oanykey = ord(anykey)
# print(type(oanykey))    # int类型
# print(oanykey)   #

# if oanykey in range(0,256):
# 	print("run run")
# 	sys.exit()
# else:
# 	print("try again")


# enter--b'\r'
# space ---b' '
# tab--b'\t'


# ---------------------12、tkinter 模块中的message测试---------------------
from tkinter import *
import tkinter.messagebox


# init_window = Tk()
# init_window.title("批量邮件发送 - By 小周")
# init_window.geometry('400x300+400+300')
# init_window.attributes('-alpha',1)


# # 	# box系列
# # 圆圈蓝色感叹号
# # tkinter.messagebox.showinfo(title="温馨提示",message="试用期已过，如需续用，请联系作者邮箱：\n小周 <1358304569@qq.com>")
# # 三角黄色感叹号
# # tkinter.messagebox.showwarning(title="温馨提示",message="试用期已过，如需续用，请联系作者邮箱：\n小周 <1358304569@qq.com>")
# # 圆圈红色打×
# tkinter.messagebox.showerror(title="温馨提示",message="试用期已过，如需续用，请联系作者邮箱：\n小周 <1358304569@qq.com>")
# init_window.mainloop()


# ---------------------13、倒计时 弹窗---------------------

# def if_expired(end_time):
# 	cur_time = int(time.time())
# 	left_time = end_time - cur_time

# 	if left_time <= 0:
# 		init_window = Tk()
# 		init_window.title("批量邮件发送 - By 小周")
# 		init_window.geometry('400x300+400+300')
# 		init_window.attributes('-alpha',1)
# 		tkinter.messagebox.showerror(title="温馨提示",message="试用期已过，如需续用，请联系作者邮箱：\n小周 <1358304569@qq.com>")
# 		init_window.mainloop()
# 		print("已过期，提示完")
# 		sys.exit()
# 	else:
# 		pass

# end_time = "2018-09-09 13:50:30"
# end_time = time.strptime(end_time,"%Y-%m-%d %H:%M:%S")
# end_time = int(time.mktime(end_time))
# if_expired(end_time)
# print("判断完后")



# ---------------------14、函数调用和返回测试---------------------

# 1、没有return
# def my_swap(x, y):
# 	x, y = y, x
# print(my_swap(1, 2))			# None

# 2、有 return，直接打印
# def my_swap(x, y):
# 	x, y = y, x
# 	return x, y

# print(my_swap(1, 2))			# (2, 1)


# # 3、有 return, 函数调用
# l1 = [1, 2]
# for i in range(len(l1)-1):
# 	my_swap(l1[i], l1[i+1])

# print(l1)			# [1, 2]

# # 4、有 return, 函数调用，再返回
# l2 = [1, 2]
# for i in range(len(l2)-1):
# 	l2[i], l2[i+1] = my_swap(l2[i], l2[i+1])

# print(l2)			# [2, 1]












