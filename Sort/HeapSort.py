# coding:utf-8

import random,math

"""
# 堆排序：
# 基于二叉堆结构，主要运用了完全二叉树的性质：
# 根节点从 1 开始，则节点序号为 i 的左孩子序号为 2i，右孩子为 2i+1；
# 根节点从 0 开始，则节点序号为 i 的左孩子序号为 2i+1，右孩子为 2i+2；

# 二叉堆分为最大堆、最小堆，最大堆用于排序，最小堆用于实现优先队列
# 最大堆：根节点大于两个孩子节点，最小堆反之。

# 堆排序主要分为三步，：
1、将待排序列表构建成一个大顶堆；
2、将堆顶记录（最大值）与当前未经排序子序列的最后一个记录交换
3、再将剩下的 n-1 个元素重新构建为大顶堆，重复第二步，
其中关键部分就是如何构建大顶堆（HeapAdjust）

"""
#网上找的打印树的一个函数，很好用
def print_tree(array): #打印堆排序使用
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
        # 孩子比跟节点大，交换
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
    # 第一次构建为顶大堆
    for i in range(int(n/2), 0, -1):
        HeapAdjust(nums, i, n)

    # 将根节点（最大值）与最后一个节点交换，重新构建大顶堆
    for j in range(n, 0, -1):
        nums = swap(nums, 1, j)
        HeapAdjust(nums, 1, j-1)
    return nums

# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    # 此处插入0占位，使得根节点从1开始！！
    nums.insert(0, 0)
    print(nums)
    print_tree(nums)
    print("===========排序后=================")
    nums = HeapSort(nums)
    print_tree(nums)
    print(nums)

if __name__ == '__main__':
    start()


