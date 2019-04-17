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

# import numpy as np

# # 测试导入txt文件，n行*1列，一行为一个数据，
# y = np.loadtxt(r'C:\Users\user\Desktop\0109_point19_test\point_19\test_0-2570s.asc')

# # print(y)

# ===================3、测试一些python内置函数 =====================

# 最大 最小值（可以指定默认值）
# lst = [1255,2200,3700,4500,4900,6500]
# print(min(lst))
# print(max(lst))


# ===================4、测试matplotlib的show()函数后不继续运行程序 =========未解决=================

# import numpy as np
# import matplotlib.pyplot as plt 

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

# import csv
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
# import os

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


# ===========================11、=============================
while True:
	# print("while")
	# if msvcrt.kbhit():
	# 	print("kbhit")
	char = ord(msvcrt.getch())
	print("getch")
	if char in  [10,13,32]:
		# b = ord(msvcrt.getch())
		# x = a + (b*256)
		# # return x
		print(char)
		print("if")
	else:
		# return a
		print(char)
		print("else")
	break
	









