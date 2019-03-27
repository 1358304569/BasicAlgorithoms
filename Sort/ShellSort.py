
import random

"""
# 希尔排序：
# 基于插入排序的优化，将相距某个“增量”的记录组成一个子序列，对其进行排序，从而保证总的序列基本有序；
# 在元素较少，或基本有序时，插入排序效率很高；
# 时间复杂度为 n*log2 n

"""

def ShellSort(nums):
    # 设置初始增量
    increment = int(len(nums)/2)
    while increment > 0:
        # 接下来和插入排序一样，只是每次插入和挪动的步长为 increment，而非固定的 1
        for i in range(increment, len(nums)):
            tmp = nums[i]
            j = i - increment
            while j >= 0 and nums[j] > tmp:
                nums[j + increment] = nums[j]
                j -= increment
            nums[j + increment] = tmp
        # 在每次插入排序后，改变步长 increment 值，直到最后 increment = 1，就是普通的插入排序
        increment = int(increment/2)
    return nums



"""
# 简化写法的希尔排序
# 原理一样
"""
def ShellSortPlus(nums):
    n = len(nums)
    increment = int(n / 2)
    while increment > 0:
        for i in range(increment, n):
            while i >= increment and nums[i - increment] > nums[i]:
                nums[i - increment],nums[i] = nums[i], nums[i - increment]
                i -= increment
        increment = int(increment / 2)
    return nums





# 测试数据
def start():
    nums = [x*10 for x in range(1,11)]
    random.shuffle(nums)
    print(nums)

    print("===========排序后=================")
    # nums = ShellSort(nums)
    nums = ShellSortPlus(nums)
    print(nums)

if __name__ == '__main__':
    start()

