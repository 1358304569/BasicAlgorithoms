#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zhouyijian
# datetime:2019-11-10 19:27
# software: IntelliJ IDEA


import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(input())
    ans = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        total = values[0] + values[1] + values[2]
        if (values[0] < 0 or values[1] < 0 or total < 3):
            # print(0)
            ans.append(0)
        else:
            # print(min(values[0],values[1]))
            ans.append(min(min(values[0],values[1]), int(total / 3)))
    [print(i) for i in ans]


