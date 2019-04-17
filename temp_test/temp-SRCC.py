# 这是一个临时测试的temp文件，用于各种小测试

# ===================1、测试常量类conost.py=====================

# import const 
# const.value = 'ZYJ'
# VAR = const.value
# print(VAR)
# VAR = 'zwj'
# print(VAR)
# const.name = 'ZWJ'  # const.ConstError: Can`t rebind const(name)


# ===================2、测试numpy中的 loadtxt =====================

import numpy as np

# # 测试导入txt文件，n行*1列，一行为一个数据，
# y = np.loadtxt(r'C:\Users\user\Desktop\0109_point19_test\point_19\test_0-2570s.asc')

# # print(y)

# ===================3、测试一些python内置函数 =====================

# 最大 最小值（可以指定默认值）
# lst = [1255,2200,3700,4500,4900,6500]
# print(min(lst))
# print(max(lst))


# ===================4、测试matplotlib的show()函数后不继续运行程序 =========未解决=================

import matplotlib.pyplot as plt 

# # 开启交互模式
# # plt.ion()    # 图像一闪而过，看不见


# x = np.linspace(0, 10)
# y = np.sin(3.14*x)

# # 开始画图
# print("plot begin ")

# plt.figure(figsize=(20,8))

# # 画出原始数据 x--y
# plt.plot(x,y,"k--")

# plt.xlabel("Time in s")
# plt.ylabel("uE")
# plt.title("test_mat_1")
# plt.show()
# # plt.draw() 
# print("plot end ")


# ================5、将csv文件读取为字典=====================

import csv
# addr_file = r'C:\Users\zwj\Desktop\MailMaster\邮箱联系人表单.csv')

# with open(addr_file,'r',encoding='gbk') as addrFile: 
 # iterator should return strings, not bytes (did you open the file in text mode?
 # 因为此csv文件并非二进制文件，而是文本文件
 # 'utf-8' codec can't decode byte 0xd6 in position 0: invalid continuation byte
 # 用utf-8不能解码，改用gbk
	
	# reader = csv.reader(addrFile)
	# name = []
	# value = []
	# for row in reader:
	# 	name.append(row[0])
	# 	value.append(row[1])
	

# print(name)
# print(type(name))
# print(value)

# addrs = {}  # 用来存放字典
# for i in range(len(name)):
# 	addrs[name[i]] = value[i]

# print(addrs)
# name = '朱'
# print(addrs[name])

# ================================6、截取人名==========================

# att_name = ["结算款_1_周","结算款_2_朱朱"]
# person_name = []
# for name in att_name:
# 	person_name.append(name.split("_")[-1])

# print(person_name)  # ['周', '朱朱']


# ==================================7、获取文件完整路径=============================
import os

# attach_path = r'C:\Users\zwj\Desktop\MailMaster\attchfile'

# for root,dirs,files in os.walk(attach_path):
# 	print(root)   # C:\Users\zwj\Desktop\MailMaster
# 	print(dirs)   # ['attchfile']
# 	print(files)
# 	for file in files:
# 		print(root+"\\"+file)

	# C:\Users\zwj\Desktop\MailMaster
	# attchfile']
	#     ntent.txt', 'DefaulServerAdd.png', 'exampl.png', 'MailTest_1.py', 'MailTest_2.py', 'recv.txt', 'temp.py', '邮箱联系人表单.csv']
	#C:\Users\zwj\Desktop\MailMaster\attchfile
	#[]
	#['结算款_1_周.xlsx', '结算款_2_朱.xlsx']


# =======================8、测试zip函数====================

# name = ["周","朱朱"]
# value = ["11","22"]

# # addrs = {}  # 用来存放字典
# # for i in range(len(name)):
# # 	addrs[name[i]] = value[i]

# addrs = zip(name, value)
# print(addrs)   # <zip object at 0x000000000259A108>

# addrs = list(zip(name, value))
# print(addrs)   # [('周', '11'), ('朱朱', '22')]

# addrs = dict(zip(name, value))
# print(addrs)   # {'周': '11', '朱朱': '22'}

