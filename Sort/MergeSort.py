# coding:utf-8

import random
"""
# 归并排序
# 归并排序是分治法（Divide and Conquer）的典型思想
# 主要分为两个阶段：递归分解 与 结果合并
"""

def Merge(nums, l, m, r):
    """
    @brief 将左、右两个有序列表，合并成一个新的有序列表
    :param nums: 最终合成的结果列表
    :param l: 左边有序列表的左边界
    :param m: 左边有序列表的右边界
    :param r: 右边有序列表的右边界
    :return: 合并完成的有序列表
    """
    left = []
    right = []
    n1 = m - l +1   # 左边有序列表的长度
    n2 = r - m      # 右边有序列表的长度

    # 分解完后的左右两个列表，分别从 l 和 m+1开始
    for i in range(n1):
        left.append(nums[l + i])
    for j in range(n2):
        right.append(nums[m + 1 + j])

    i = 0
    j = 0
    k = l       # 注意，k 从左边界 l 开始，而不是0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        nums[k] = right[j]
        j += 1
        k += 1

def MergeSort(nums, l, r):
    """
    @brief 对待排序列表进行递归调用
    """
    # if l == r:
        # 此时只有一个元素了，返回
    if l < r:
        m = l + int((r - l)/2)
        MergeSort(nums, l, m)
        MergeSort(nums, m+1, r)
        # 分解出左、右两个序列，进行合并
        Merge(nums, l, m, r)


# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)     # 原始数据
    MergeSort(nums, 0, len(nums)-1)
    print(nums)     # 结果
if __name__ == "__main__":
    start()

