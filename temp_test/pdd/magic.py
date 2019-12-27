#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zhouyijian
# datetime:2019-11-10 20:04
# software: IntelliJ IDEA




import sys

def magic(values):
    # 长度，判断劣弧和优弧
    n = len(values)
    ma = 0
    cnt = 0
    row = int((n*(n-1))/2)
    arr = [[0 for i in range(3)] for j in range(row)]
    print(arr)
    for i in range(n):
        arr[i][0] = i
        for j in range(i+1,n):
            arr[i][1] = j
            tmp = values[i] + values[j]
            tmp += min((j - i), (n - j + i))
            arr[i][2] = tmp
            if tmp > ma:
                ma = tmp
    for k in range(n):
        if arr[k][2] == ma:
            cnt += 1
    print(ma,cnt)
    # print(cnt)

if __name__ == "__main__":
    # 读取第一行的n
    # n = int(input())
    n = 1
    for i in range(n):
        # 读取每一行
        # line = sys.stdin.readline().strip()
        # # 把每一行的数字分隔后转化成int列表
        # values = list(map(int, line.split()))
        values = [1,2,3,4]
        magic(values)

    # [print(i) for i in ans]