# =======================9、测试tkinter中filedialog 模块====================

# import tkinter
# from tkinter.filedialog import *
# from tkinter import *
# from tkinter.constants import *

# def openfile():
# 	filename = askopenfilename(initialdir = r'C:\Users\user\Desktop')
# 	lb.config(text="filename:"+filename)


# init_window = tkinter.Tk()
# init_window.geometry('300x200+300+200')

# lb = Label(init_window,text="")
# lb.pack()
# button_fileopen = Button(init_window,text="openfile",command=openfile)
# button_fileopen.pack()
# init_window.mainloop()

# ===========================10、测试enter键退出=============================
import msvcrt
import sys

# def getRecvAddr(one):
# 	if not one in range(0,9):
# 		print("没有<"+str(one)+">的邮箱地址! 请在联系人中添加此人邮箱后重试。")
# 		print("请按任意键退出程序：",end=' ')
# 		char = input()
# 		if  char == '\n':
# 			time.sleep(2)
# 			sys.exit(0)
# 			# break
# 	# try:
# 	print(str(one))
# 	return one


# # getRecvAddr(1)

# getRecvAddr(20)


# ===========================11、msvcrt 捕获键盘测试=============================
# while True:
# 	# print("while")
# 	# if msvcrt.kbhit():
# 	# 	print("kbhit")
# 	char = ord(msvcrt.getch())
# 	print("getch")
# 	if char in  [10,13,32]:
# 		# b = ord(msvcrt.getch())
# 		# x = a + (b*256)
# 		# # return x
# 		print(char)
# 		print("if")
# 	else:
# 		# return a
# 		print(char)
# 		print("else")
# 	break
	


# ===========================12 生成器测试=============================


# a=1
# b=2

# a,b=a,a+b

# print(a)
# print(b)

# a,b=a+b,a
# # print(a)
# # print(b)

# 测试map输出是不是迭代器

def sum(x):
        return x+1

x = [1,2,3,4]

# a = map(sum,x)
# print(type(a))  #<class 'map'>
# print(next(a))  # 2
# print(next(a))  # 3

# ===========================13 pandas测试=============================

import pandas as pd
import xlrd

# file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\123458#7Waveform_0.125s.XLS'
# df = pd.read_excel(file_name,usecols=[3,4]) # 读取指定列（第4,5列）
# # print(type(df))   # <class 'pandas.core.frame.DataFrame'>

# x = df.iloc[0:,0] # 剔除标题行，取横坐标-时间
# y = df.iloc[0:,1]  # 剔除标题行，取纵坐标-加速度

# # print(type(x))   # <class 'pandas.core.series.Series'>
# # print(y)
# # print(len(y))
# # print(y.values)   # [-0.000658 -0.000686 -0.000574 ... -0.000447 -0.000477 -0.000522]
# # print(type(y.values))  # <class 'numpy.ndarray'>
# ys = list(y.values)
# # print(ys)  # done

# # 求和
# mysum = 0
# for i in range(len(ys)):
# 	mysum += ys[i]
# # from functools import reduce

# print(mysum)



# ===========================14 测试int是四舍五入还是向下取整=============================

a = 1.8
b = 1.2
c = int(a)
d = int(b)
# print(c)     # 1
# print(d)	# 1

# 向下取整

# ===========================15 测试怎么去除头尾的标点符号=============================
import string
# s0 = "~hello,this is a punctuation,,.   "
#
# s1 = s0.strip()
# print(s1)  # "~hello,this is a punctuation,,."
# s2 = s0.strip(string.punctuation)
# print(s2)   # "hello,this is a punctuation,,.   "
# s3 = s1.strip(string.punctuation)
# print(s3)   # "hello,this is a punctuation"

# ===========================16 取CSV文件中的一列=============================

import pandas as pd

# csv_file = r'C:\Users\Administrator\Desktop\point19-22.csv'
# out_file = r'C:\Users\Administrator\Desktop\point19_part.csv'
# df = pd.DataFrame(pd.read_csv(csv_file))
#
# col = df.iloc[:,1]
# col.to_csv(out_file, index=False, sep=',')

