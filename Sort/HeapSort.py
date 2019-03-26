# coding:utf-8

import random,math

"""
# 堆排序：
# 基于二叉堆结构，主要运用了完全二叉树的性质：
# 根节点从 1 开始，则节点序号为 i 的左孩子序号为 2i，右孩子为 2i+1；
# 根节点从 0 开始，则节点序号为 i 的左孩子序号为 2i+1，右孩子为 2i+2；
# 最大堆：
"""
#网上找的打印树的一个函数，很好用
def print_tree(array): #打印堆排序使用
    '''
    深度 前空格 元素间空格
    1     7       0
    2     3       7
    3     1       3
    4     0       1
    '''
    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
    return nums

def HeapAdjust(nums, start, end):
    temp = nums[start]
    i = start
    # 从左孩子开始
    j = 2*i
    while j <= end:
        # 右孩子比左孩子大，则指向右
        # if nums[j] < nums[j+1]:         # j 会 out of range
        if j < end and (nums[j] < nums[j + 1]):
            j += 1
        # 孩子比双亲大，交换
        if temp < nums[j]:
            nums[i] = nums[j]
            i = j
            j = 2 * i
        else:
            break
    nums[i] = temp

def HeapSort(nums):
    n = len(nums)-1
    # 完全二叉树性质，第n/2个为双亲节点
    for i in range(int(n/2), 0, -1):
        HeapAdjust(nums, i, n)

    for j in range(n, 0, -1):
        nums = swap(nums, 1, j)
        HeapAdjust(nums, 1, j-1)
    return nums

# 原始数据
# nums = [0, 20, 10, 60, 100, 90, 30, 40, 50, 70, 80]
nums = [x*10 for x in range(1,11)]
random.shuffle(nums)
nums.insert(0, 0)
print(nums)
# print_tree(nums)
print("===========排序后=================")
nums = HeapSort(nums)
# print_tree(nums)
print(nums)
