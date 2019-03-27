

import random

"""
# 这里先放一种最简单的交换排序：
"""
def SwapSort(nums):
    """
    @brief 简单的交换排序
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


"""
# 最基本的冒泡排序：
# 相邻的两个元素，两两比较
# 两个 for 循环，内循环每次得到一个最大（小）值，外循环为元素个数，直到最后一个待比较元素
"""
def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


"""
# 改进的冒泡排序：
# 上述冒泡排序中，对每个元素都进行了比较，但有时候比较几次后，就已经有序了，无需进行后续的比较。
# 优化方法：设置标志位，发现整体有序后，不再比较

# 如【5，1，2，3，8】
# 在经过第一次循环（i=0）后，就已经整体有序了，无需再对2后面的进行比较

"""
def BubbleSortPlus(nums):
    for i in range(len(nums)):
        flag = 0
        for j in range(len(nums)-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = 1
        if flag == 0:
            break
    return nums


# 测试数据


def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    # nums = SwapSort(nums)
    # nums = BubbleSort(nums)
    nums = BubbleSortPlus(nums)

    print(nums)

if __name__ == '__main__':
    start()