# ===========================17 测试dataframe重排索引=============================

data = [[11,12,13,14,15],
        [21,22,23,24,25],
        [31,32,33,34,35]]
#
# df = pd.DataFrame(data)
# print(df)
# df2 = df.drop([1])
# print(df2)
#
# df2['index'] = range(df2.shape[0])
# print(df2)
# df3 = df2.set_index('index')
# print(df2)
# # print(df3)
#
# ===========================18 测试各种左闭右开=============================
# print("----for range 范围----")
# for i in range(5):
#         print(i,end=' ')        # 0 1 2 3 4
# print()
# print("----【:】范围----")
# nums = [0,1,2,3,4,5]
# print(nums[0:4])                # [0, 1, 2, 3]
# print(nums[0:-2])               # [0, 1, 2, 3]
# print(nums[::-1])               # [5, 4, 3, 2, 1, 0]


# ===========================19 编写9*9乘法表=============================

# if else
# for i in range(1, 10):
#     for j in range(1,i+1):
#         if j == i:
#             print(str(j)+"*"+str(i)+"="+str(j*i))
#         else:
#             print(str(j)+"*"+str(i)+"="+str(j*i),end='\t|\t')

# 三目运算符
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(j)+"*"+str(i)+"="+str(j*i),end=("\r\n" if i == j else "\t|\t"))


# ===========================20 排序=============================
# 2019-03-12

import random

# nums = [x for x in range(1,1001)]
# random.shuffle(nums)
# print(nums)

import time
start_time = time.time()


# 1、直接插入排序---0.09209 s
# for i in range(1,len(nums)):
#         j = i - 1
#         if nums[j] > nums[i]:
#                 tmp = nums[i]
#                 nums[i] = nums[j]
#                 j -= 1
#                 while j >= 0 and nums[j] > tmp:
#                         nums[j+1] = nums[j]
#                         j -= 1
#                 nums[j+1] = tmp


# 2、希尔排序----0.01300 s

# n = len(nums)
# increment = n//2
# while increment > 0:
#         for i in range(increment, n):
#                 while i >= increment and nums[i-increment] > nums[i]:
#                         nums[i-increment], nums[i] = nums[i], nums[i-increment]
#                         i -= increment
#         increment = increment//2
#
# end_time = time.time()
# print("耗时："+str(end_time - start_time))
# print(nums)
#


# ===========================21 测试map中的func传参数====partial偏函数=========================
# 2019-03-19

from functools import partial

def format(x):
        return round(float(x*2), 8)

def format_2(x, k):
        return round(float(x * k), 8)

x = [2.15,3.5,5.84,10.684]
k = 0.017

# y = list(map(format, x))
# print(y)
part = partial(format_2, k)
y = list(map(part, x))
print(y)


# # 第一种情况
# y = list(map(format, x))
# print(y)                        # [4.0, 6.0, 10.0, 20.0]
#
# # 第二种情况
# # y2 = list(map(format_2, x, k))
# # print(y2)                      # TypeError: 'float' object is not iterable
#
# # 第三种情况
# # temp = def format_2(x, k)
# # y3 = list(map(temp, x))
# # print(y3)                       # TypeError: can't multiply sequence by non-int of type 'float'
#
# # 第四种情况
# temp2 = partial(format_2, k)
# y4 = list(map(temp2, x))
# print(y4)                        # [20.0, 30.0, 50.0, 100.0]

# ===========================22 partial 偏函数=========================
# 2019-03-19
from functools import partial

def func(a, b, c):
        return  a + b - c

# 按顺序
# part = partial(func, 10, 10)
# y = part(20)
# print(y)
#
# # 按指定
# part_2 = partial(func, b = 10, c = 10)
# y2 = part_2(0)
# print(y2)
#
# part_3 = partial(func, a = 10, c = 10)
# y3 = part_3(0)
# print(y3)

# part = partial(func, b = 10)
# y = part(a=10,c=20)
# print(y)


# def my(a, b, c, d, e):
#         return a + b + c + d + e
#
# part = partial(my,  2,  4)
# y = part(1,3,5)
# print(y)



